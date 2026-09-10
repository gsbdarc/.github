# Repository topics: a proposed taxonomy for gsbdarc

> **Status: PROPOSED — not adopted, and nothing has been applied.**
> No repository's topics have been changed. This document,
> [`topics.yml`](topics.yml) and [`proposed-changes.md`](proposed-changes.md)
> exist so the team can review and discuss the scheme before any of it takes
> effect.

**29 topics, four facets.** Deliberately lean: a scheme nobody can remember is a
scheme nobody applies.

## The problem

The org has 75 repositories and no working way to browse them.

- **62 of 75 (83%) have no topics at all.**
- The handful that do drifted almost immediately: `etl-pipeline`, `etl`, and
  `data-etl` were three spellings of one idea. The cause is traceable — the only
  place topics were ever documented is one line in
  `data-etl-template/TEMPLATE_USAGE.md` telling new repos to tag `etl`, while
  the siblings used `etl-pipeline`. Every repo made from the template re-created
  the split.
- `data-engineering` (10 repos) can't tell a school-wide licensed data asset
  (`pitchbook-feed-ETL`) from one PI's pipeline (`shosh_freightos_pipeline`).
- 13 repos have had no push since 2024 and 3 are empty, but **nothing is
  archived** — so the listing gives no signal about what is still alive.

## The four facets

| Facet | Rule | Terms |
|---|---|---|
| **Work type** — what kind of work this is | exactly one | 6 |
| **Client** — who it's for | optional | 1 |
| **Stack** — what it runs on | optional, any number | 13 |
| **Lifecycle** — is it alive? | exactly one | 5 + 4 years |

Only terms on this page are valid. A new term gets added here in the same pull
request that first uses it — that is the mechanism that stops the vocabulary
splintering again.

## Facet 1 — Work type (exactly one, required)

| Topic | Use it for | Repos |
|---|---|---|
| `data-delivery` | Vendor or external data acquired and delivered to researchers | 15 |
| `research-computing` | The Yens and cluster: compute, GPUs, environments, platform docs | 16 |
| `training` | Courses, bootcamps, workshops, how-to content | 16 |
| `internal-ops` | DARC's own workflow and operations tooling | 13 |
| `research-support` | Analysis or method code written for one specific research question | 8 |
| `app-build` | Building or supporting an application, dashboard, or survey instrument | 7 |

The line between `data-delivery` and `research-support` is **who the data is
for**: many researchers, or one question. `pitchbook-feed-ETL` serves the school
(`data-delivery`); `jungho_state-regulations` builds a corpus for one paper
(`research-support`).

Work type describes the **purpose**, not the implementation. `slurm-viz` is a web
dashboard, but it exists to make the cluster legible, so it's
`research-computing` rather than `app-build`.

## Facet 2 — Client (optional)

`faculty-project` — this repo is work for a named PI or lab.

**This is orthogonal to work type, not one of its values.** A faculty engagement
can be data work, an app build, or analysis, and you want it findable both ways:

```
topic:faculty-project                            -> 12 repos
topic:faculty-project topic:app-build            ->  4   (the Qualtrics/LLM studies)
topic:faculty-project topic:research-support      ->  6   (the analysis engagements)
topic:faculty-project topic:data-delivery         ->  1   (shosh_freightos_pipeline)
```

Filing faculty work *under* `faculty-project` as its work type would mean "show
me every app we've built" silently omits four of them.

## Facet 3 — Stack (optional, any number)

What it runs on. **Every term here is earned by at least two repos** — a tag on
one repo is a note, not a facet, and belongs in the description.

`yens` (21) · `llm` (17) · `claude-code` (11) · `gpu` (6) · `google-cloud` (6) ·
`terraform` (6) · `qualtrics` (5) · `slurm` (5) · `aws` (4) · `sherlock` (3) ·
`docker` (3) · `web-scraping` (3) · `redivis` (2)

Spellings follow GitHub's community-standard names where one exists
(`google-cloud`, not `gcp`).

### Not in this facet, on purpose

**Programming languages.** GitHub derives them from file contents and the org
listing already has a native Language filter. Tagging `python` duplicates that
and goes stale.

**Vendors and data sources.** The vendor belongs in the **repo name**, not a
topic. `q=pitchbook in:name` already finds `pitchbook-feed-ETL`, and across all
75 repos exactly **one** has a data source invisible in its name
(`gelfand_scientific-disciplines-datasets` → Web of Science). One repo does not
justify a 16-term facet; put Web of Science in that repo's description.

