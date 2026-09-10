# Repository topics for gsbdarc

> **Status: PROPOSED — nothing has been applied.** No repository's topics have
> been changed. This document is the whole proposal: the taxonomy, and the
> topics proposed for every repo. [`topics.yml`](topics.yml) is the same thing
> machine-readable.

Deliberately lean — a scheme nobody can remember is a scheme nobody applies.
Tagging a new repo is **three choices, about 30 seconds**: one work type, one
status, and `faculty-project` if it's for a named PI.

## The problem

The org has 75 repositories and no working way to browse them.

- **62 of 75 (83%) have no topics at all.**
- The handful that do drifted almost immediately: `etl-pipeline`, `etl` and
  `data-etl` were three spellings of one idea. The cause is traceable — the only
  place topics were ever documented is one line in
  `data-etl-template/TEMPLATE_USAGE.md` telling new repos to tag `etl` while the
  siblings used `etl-pipeline`, so every repo made from the template re-created
  the split.
- `data-engineering` can't tell a school-wide licensed data asset
  (`pitchbook-feed-ETL`) from one PI's pipeline (`shosh_freightos_pipeline`).
  Both carry it.
- 13 repos have had no push since 2024 and 3 are empty, but **nothing is
  archived** — so the listing gives no signal about what is still alive.
- Names encode category inconsistently (`preqin-data-ETL` vs
  `sensor-tower-data-etl`), so browsing by name doesn't work either.

## The four facets

| Facet | Rule |
|---|---|
| **Work type** — what kind of work this is | exactly one, required |
| **Client** — who it's for | optional |
| **Stack** — what it runs on | optional, any number |
| **Lifecycle** — is it alive? | exactly one, required |

