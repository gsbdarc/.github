# What this proposal would change

> **Nothing here has been applied.** This is the committed output of
> `./scripts/apply-topics.py` (dry run) against the org as it stands, so the
> whole impact is reviewable without running anything.
>
> Removals are **enumerated, not inferred** — only the six terms under `remove:`
> in `topics.yml` are ever deleted (13 deletions across 12 repos). Vendor tags
> and `etl-pipeline` are untouched. Absence from the manifest is not a delete
> signal.

```
validation passed: 75 repos, 30 vocabulary terms

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
    = etl-pipeline
    + data-delivery
    + status-active
    - data-engineering  -> data-delivery

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
    = etl-pipeline
    + data-delivery
    + status-active
    - data-engineering  -> data-delivery

data-etl-template
    = etl-pipeline
    + data-delivery
    + status-maintained
    - data-engineering  -> data-delivery
    - template  -> repo-template

dnb-establishment-data-ETL
    = dun-and-bradstreet
    = etl-pipeline
    + data-delivery
    + status-active
    - data-engineering  -> data-delivery

edgar-yens-mirror
    + data-delivery
    + etl-pipeline
    + status-active
    + yens

gcp-scraping-terraform
    + data-delivery
    + etl-pipeline
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
    + etl-pipeline
    + faculty-project
    + llm
    + research-support
    + status-active

kpler-maritime-gcp-ETL
    = etl-pipeline
    = google-cloud
    = kpler
    = terraform
    + data-delivery
    + status-active
    - data-engineering  -> data-delivery

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
    = qualtrics
    + app-build
    + status-active
    - javascript  (GitHub derives languages)
    - survey  -> survey-research

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
    = etl-pipeline
    = pitchbook
    + data-delivery
    + redivis
    + status-active
    - data-engineering  -> data-delivery

preqin-data-ETL
    + aws
    + data-delivery
    + etl-pipeline
    + status-active

promptops
    + internal-ops
    + last-active-2024
    + llm
    + status-inactive

pubsubgpt_pipeline
    + etl-pipeline
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
    = etl-pipeline
    = sensor-tower
    + aws
    + data-delivery
    + redivis
    + sherlock
    + slurm
    + status-active
    - data-engineering  -> data-delivery

sf311
    + status-maintained
    + training

shosh_freightos_pipeline
    = etl-pipeline
    = freightos
    + data-delivery
    + faculty-project
    + status-active
    - data-engineering  -> data-delivery

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
    = etl-pipeline
    = sp-global
    + data-delivery
    + status-active
    - data-engineering  -> data-delivery

sp-panjiva-ETL
    = etl-pipeline
    = sp-global
    + data-delivery
    + status-active
    - data-engineering  -> data-delivery

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

75 repos change, 0 unchanged. 13 topic(s) deleted, all from the enumerated remove: list.

Dry run -- nothing was written. Re-run with --apply to write.
```
