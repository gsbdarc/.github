# Understanding the taxonomy

How the topic scheme works and why it's shaped this way. This is the
explanation; [`repo-topics.md`](repo-topics.md) is the reference — the exact
terms and the topics proposed for each repo.

Deliberately no counts in this document. Numbers belong in the reference, where
they're generated from [`topics.yml`](topics.yml) and can't go stale.

## Why tag repos at all

We have around 75 repositories. Some are pipelines that run every week and page
someone when they break. Some are courses taught once in 2024 and frozen since.
Some are one PI's analysis. Some are prototypes that never went anywhere.

From the repo listing they look identical: a name, maybe a description, a
language, a date. So every "have we built one of these before?" question becomes
someone's memory, and the answer is usually "ask whoever's been here longest."
Topics turn those questions into queries.

## Why facets instead of categories

The instinct is to sort repos into categories — a folder-shaped scheme where
each repo goes in one bucket. That breaks immediately, because our repos are
several things at once.

Take `monin-video-rating-survey`. Is it a *faculty project* or a *Qualtrics
app*? It's both, unavoidably. A single-bucket scheme forces you to pick, and
whichever you pick, the other question becomes unanswerable — file it under
faculty work and "show me every app we've built" silently omits it.

A **facet** is one independent question you can ask about a repo. Instead of one
label, each repo carries an answer to each facet:

```
monin-video-rating-survey
    app-build          <- what kind of work is this?
    faculty-project    <- who is it for?
    qualtrics          <- what does it run on?
    status-active      <- is it alive?
```

Nothing is forced to choose, and the questions compose. Because the facets are
independent, you get answers nobody had to anticipate:

```
topic:app-build topic:faculty-project        every app we've built for a PI
topic:training topic:yens                    Yens teaching material
topic:qualtrics topic:status-active          live Qualtrics work
topic:research-computing -topic:status-active   cluster work nobody is maintaining
```

That last one is the point. No category scheme has a "cluster work nobody is
maintaining" bucket, because nobody thought to make one. Facets answer it anyway.

## The four facets

### 1. Work type — *what kind of work is this?*

**Exactly one, required.** The primary axis: why DARC has this repo at all.

Two rules settle almost every hard case.

**Who is it for?** This is the line between `data-delivery` and
`research-support`: many researchers, or one question. `pitchbook-feed-ETL`
licenses a dataset the whole school can use. `jungho_state-regulations` builds a
corpus for one paper. Both are data pipelines; they are not the same kind of
work.

**Purpose, not implementation.** `slurm-viz` is, technically, a web dashboard.
But it exists to make the cluster legible, so it's `research-computing`, not
`app-build`. Ask what the repo is *for*, not what it's *made of* — the stack
facet already records what it's made of.

### 2. Client — *who is it for?*

**Optional.** One term: `faculty-project`.

This exists as its own facet rather than a work-type value, and that's the most
important structural decision in the scheme. A faculty engagement can be data
work, an app build, or an analysis. If `faculty-project` were a work type, every
faculty repo would be filed there *instead of* under what it actually is — and
"show me every app we've built" would quietly return the wrong answer.

Keeping it separate means faculty work is findable both ways, and you can ask
for the intersection.

### 3. Stack — *what does it run on?*

**Optional, any number.** Where it runs, what it's built with.

One rule: **a term must be earned by at least two repos.** A tag that applies to
exactly one repo isn't a category, it's a note — and a note belongs in the
description, where it can be a sentence instead of a word. Single-use terms are
how a vocabulary quietly grows to a hundred entries nobody can remember.

### 4. Lifecycle — *is this alive?*

**Exactly one, required.** Plus a `last-active-YYYY` year tag when a repo has
stopped.

The year tag has one property worth understanding, because it's the reason this
facet is maintainable: **the year is frozen at the moment a repo goes inactive,
and never updated again.** Active repos carry no year at all.

The alternative — tagging every repo with the year it was last touched — would
need a re-tagging sweep across the whole org every January. That sweep would get
skipped, and then the labels would be quietly wrong, which is worse than having
no labels. A scheme that needs periodic maintenance to stay true is a scheme
that will eventually lie to you.