## Facet 4 — Lifecycle (exactly one, required)

| Topic | Meaning |
|---|---|
| `status-active` | Under development now |
| `status-maintained` | Stable and supported; changes are occasional |
| `status-inactive` | No longer worked on, kept for reference |
| `status-archived` | Retired or superseded |
| `status-experimental` | A prototype or spike; may break, don't depend on it |

`status-inactive` and `status-archived` **must** carry a year tag recording when
work stopped: `last-active-2023` · `last-active-2024` · `last-active-2025` ·
`last-active-2026`

**The year is frozen when the repo goes inactive, so it never needs updating.**
Active repos get no year tag — otherwise every January would need a re-tagging
sweep across the org, which is exactly the upkeep that gets skipped and leaves
labels quietly lying to you.

Where the line falls here: no push in the last 12 months is `status-inactive`,
tagged with the year of the last push. Two deliberate exceptions:

- **Superseded annual courses.** `yens-onboarding-2025` was pushed within 12
  months but `yens-onboarding-2026` replaced it. An annual course repo is
  *supposed* to be a frozen snapshot of the year it was taught; `status-inactive`
  + `last-active-2025` says so instead of making it look abandoned.
- **Empty repos.** `softball-lineup-maker`, `test-agent` and `Qlora_code` have no
  content at all, so they're `status-archived`.

## Worked examples

```
sensor-tower-data-etl     data-delivery  sherlock slurm redivis aws  status-active
monin-video-rating-survey app-build  faculty-project  qualtrics       status-active
vllm_helper               research-computing  yens sherlock gpu llm   status-maintained
intro_to_yens_2024        training  yens          status-inactive  last-active-2024
paperrag                  research-support  llm                      status-experimental
```

Four to six topics each. GitHub's limit is 20.

## Deprecated spellings (left in place, not removed)

We would stop using these on **new** repos. They are **not** removed from repos
that carry them — the proposal is strictly additive and
[`apply-topics.py`](../scripts/apply-topics.py) never deletes a topic.

| Deprecated | Prefer | On repos today |
|---|---|---|
| `data-engineering` | `data-delivery` | 10 |
| `etl` / `data-etl` | `etl-pipeline`, or nothing — implied by `data-delivery` | 0 (already cleaned up) |
| `survey` | `survey-research` | 1 |
| `template` | `repo-template` | 1 |
| `javascript` | *(nothing — GitHub derives languages)* | 1 |

This costs nothing in findability: because the canonical term is **added**
everywhere it belongs, filtering works whether or not an old alias sits next to
it. Actually retiring any of them is a separate, later decision.

## Open questions for review

**1. Is `internal-ops` doing too much?** At 13 repos it holds DARC tooling
(`darc-orchestrator`, `darc-staff-skills`) alongside prototypes and dead ends
(`promptops`, `test-agent`, `Structured_output_blog-test-`). An `rnd` work type
would separate experiments from real internal tooling — though
`status-experimental` already flags most of them.

**2. Should dormant repos also get GitHub's native archive flag?** The `status-*`
+ year tags are proposed here because they carry *when*, which the flag doesn't.
But the native flag also makes a repo read-only and greys it out in listings — a
stronger signal for the 3 empty repos. The two aren't exclusive.

**3. Should recurring content series get tags?** `image_ai_HHT`,
`reproducibility_HHT` and `HHT_titantic` are one real "Hub How-To" series with
nothing tying them together; same for `rf_bootcamp_*` and `pearc26-*`. Left out
to keep the vocabulary at 29.

**4. The boundary calls most worth challenging.** `bay-area-smoke` and `sf311`
are `training` (worked-example analyses) rather than `research-support`;
`rcpedia` is `research-computing` (it documents the platform) rather than
`training`; `hackingresources` is `data-delivery` rather than `internal-ops`;
`paperrag` is `research-support` rather than `internal-ops`.

## GitHub's constraints

- Topics allow **lowercase letters, numbers and hyphens only** — no colons, dots
  or uppercase. That's why lifecycle reads `status-active`, not `status:active`.
- **Maximum 20 topics per repo**, 50 characters each.
- The topics API **replaces** a repo's entire topic list rather than adding to
  it. Any change must go through
  [`scripts/apply-topics.py`](../scripts/apply-topics.py), which reads the
  current list and merges — never a bare `PUT`.

<!-- Reference: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics -->
