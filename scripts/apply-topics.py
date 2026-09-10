#!/usr/bin/env python3
"""Validate docs/topics.yml and apply it to the gsbdarc org.

Writes nothing unless --apply is passed. Strictly additive: a topic already on a
repo is never removed, so deprecated spellings are left exactly as they are.

    ./scripts/apply-topics.py              # validate + show the diff
    ./scripts/apply-topics.py --check      # validate only, exit 1 on any problem
    ./scripts/apply-topics.py --apply      # write (asks for confirmation)

Needs the `gh` CLI, authenticated with a token that can write repo metadata.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit(
        "This script needs PyYAML.\n"
        "  pip install pyyaml          (or: /usr/bin/python3 scripts/apply-topics.py ...)"
    )

ORG = "gsbdarc"
GITHUB_MAX_TOPICS = 20
ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "docs" / "topics.yml"
DOC = ROOT / "docs" / "repo-topics.md"


def gh_json(*args):
    """Run gh and parse JSON, failing loudly rather than returning a default."""
    proc = subprocess.run(
        ["gh", *args], capture_output=True, text=True
    )
    if proc.returncode != 0:
        raise SystemExit(f"gh {' '.join(args)} failed:\n{proc.stderr.strip()}")
    return json.loads(proc.stdout)


def fetch_org_topics():
    """Every repo in the org with its current topics. Paginated deliberately --
    a truncated listing would read as 'this repo has no topics' and the additive
    merge would look correct while silently proposing a no-op."""
    repos = gh_json(
        "api", "--paginate", f"/orgs/{ORG}/repos?per_page=100&type=all"
    )
    return {r["name"]: sorted(r["topics"]) for r in repos}


def validate(manifest, org_topics):
    """Collect every problem rather than exiting on the first one."""
    problems = []
    facets = manifest["facets"]
    vocab = {t: f for f, terms in facets.items() for t in terms}

    # --- the doc and the manifest must describe the same vocabulary ---
    doc_text = DOC.read_text()
    doc_terms = set(re.findall(r"`([a-z0-9][a-z0-9-]*)`", doc_text))
    for term in sorted(vocab):
        if term not in doc_terms:
            problems.append(f"vocabulary: `{term}` is in topics.yml but not documented in {DOC.name}")

    # --- GitHub's own naming rule ---
    for term in sorted(vocab):
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,49}", term):
            problems.append(f"vocabulary: `{term}` is not a legal GitHub topic (lowercase, digits, hyphens; <=50 chars)")

    # --- the manifest must cover the org exactly ---
    proposed = manifest["repos"]
    for name in sorted(set(org_topics) - set(proposed)):
        problems.append(f"coverage: {name} exists in the org but is missing from topics.yml")
    for name in sorted(set(proposed) - set(org_topics)):
        problems.append(f"coverage: {name} is in topics.yml but not in the org")

    # --- per-repo invariants ---
    for name, topics in sorted(proposed.items()):
        if topics is None:
            problems.append(f"{name}: no topics listed")
            continue
        dupes = {t for t in topics if topics.count(t) > 1}
        if dupes:
            problems.append(f"{name}: duplicate topics {sorted(dupes)}")

        unknown = [t for t in topics if t not in vocab and t not in manifest["deprecated"]]
        if unknown:
            problems.append(f"{name}: undefined topics {sorted(unknown)} -- add them to facets: and to {DOC.name}")

        by_facet = {}
        for t in topics:
            if t in vocab:
                by_facet.setdefault(vocab[t], []).append(t)

        work = by_facet.get("work-type", [])
        if len(work) != 1:
            problems.append(f"{name}: needs exactly one work-type topic, has {len(work)} {sorted(work)}")

        life = by_facet.get("lifecycle", [])
        if len(life) != 1:
            problems.append(f"{name}: needs exactly one status-* topic, has {len(life)} {sorted(life)}")

        years = by_facet.get("year", [])
        needs_year = bool(set(life) & {"status-inactive", "status-archived"})
        if needs_year and len(years) != 1:
            problems.append(f"{name}: {life[0] if life else '?'} requires exactly one last-active-YYYY, has {sorted(years)}")
        if not needs_year and years:
            problems.append(f"{name}: {sorted(years)} only belongs on status-inactive / status-archived")

        # additive merge is what actually lands -- check the limit against that
        final = set(topics) | set(org_topics.get(name, []))
        if len(final) > GITHUB_MAX_TOPICS:
            problems.append(f"{name}: would end up with {len(final)} topics, over GitHub's limit of {GITHUB_MAX_TOPICS}")

    # --- every documented term should actually be used, or it is dead vocabulary ---
    used = {t for ts in proposed.values() for t in (ts or [])}
    for term in sorted(set(vocab) - used):
        problems.append(f"vocabulary: `{term}` is defined but no repo uses it")

    return problems


def plan(manifest, org_topics):
    """Additive merge. Returns [(repo, current, final, added)] for repos that change."""
    changes = []
    for name, proposed in sorted(manifest["repos"].items(), key=lambda kv: kv[0].lower()):
        current = set(org_topics.get(name, []))
        final = current | set(proposed)
        added = sorted(final - current)
        if added:
            changes.append((name, sorted(current), sorted(final), added))
    return changes


def confirm(n):
    """Read from the terminal, not stdin -- a piped or redirected stdin must not
    be able to answer this for us."""
    try:
        with open("/dev/tty") as tty:
            sys.stderr.write(f"\nWrite topics to {n} repos in `{ORG}`? [y/N] ")
            sys.stderr.flush()
            return tty.readline().strip().lower() in {"y", "yes"}
    except OSError:
        raise SystemExit("Refusing to apply: no terminal available to confirm. Run interactively.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="actually write topics (default is a dry run)")
    ap.add_argument("--check", action="store_true", help="validate only; exit 1 if anything is wrong")
    args = ap.parse_args()

    manifest = yaml.safe_load(MANIFEST.read_text())
    org_topics = fetch_org_topics()

    problems = validate(manifest, org_topics)
    if problems:
        print(f"{len(problems)} problem(s) found:\n", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        raise SystemExit(1)
    print(f"validation passed: {len(manifest['repos'])} repos, "
          f"{sum(len(v) for v in manifest['facets'].values())} vocabulary terms")

    if args.check:
        return

    changes = plan(manifest, org_topics)
    for name, current, final, added in changes:
        print(f"\n{name}")
        for t in current:
            note = "  (deprecated, kept)" if t in manifest["deprecated"] else ""
            print(f"    = {t}{note}")
        for t in added:
            print(f"    + {t}")

    n_noop = len(manifest["repos"]) - len(changes)
    print(f"\n{len(changes)} repos would gain topics, {n_noop} unchanged. "
          f"No topic is ever removed.")

    if not args.apply:
        print("\nDry run -- nothing was written. Re-run with --apply to write.")
        return

    if not confirm(len(changes)):
        raise SystemExit("Aborted; nothing written.")

    failed = []
    for name, _current, final, _added in changes:
        cmd = ["gh", "api", "-X", "PUT", f"/repos/{ORG}/{name}/topics"]
        for t in final:
            cmd += ["-f", f"names[]={t}"]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            failed.append((name, proc.stderr.strip()))
            print(f"  FAILED {name}: {proc.stderr.strip()}", file=sys.stderr)
            continue
        # re-read rather than trusting the write
        landed = set(gh_json("api", f"/repos/{ORG}/{name}/topics")["names"])
        if not set(final) <= landed:
            failed.append((name, f"expected {sorted(set(final) - landed)} to land, they did not"))
            print(f"  MISMATCH {name}: {sorted(set(final) - landed)} missing after write", file=sys.stderr)
        else:
            print(f"  ok {name} ({len(landed)} topics)")

    if failed:
        raise SystemExit(f"\n{len(failed)} of {len(changes)} repos failed; see above.")
    print(f"\napplied to {len(changes)} repos, all verified by re-read.")


if __name__ == "__main__":
    main()