Only terms in this document are valid. A new term gets added here in the same
pull request that first uses it — that is the mechanism that stops the
vocabulary splintering again. Exact terms and usage counts are in
[The proposal, in full](#the-proposal-in-full).

### Facet 1 — Work type

Two rules resolve almost every hard case.

**Who is it for?** That's the line between `data-delivery` and
`research-support`: many researchers, or one question. `pitchbook-feed-ETL`
serves the school; `jungho_state-regulations` builds a corpus for one paper.

**Purpose, not implementation.** `slurm-viz` is a web dashboard, but it exists to
make the cluster legible, so it's `research-computing`, not `app-build`.

### Facet 2 — Client

`faculty-project` — work for a named PI or lab.

**This is orthogonal to work type, not one of its values.** A faculty engagement
can be data work, an app build, or analysis, and it should be findable both ways.
Filing faculty work *under* `faculty-project` as its work type would mean "show
me every app we've built" silently omits the faculty ones.

### Facet 3 — Stack

What it runs on. **Every term is earned by at least two repos** — a tag on one repo is a note, not a facet, and belongs in the
description. Spellings follow GitHub's community-standard names where one exists
(`google-cloud`, not `gcp`).

#### Three things deliberately not tagged

**Programming languages.** GitHub derives them from file contents and the org
listing already has a native Language filter. Tagging `python` duplicates that
and goes stale.

**Vendors and data sources.** The vendor belongs in the **repo name**.
`q=pitchbook in:name` already finds `pitchbook-feed-ETL`, and across all 75 repos
exactly *one* has a data source invisible in its name
(`gelfand_scientific-disciplines-datasets` → Web of Science) — not worth a
sixteen-term facet. Put Web of Science in that repo's description instead.

The decisive argument is what the existing tags actually look like: **the vendor
facet reached only 9 of the 15 data repos.** `preqin-data-ETL` and
`edgar-yens-mirror` never got one despite having obvious vendors. A facet applied
to some of its population is worse than none at all, because absence stops
meaning anything — you can't tell "no Preqin data" from "nobody tagged it." So
the nine existing vendor tags are removed rather than the facet completed. The
naming convention in [`CONTRIBUTING.md`](../CONTRIBUTING.md) is what makes this
hold for new repos.

**Pipelines.** `etl-pipeline` was on 10 repos and is dropped: 13 of the 15 repos
it would cover are already `data-delivery`, so it restates the work type. The two
exceptions (`jungho_state-regulations`, `pubsubgpt_pipeline`) don't earn a term
applied to 15 repos. If "which pipelines do we operate?" turns out to be a
question worth asking, `topic:data-delivery` is the answer and reinstating this
is one line — see open question 5.

### Facet 4 — Lifecycle

`status-inactive` and `status-archived` **must** carry a `last-active-YYYY` tag
recording when work stopped.

**The year is frozen when the repo goes inactive, so it never needs updating.**
Active repos get no year tag — otherwise every January would need a re-tagging
sweep across the org, which is exactly the upkeep that gets skipped and leaves
labels quietly lying to you.

Where the line falls: no push in the last 12 months is `status-inactive`, tagged
with the year of the last push. Two deliberate exceptions:

- **Superseded annual courses.** `yens-onboarding-2025` was pushed within 12
  months but `yens-onboarding-2026` replaced it. An annual course repo is
  *supposed* to be a frozen snapshot of the year it was taught; `status-inactive`
  + `last-active-2025` says so instead of making it look abandoned.
- **Empty repos.** `softball-lineup-maker`, `test-agent` and `Qlora_code` have no
  content at all, so they're `status-archived`.

## What gets deleted

Removals are **enumerated, not inferred.** Absence from `topics.yml` is
deliberately *not* a delete signal, and only the terms listed under `remove:`
are ever deleted — see [the summary below](#what-changes-on-apply).

The list is long — it includes the nine vendor tags and `etl-pipeline` — but
enumeration still matters, for what happens *next*. An authoritative manifest
would silently wipe anything not listed in it, so a tag someone adds in the
GitHub UI next month gets reverted on the following run with no trace.
Enumerating removals keeps every deletion something a person wrote down and a
reason they wrote next to it.

The counterpart is a totality check: **every topic live in the org must be either
in the vocabulary or in `remove:`.** Nothing is allowed to sit unaccounted for.
That check is what surfaced the nine vendor tags in the first place — they were
neither blessed nor slated for removal, so they would have persisted forever.

## Open questions for review

**1. Is `internal-ops` doing too much?** It holds real DARC tooling
(`darc-orchestrator`, `darc-staff-skills`) alongside prototypes and dead ends
(`promptops`, `test-agent`, `Structured_output_blog-test-`). An `rnd` work type
would separate experiments from tooling we depend on — though
`status-experimental` already flags most of them.

**2. Should dormant repos also get GitHub's native archive flag?** The `status-*`
+ year tags are proposed here because they carry *when*, which the flag doesn't.
But the flag also makes a repo read-only and greys it out in listings — a
stronger signal for the 3 empty repos. The two aren't exclusive.

**3. Should recurring content series get tags?** `image_ai_HHT`,
`reproducibility_HHT` and `HHT_titantic` are one real "Hub How-To" series with
nothing tying them together; same for `rf_bootcamp_*` and `pearc26-*`. Left out
to keep the vocabulary small.

**4. The boundary calls most worth challenging.** `bay-area-smoke` and `sf311`
are `training` (worked-example analyses) rather than `research-support`;
`rcpedia` is `research-computing` (it documents the platform) rather than
`training`; `hackingresources` is `data-delivery` rather than `internal-ops`;
`paperrag` is `research-support` rather than `internal-ops`.

**5. Was dropping `etl-pipeline` right?** It's the closest call here. It was on
10 repos and is a well-recognised GitHub topic, and it does say something work
type doesn't for two repos. Reinstating it means adding it to `facets: stack`,
removing it from `remove:`, and re-rendering — about a one-line change either
way, so it's cheap to reverse if "which pipelines do we run?" turns out to be a
question people actually ask.

## GitHub's constraints

- Topics allow **lowercase letters, numbers and hyphens only** — no colons, dots
  or uppercase. That's why lifecycle reads `status-active`, not `status:active`.
- **Maximum 20 topics per repo**, 50 characters each.
- The topics API **replaces** a repo's entire topic list rather than adding to
  it, so changes must go through
  [`scripts/apply-topics.py`](../scripts/apply-topics.py), which reads the
  current list and merges — never a bare `PUT`.

---

<!-- BEGIN GENERATED -- edit docs/topics.yml, then run: scripts/apply-topics.py --render -->

## The proposal, in full

*Generated from [`topics.yml`](topics.yml) -- 75 repos, 29 topics. Do not edit by hand; run `scripts/apply-topics.py --render`.*

### The vocabulary

**Work type (exactly one)** — 6 terms  
`research-computing` (16) · `training` (16) · `data-delivery` (15) · `internal-ops` (13) · `research-support` (8) · `app-build` (7)

**Client (optional)** — 1 term  
`faculty-project` (12)

**Stack (optional)** — 13 terms  
`yens` (21) · `llm` (17) · `claude-code` (11) · `google-cloud` (6) · `gpu` (6) · `terraform` (6) · `qualtrics` (5) · `slurm` (5) · `aws` (4) · `docker` (3) · `sherlock` (3) · `web-scraping` (3) · `redivis` (2)

**Lifecycle (exactly one)** — 5 terms  
`status-active` (38) · `status-inactive` (17) · `status-maintained` (10) · `status-experimental` (7) · `status-archived` (3)

**Year (required if inactive/archived)** — 4 terms  
`last-active-2024` (10) · `last-active-2025` (5) · `last-active-2023` (3) · `last-active-2026` (2)

### `faculty-project` spans work types

12 repos carry it, which is why it is a separate facet:

```
topic:faculty-project topic:research-support     ->  7
topic:faculty-project topic:app-build            ->  4
topic:faculty-project topic:data-delivery        ->  1
```

### Proposed topics per repo

#### `data-delivery` — 15 repos

| Repo | Other topics |
|---|---|
| [`comscore-data-ETL`](https://github.com/gsbdarc/comscore-data-ETL) | `status-active` |
| [`data-axle-reference-usa-ETL`](https://github.com/gsbdarc/data-axle-reference-usa-ETL) | `status-active` |
| [`data-etl-template`](https://github.com/gsbdarc/data-etl-template) | `status-maintained` |
| [`dnb-establishment-data-ETL`](https://github.com/gsbdarc/dnb-establishment-data-ETL) | `status-active` |
| [`edgar-yens-mirror`](https://github.com/gsbdarc/edgar-yens-mirror) | `yens` `status-active` |
| [`gcp-scraping-terraform`](https://github.com/gsbdarc/gcp-scraping-terraform) | `google-cloud` `terraform` `web-scraping` `status-inactive` `last-active-2025` |
| [`hackingresources`](https://github.com/gsbdarc/hackingresources) | `web-scraping` `status-experimental` |
| [`kpler-maritime-gcp-ETL`](https://github.com/gsbdarc/kpler-maritime-gcp-ETL) | `google-cloud` `terraform` `status-active` |
| [`pitchbook-feed-ETL`](https://github.com/gsbdarc/pitchbook-feed-ETL) | `redivis` `status-active` |
| [`preqin-data-ETL`](https://github.com/gsbdarc/preqin-data-ETL) | `aws` `status-active` |
| [`sensor-tower-data-etl`](https://github.com/gsbdarc/sensor-tower-data-etl) | `sherlock` `slurm` `redivis` `aws` `status-active` |
| [`shosh_freightos_pipeline`](https://github.com/gsbdarc/shosh_freightos_pipeline) | `faculty-project` `status-active` |
| [`sp-451-research-datacenters-ETL`](https://github.com/gsbdarc/sp-451-research-datacenters-ETL) | `status-active` |
| [`sp-panjiva-ETL`](https://github.com/gsbdarc/sp-panjiva-ETL) | `status-active` |
| [`wos-starter-api-app`](https://github.com/gsbdarc/wos-starter-api-app) | `status-maintained` |

#### `app-build` — 7 repos

| Repo | Other topics |
|---|---|
| [`behavior-lab-chatbot`](https://github.com/gsbdarc/behavior-lab-chatbot) | `faculty-project` `llm` `qualtrics` `terraform` `status-active` |
| [`gsb-qualtrics-ai-chatbot`](https://github.com/gsbdarc/gsb-qualtrics-ai-chatbot) | `llm` `qualtrics` `google-cloud` `terraform` `status-maintained` |
| [`monin-video-aws-delivery`](https://github.com/gsbdarc/monin-video-aws-delivery) | `faculty-project` `aws` `terraform` `qualtrics` `status-active` |
| [`monin-video-rating-survey`](https://github.com/gsbdarc/monin-video-rating-survey) | `faculty-project` `qualtrics` `status-active` |
| [`qualtrics-proxy`](https://github.com/gsbdarc/qualtrics-proxy) | `qualtrics` `status-experimental` |
| [`saml-fullstack-stanford`](https://github.com/gsbdarc/saml-fullstack-stanford) | `terraform` `aws` `google-cloud` `status-active` |
| [`wjnkim-llm-study`](https://github.com/gsbdarc/wjnkim-llm-study) | `faculty-project` `llm` `google-cloud` `docker` `status-active` |

#### `research-computing` — 16 repos

| Repo | Other topics |
|---|---|
| [`claude-code-sandbox`](https://github.com/gsbdarc/claude-code-sandbox) | `docker` `claude-code` `status-experimental` |
| [`gsb-yen`](https://github.com/gsbdarc/gsb-yen) | `yens` `status-active` |
| [`LLM_benchmarks`](https://github.com/gsbdarc/LLM_benchmarks) | `llm` `status-active` |
| [`llm_inference`](https://github.com/gsbdarc/llm_inference) | `yens` `gpu` `llm` `status-inactive` `last-active-2024` |
| [`LLM_YEN_BENCHMARK`](https://github.com/gsbdarc/LLM_YEN_BENCHMARK) | `yens` `gpu` `llm` `status-active` |
| [`multi-fixmask`](https://github.com/gsbdarc/multi-fixmask) | `yens` `status-maintained` |
| [`ollama_helper`](https://github.com/gsbdarc/ollama_helper) | `yens` `sherlock` `gpu` `llm` `status-inactive` `last-active-2025` |
| [`pubsubgpt_pipeline`](https://github.com/gsbdarc/pubsubgpt_pipeline) | `google-cloud` `llm` `status-inactive` `last-active-2024` |
| [`Qlora_code`](https://github.com/gsbdarc/Qlora_code) | `yens` `llm` `status-archived` `last-active-2024` |
| [`rcpedia`](https://github.com/gsbdarc/rcpedia) | `yens` `status-active` |
| [`slurm-viz`](https://github.com/gsbdarc/slurm-viz) | `yens` `slurm` `status-active` |
| [`Vast_Scripts`](https://github.com/gsbdarc/Vast_Scripts) | `yens` `status-experimental` |
| [`vllm_helper`](https://github.com/gsbdarc/vllm_helper) | `yens` `sherlock` `gpu` `llm` `status-maintained` |
| [`yen_cluster_skills`](https://github.com/gsbdarc/yen_cluster_skills) | `yens` `slurm` `claude-code` `status-active` |
| [`yenbox`](https://github.com/gsbdarc/yenbox) | `yens` `docker` `claude-code` `status-experimental` |
| [`yens-gpu-demo`](https://github.com/gsbdarc/yens-gpu-demo) | `yens` `gpu` `status-inactive` `last-active-2023` |

#### `research-support` — 8 repos

| Repo | Other topics |
|---|---|
| [`City_council_meeting_parser`](https://github.com/gsbdarc/City_council_meeting_parser) | `faculty-project` `llm` `status-active` |
| [`gelfand_scientific-disciplines-datasets`](https://github.com/gsbdarc/gelfand_scientific-disciplines-datasets) | `faculty-project` `status-active` |
| [`green-patents`](https://github.com/gsbdarc/green-patents) | `faculty-project` `status-inactive` `last-active-2024` |
| [`jungho_state-regulations`](https://github.com/gsbdarc/jungho_state-regulations) | `faculty-project` `llm` `status-active` |
| [`paperrag`](https://github.com/gsbdarc/paperrag) | `llm` `status-experimental` |
| [`recombinant-search`](https://github.com/gsbdarc/recombinant-search) | `faculty-project` `status-inactive` `last-active-2025` |
| [`sam-and-guy-ad-transparency-center`](https://github.com/gsbdarc/sam-and-guy-ad-transparency-center) | `faculty-project` `web-scraping` `status-inactive` `last-active-2023` |
| [`Saumitra-FrenchOCR-Lemay`](https://github.com/gsbdarc/Saumitra-FrenchOCR-Lemay) | `faculty-project` `llm` `status-maintained` |

#### `training` — 16 repos

| Repo | Other topics |
|---|---|
| [`bay-area-smoke`](https://github.com/gsbdarc/bay-area-smoke) | `status-maintained` |
| [`claude-skill-github-for-research`](https://github.com/gsbdarc/claude-skill-github-for-research) | `claude-code` `status-active` |
| [`gsb-research-computing-ai-skills`](https://github.com/gsbdarc/gsb-research-computing-ai-skills) | `yens` `slurm` `gpu` `claude-code` `status-active` |
| [`HHT_titantic`](https://github.com/gsbdarc/HHT_titantic) | `status-maintained` |
| [`image_ai_HHT`](https://github.com/gsbdarc/image_ai_HHT) | `status-inactive` `last-active-2024` |
| [`intermediate_yens_2024`](https://github.com/gsbdarc/intermediate_yens_2024) | `yens` `status-inactive` `last-active-2024` |
| [`intro_to_yens_2024`](https://github.com/gsbdarc/intro_to_yens_2024) | `yens` `status-inactive` `last-active-2024` |
| [`pearc26-workshop-cursor`](https://github.com/gsbdarc/pearc26-workshop-cursor) | `status-active` |
| [`pearc26_tutorial_ai_agents`](https://github.com/gsbdarc/pearc26_tutorial_ai_agents) | `claude-code` `status-active` |
| [`reproducibility_HHT`](https://github.com/gsbdarc/reproducibility_HHT) | `status-inactive` `last-active-2024` |
| [`rf_bootcamp_2024`](https://github.com/gsbdarc/rf_bootcamp_2024) | `status-inactive` `last-active-2024` |
| [`rf_bootcamp_2025`](https://github.com/gsbdarc/rf_bootcamp_2025) | `status-inactive` `last-active-2025` |
| [`sf311`](https://github.com/gsbdarc/sf311) | `status-maintained` |
| [`sklearn-pipeline`](https://github.com/gsbdarc/sklearn-pipeline) | `status-inactive` `last-active-2023` |
| [`yens-onboarding-2025`](https://github.com/gsbdarc/yens-onboarding-2025) | `yens` `status-inactive` `last-active-2025` |
| [`yens-onboarding-2026`](https://github.com/gsbdarc/yens-onboarding-2026) | `yens` `slurm` `claude-code` `status-active` |

#### `internal-ops` — 13 repos

| Repo | Other topics |
|---|---|
| [`.github`](https://github.com/gsbdarc/.github) | `status-active` |
| [`claude-code-best-practices`](https://github.com/gsbdarc/claude-code-best-practices) | `claude-code` `status-active` |
| [`claude-skills-project-summary`](https://github.com/gsbdarc/claude-skills-project-summary) | `claude-code` `status-active` |
| [`darc-orchestrator`](https://github.com/gsbdarc/darc-orchestrator) | `claude-code` `status-active` |
| [`darc-staff-skills`](https://github.com/gsbdarc/darc-staff-skills) | `yens` `claude-code` `status-active` |
| [`github-slack-connector`](https://github.com/gsbdarc/github-slack-connector) | `status-active` |
| [`gsb-publications-explorer`](https://github.com/gsbdarc/gsb-publications-explorer) | `status-active` |
| [`promptops`](https://github.com/gsbdarc/promptops) | `llm` `status-inactive` `last-active-2024` |
| [`softball-lineup-maker`](https://github.com/gsbdarc/softball-lineup-maker) | `status-archived` `last-active-2026` |
| [`Structured_output_blog-test-`](https://github.com/gsbdarc/Structured_output_blog-test-) | `llm` `status-experimental` |
| [`test-agent`](https://github.com/gsbdarc/test-agent) | `status-archived` `last-active-2026` |
| [`tokenviz`](https://github.com/gsbdarc/tokenviz) | `llm` `status-active` |
| [`welcome-email`](https://github.com/gsbdarc/welcome-email) | `yens` `status-maintained` |

### What changes on apply

75 of 75 repos change: **265 topics added, 32 deleted.** Every deletion is an enumerated `remove:` term -- nothing else is touched.

| Deleted | Use instead | Repos | Why |
|---|---|---|---|
| `data-engineering` | `data-delivery` | 10 | could not tell a school-wide data asset from one PI's pipeline |
| `etl-pipeline` | `data-delivery` | 10 | redundant -- 13 of the 15 repos carrying it are already `data-delivery` |
| `sp-global` `comscore` `data-axle` `dun-and-bradstreet` `kpler` `pitchbook` `sensor-tower` `freightos` | — | 9 | the vendor belongs in the repo name; the facet reached only 9 of 15 data repos, so its absence meant nothing |
| `template` | — | 1 | GitHub has its own template-repo flag, shown as a badge on the repo |
| `javascript` | — | 1 | GitHub derives languages from file contents |
| `survey` | `qualtrics` | 1 | every repo carrying it is a Qualtrics instrument, already tagged |

Also in `remove:` but not currently on any repo, listed to block reintroduction: `data-etl`, `etl`.

<!-- END GENERATED -->

<!-- Reference: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics -->
