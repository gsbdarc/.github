# What this proposal would change

> **Nothing here has been applied.** This is the committed output of
> `./scripts/apply-topics.py` (dry run) against the org as it stands, so the
> whole impact is reviewable without running anything.
>
> The proposal is **strictly additive** — no repo loses a topic. Deprecated
> spellings still present (`data-engineering`, `survey`, `template`,
> `javascript`) are marked `(deprecated, kept)` and left in place.

```
validation passed: 75 repos, 29 vocabulary terms

.github
    + internal-ops
    + status-active

bay-area-smoke
    + status-maintained
    + training

behavior-lab-chatbot
    + app-build
    + faculty-project
    + llm
    + qualtrics
    + status-active
    + terraform

City_council_meeting_parser
    + faculty-project
    + llm
    + research-support
    + status-active

claude-code-best-practices
    + claude-code
    + internal-ops
    + status-active

claude-code-sandbox
    + claude-code
    + docker
    + research-computing
    + status-experimental

claude-skill-github-for-research
    + claude-code
    + status-active
    + training

claude-skills-project-summary
    + claude-code
    + internal-ops
    + status-active

comscore-data-ETL
    = comscore
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    + data-delivery
    + status-active

darc-orchestrator
    + claude-code
    + internal-ops
    + status-active

darc-staff-skills
    + claude-code
    + internal-ops
    + status-active
    + yens

data-axle-reference-usa-ETL
    = data-axle
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    + data-delivery
    + status-active

data-etl-template
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    = template  (deprecated, kept)
    + data-delivery
    + status-maintained

dnb-establishment-data-ETL
    = data-engineering  (deprecated, kept)
    = dun-and-bradstreet
    = etl-pipeline
    + data-delivery
    + status-active

edgar-yens-mirror
    + data-delivery
    + status-active
    + yens

gcp-scraping-terraform
    + data-delivery
    + google-cloud
    + last-active-2025
    + status-inactive
    + terraform
    + web-scraping

gelfand_scientific-disciplines-datasets
    = faculty-project
    + research-support
    + status-active

github-slack-connector
    + internal-ops
    + status-active

green-patents
    + faculty-project
    + last-active-2024
    + research-support
    + status-inactive

gsb-publications-explorer
    + internal-ops
    + status-active

gsb-qualtrics-ai-chatbot
    + app-build
    + google-cloud
    + llm
    + qualtrics
    + status-maintained
    + terraform

gsb-research-computing-ai-skills
    + claude-code
    + gpu
    + slurm
    + status-active
    + training
    + yens

gsb-yen
    + research-computing
    + status-active
    + yens

hackingresources
    + data-delivery
    + status-experimental
    + web-scraping

HHT_titantic
    + status-maintained
    + training

image_ai_HHT
    + last-active-2024
    + status-inactive
    + training

intermediate_yens_2024
    + last-active-2024
    + status-inactive
    + training
    + yens

intro_to_yens_2024
    + last-active-2024
    + status-inactive
    + training
    + yens

jungho_state-regulations
    + faculty-project
    + llm
    + research-support
    + status-active

kpler-maritime-gcp-ETL
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    = google-cloud
    = kpler
    = terraform
    + data-delivery
    + status-active

LLM_benchmarks
    + llm
    + research-computing
    + status-active

llm_inference
    + gpu
    + last-active-2024
    + llm
    + research-computing
    + status-inactive
    + yens

LLM_YEN_BENCHMARK
    + gpu
    + llm
    + research-computing
    + status-active
    + yens

monin-video-aws-delivery
    = aws
    = faculty-project
    = qualtrics
    = terraform
    + app-build
    + status-active

monin-video-rating-survey
    = faculty-project
    = javascript  (deprecated, kept)
    = qualtrics
    = survey  (deprecated, kept)
    + app-build
    + status-active

multi-fixmask
    + research-computing
    + status-maintained
    + yens

ollama_helper
    + gpu
    + last-active-2025
    + llm
    + research-computing
    + sherlock
    + status-inactive
    + yens

paperrag
    + llm
    + research-support
    + status-experimental

pearc26-workshop-cursor
    + status-active
    + training

pearc26_tutorial_ai_agents
    + claude-code
    + status-active
    + training

pitchbook-feed-ETL
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    = pitchbook
    + data-delivery
    + redivis
    + status-active

preqin-data-ETL
    + aws
    + data-delivery
    + status-active

promptops
    + internal-ops
    + last-active-2024
    + llm
    + status-inactive

pubsubgpt_pipeline
    + google-cloud
    + last-active-2024
    + llm
    + research-computing
    + status-inactive

Qlora_code
    + last-active-2024
    + llm
    + research-computing
    + status-archived
    + yens

qualtrics-proxy
    + app-build
    + qualtrics
    + status-experimental

rcpedia
    + research-computing
    + status-active
    + yens

recombinant-search
    + faculty-project
    + last-active-2025
    + research-support
    + status-inactive

reproducibility_HHT
    + last-active-2024
    + status-inactive
    + training

rf_bootcamp_2024
    + last-active-2024
    + status-inactive
    + training

rf_bootcamp_2025
    + last-active-2025
    + status-inactive
    + training

sam-and-guy-ad-transparency-center
    + faculty-project
    + last-active-2023
    + research-support
    + status-inactive
    + web-scraping

saml-fullstack-stanford
    + app-build
    + aws
    + google-cloud
    + status-active
    + terraform

Saumitra-FrenchOCR-Lemay
    + faculty-project
    + llm
    + research-support
    + status-maintained

sensor-tower-data-etl
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    = sensor-tower
    + aws
    + data-delivery
    + redivis
    + sherlock
    + slurm
    + status-active

sf311
    + status-maintained
    + training

shosh_freightos_pipeline
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    = freightos
    + data-delivery
    + faculty-project
    + status-active

sklearn-pipeline
    + last-active-2023
    + status-inactive
    + training

slurm-viz
    + research-computing
    + slurm
    + status-active
    + yens

softball-lineup-maker
    + internal-ops
    + last-active-2026
    + status-archived

sp-451-research-datacenters-ETL
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    = sp-global
    + data-delivery
    + status-active

sp-panjiva-ETL
    = data-engineering  (deprecated, kept)
    = etl-pipeline
    = sp-global
    + data-delivery
    + status-active

Structured_output_blog-test-
    + internal-ops
    + llm
    + status-experimental

test-agent
    + internal-ops
    + last-active-2026
    + status-archived

tokenviz
    + internal-ops
    + llm
    + status-active

Vast_Scripts
    + research-computing
    + status-experimental
    + yens

vllm_helper
    + gpu
    + llm
    + research-computing
    + sherlock
    + status-maintained
    + yens

welcome-email
    + internal-ops
    + status-maintained
    + yens

wjnkim-llm-study
    + app-build
    + docker
    + faculty-project
    + google-cloud
    + llm
    + status-active

wos-starter-api-app
    + data-delivery
    + status-maintained

yen_cluster_skills
    + claude-code
    + research-computing
    + slurm
    + status-active
    + yens

yenbox
    + claude-code
    + docker
    + research-computing
    + status-experimental
    + yens

yens-gpu-demo
    + gpu
    + last-active-2023
    + research-computing
    + status-inactive
    + yens

yens-onboarding-2025
    + last-active-2025
    + status-inactive
    + training
    + yens

yens-onboarding-2026
    + claude-code
    + slurm
    + status-active
    + training
    + yens

75 repos would gain topics, 0 unchanged. No topic is ever removed.

Dry run -- nothing was written. Re-run with --apply to write.
```
