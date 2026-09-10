# Contributing to gsbdarc repositories

> **Status: PROPOSED — not adopted.** This is a draft convention put up for the
> team to review and discuss. Nothing here is enforced yet, and no existing repo
> has been changed to match it.

## Starting a new repository

- [ ] **Write a description.** One sentence saying what it is and, if it's for
      someone, who. 13 of our 75 repos have no description, which makes them
      invisible in any listing.
- [ ] **Name it to the convention below.**
- [ ] **Add topics** from [`docs/repo-topics.md`](docs/repo-topics.md) — three
      choices, about 30 seconds: exactly one **work type**, exactly one
      **`status-*`**, and `faculty-project` if it's for a named PI. Add stack
      tags if they help. Don't tag the vendor — that goes in the name.
- [ ] **Add a README** covering what it is, how to set it up, and how to
      reproduce the results.
- [ ] **Add a `.gitignore` before the first commit**, including `.env`.
- [ ] **Check no credentials are in the history**, not just the working tree.

## Naming convention

**These rules apply to new repositories only.** Existing repos are *not* being
renamed — renaming breaks clones, bookmarks, and inbound links for everyone who
already has the repo, which costs more than the inconsistency does.

Three rules:

1. **All lowercase.**
2. **Hyphens, never underscores**, and no CamelCase.
3. **No filler suffixes** — `_code`, `_Scripts`, `-test-` say nothing.

Then match the pattern for the kind of work:

| Kind of repo | Pattern | Follows it today |
|---|---|---|
| Data acquisition | `<vendor>-<dataset>-etl` | `sensor-tower-data-etl` |
| Work for one PI | `<pi-lastname>-<topic>` | `monin-video-rating-survey` |
| Taught course | `<audience>-<kind>-<year>` | `yens-onboarding-2026` |
| Tool or app | `<thing>-<kind>` | `slurm-viz`, `qualtrics-proxy` |

### Where we currently drift

Listed to make the convention concrete, not as a to-do:

| Repo | Issue |
|---|---|
| `preqin-data-ETL`, `sp-panjiva-ETL`, `pitchbook-feed-ETL`, `comscore-data-ETL`, `dnb-establishment-data-ETL`, `data-axle-reference-usa-ETL`, `sp-451-research-datacenters-ETL`, `kpler-maritime-gcp-ETL` | uppercase `-ETL`; only `sensor-tower-data-etl` is lowercase |
| `gelfand_scientific-disciplines-datasets`, `jungho_state-regulations`, `shosh_freightos_pipeline` | underscore after the PI name |
| `rf_bootcamp_2024`, `rf_bootcamp_2025`, `intro_to_yens_2024`, `intermediate_yens_2024` | underscores throughout |
| `Vast_Scripts`, `LLM_YEN_BENCHMARK`, `Qlora_code`, `City_council_meeting_parser`, `Structured_output_blog-test-` | mixed case, underscores, filler suffixes, trailing hyphen |
| `HHT_titantic` | typo — "titantic" |

### The vendor goes in the name, not a topic

This is load-bearing, not cosmetic. There is deliberately **no data-source
topic** in the taxonomy, because the repo name already carries it:
`q=pitchbook in:name` finds `pitchbook-feed-ETL` today. Across all 75 repos
exactly one has a source invisible in its name
(`gelfand_scientific-disciplines-datasets` → Web of Science), and one repo is not
worth a 16-term facet.

So: **if the repo is about a specific vendor or dataset, the vendor's name must
be in the repo name.** If it can't be — an omnibus repo, or an NDA that makes the
vendor name awkward in a public listing — put it in the description instead.

The `-ETL` suffix is the interesting case: **8 of 9 repos use uppercase**, so
lowercase `-etl` is the minority spelling today. It's proposed anyway because
lowercase is the broader GitHub convention and keeps repo names consistent with
topic names — but that's a judgment call worth arguing about, not a settled fact.

## Working in a repository

We follow [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow):
branch → commit → pull request → review → merge → delete the branch. `main`
stays working.

- **Log problems as issues**, even ones you fix immediately, so the problem is on
  the record and not just the fix.
- **Say why, not just what** in commit messages and PR descriptions.
- **Link the issue** from the PR that resolves it (`Closes #12`).
- **Never commit secrets.** Keep them in an ignored `.env` and commit a
  `.env.example` listing the *names* of required keys. If one does leak, rotate
  it first — scrubbing history alone is not enough.
- **Validate data transformations.** Any step that cleans, merges, or filters
  data gets checks saved next to it (row counts, types, uniqueness, ranges).
  Raw data is read-only; derived data goes somewhere else.

## Where AI assistance is involved

So it's clear who did what: commits made with an AI assistant carry a
`Co-Authored-By:` trailer, and pull requests it drafted say so in the
description. See `claude-code-best-practices` for credential scoping and
settings templates.