`status-inactive` is also not a judgment. An annual course repo is *supposed* to
be a frozen snapshot of the year it was taught. Tagging `intro_to_yens_2024` as
inactive with `last-active-2024` states that plainly, instead of leaving it
looking abandoned.

## Tagging a new repo

Three questions, about thirty seconds:

```
1. What kind of work is this?      -> exactly one work type
2. Is it for a named PI?           -> add faculty-project
3. Is it alive?                    -> exactly one status-*
                                      (+ last-active-YYYY if not)

then, optionally:
4. Does it run on something others might search for?  -> stack terms
```

And one thing *not* to do: **don't tag the vendor.** If the repo is about a
specific dataset, the vendor's name goes in the **repo name** — see
[`CONTRIBUTING.md`](../CONTRIBUTING.md). Name search already finds it.

## What earns a facet — and what doesn't

Two tests. A candidate facet has to pass both.

**1. Is it derivable from something you already have?** If so, tagging it is
duplicate bookkeeping that goes stale.

**2. Can you apply it to its entire population?** If it will only ever cover
part of the repos it's about, absence stops meaning anything — and a facet whose
absence is ambiguous is worse than no facet, because it looks authoritative
while being unreliable.

Three candidates were rejected, and each fails a different way. They're worth
reading as case studies, because they're the shape of most bad tags.

### Programming languages — fails test 1

GitHub derives the language from file contents. `language:Python` already returns
every Python repo in the org, and the org listing has a native Language filter.
A `python` topic would restate that, and would be wrong the moment a repo's
composition shifted.

### Vendors and data sources — fails both

The vendor is already in the repo name for almost every repo that has one, so
`q=pitchbook in:name` works today — that's test 1.

But the decisive failure was test 2. The vendor tags that existed reached only
*some* of the data repos; several with obvious vendors never got tagged. So you
could not tell "this dataset isn't Preqin" from "nobody got round to tagging
it." Rather than complete the facet to a term per vendor, the existing tags were
removed and the naming convention made load-bearing instead.

There is exactly one repo where the source is genuinely invisible in the name.
One repo is a description fix, not a facet.

### `etl-pipeline` — fails test 1

Nearly every repo it would cover is already `data-delivery`, so for almost all of
them it restates the work type. A handful of exceptions are real, but they don't
earn a term applied across that many repos.

This was the closest call in the scheme and it's logged as an open question in
the reference, with the one-line path to reinstating it. If "which pipelines do
we operate?" turns out to be a question people ask often, that's the evidence to
bring back.

## How the scheme is kept honest

A taxonomy is only as good as the thing stopping it from drifting. Ours drifted
within months of the first tag — `etl`, `data-etl` and `etl-pipeline` all meant
one thing — so the scheme ships with checks rather than good intentions.

All of these run via `scripts/apply-topics.py --check`:

- **The vocabulary is closed.** A term used in `topics.yml` but not documented in
  the reference is an error, and so is a documented term nothing uses. The doc
  and the data cannot describe different schemes.
- **Every live topic is accounted for.** Any topic present on a repo must be
  either in the vocabulary or explicitly listed for removal. Nothing sits in
  limbo — this is the check that surfaced the stale vendor tags.
- **A replacement must exist.** If a removed term says "use X instead", X has to
  be a real term. Otherwise the doc sends people to something undefined.
- **Per-repo invariants.** Exactly one work type, exactly one status, a year tag
  if and only if inactive or archived, and no repo over GitHub's 20-topic limit.
- **The reference's tables are generated.** Every count comes from `topics.yml`
  via `--render`, and `--check` fails if they're out of date. Hand-typed counts
  went stale five separate times before this existed.
- **Removals are enumerated, never inferred.** Only terms on an explicit list are
  deleted. A tag someone adds in the GitHub UI is never silently reverted — it
  gets surfaced by the totality check so someone can decide about it.

## Extending it

Adding a term is a pull request that touches both the vocabulary in `topics.yml`
and the reference doc — the closure check enforces that, so they can't diverge.
Then `--render` and commit.

Before proposing one, run it through the two tests above. In practice the useful
question is: **what query do I want to run that I can't run today?** If there
isn't one, the term is decoration.
