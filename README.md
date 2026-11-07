# Local Lead Intelligence

> **Turn focused local research into credible website sales opportunities.**
>
> Evidence-first prospecting for web freelancers and small agencies using Codex.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827?style=flat-square)](#quick-start)
[![License: MIT](https://img.shields.io/badge/License-MIT-16a34a?style=flat-square)](LICENSE)
[![Workflow](https://img.shields.io/badge/Workflow-human--reviewed-2563eb?style=flat-square)](#the-workflow)

## The problem

Most local-business lead lists are a dead end: they are huge, generic, full of duplicates and give you no good reason to start a conversation.

**Local Lead Intelligence** helps you find fewer prospects, but better ones. It researches a focused local market, checks public web presence, identifies a specific opportunity, scores the fit, recommends the smallest useful website offer and drafts a respectful message for your review.

It does **not** scrape Google Maps or blast automated outreach. It gives you evidence and a professional starting point for selling websites.

## What you get

| Output | Why it helps you sell |
|---|---|
| **Shortlist of verified prospects** | Spend time on businesses that fit your offer. |
| **Evidence-based mini-audit** | Start with a real observation, not “your website is bad.” |
| **Transparent opportunity score** | Know which business to approach first and why. |
| **Right-sized website offer** | Sell a landing page, booking flow or redesign that matches the visible need. |
| **Personalized outreach draft** | Start a useful conversation without sounding like spam. |
| **Simple pipeline status** | Track research, approval, contact, proposal and close. |

## The workflow

```text
Focused market → Discover → Verify → De-duplicate → Audit → Score → Offer → Draft → Your approval → Send
```

### 1. Focus the search
Choose one niche, one location and one clear offer.

> Example: Find up to 10 independent dental clinics in Bacabal, MA that could benefit from a mobile-first website with a WhatsApp appointment button.

### 2. Verify before you judge
The skill checks official public sources and labels each finding as **verified**, **not observed** or **not tested**. It does not turn guesses into “facts.”

### 3. Find an opportunity worth discussing
It looks for practical signals such as:

- no independently reachable official website after a limited check
- a social-only public presence
- contact, WhatsApp, booking or quote action hard to find
- a specific mobile navigation or readability issue
- unclear services, location or customer path
- visible broken pages or errors
- HTTPS observations, only when directly checked

### 4. Prioritize transparently

| Factor | Points | Meaning |
|---|---:|---|
| Clear public web gap | 0–30 | A verifiable reason to improve the presence |
| Mobile or conversion friction | 0–20 | A specific obstacle for a visitor |
| Offer fit | 0–15 | A website solution matches the business model |
| Visible business activity | 0–15 | Current public sign that the business is operating |
| Impact potential | 0–10 | Booking, quote, catalogue or local-service upside |
| Contact suitability | 0–10 | A public, appropriate business contact channel |
| **Total** | **0–100** | High: 70–100 · Medium: 45–69 · Low: below 45 |

### 5. Draft, then you decide
Every message is a draft. The skill never sends messages or follow-ups unless you explicitly approve the exact action for the exact recipient.

## Quick start

Copy this folder into your Codex skills directory and use a focused prompt like this:

```text
Use local-lead-intelligence to find up to 10 independent dental clinics in Bacabal, MA.
I sell mobile-first institutional sites with WhatsApp appointment buttons.
Avoid large chains. Verify official websites independently, de-duplicate the results,
score the opportunities, and write outreach drafts only for the top 5.
Do not send any messages.
```

## What makes it different

### Built for evidence, not volume
A Maps result can help discover a business, but it is not treated as a durable lead record. Before a prospect is saved in a report, the skill independently verifies it through an official public website, public social profile, user-provided list or another permitted source.

### Built for good sales conversations
The goal is not to insult somebody’s current website. The goal is to identify one useful improvement and connect it to a clear offer.

> Instead of: “Your site is outdated.”  
> Use: “I checked the homepage today and could not find a clear WhatsApp action on mobile. A simpler contact path could make it easier for a new visitor to ask for a quote.”

### Built with responsible limits
- Default batch is **10** prospects; it will not go above **20** without your instruction.
- It de-duplicates businesses before scoring.
- It does not scrape, bulk-export or build a database from Google Maps content.
- It does not bypass logins, CAPTCHAs, access blocks or private account areas.
- It does not make claims about security, SEO, compliance or performance without a suitable test and evidence.
- It respects public contact channels, opt-outs and user approval before outreach.

## Included templates

| File | Purpose |
|---|---|
| [`templates/lead-brief.md`](templates/lead-brief.md) | One verified prospect: evidence, score, offer and outreach draft. |
| [`templates/batch-report.md`](templates/batch-report.md) | Ranked, concise report for a local market. |
| [`templates/outreach-draft.md`](templates/outreach-draft.md) | Respectful WhatsApp, email or Instagram starting points. |
| [`references/website-audit-rubric.md`](references/website-audit-rubric.md) | Practical checklist for public website observations. |
| [`references/google-maps-and-data-use.md`](references/google-maps-and-data-use.md) | Responsible Maps and business-data guidance. |

## Example outcome

| Prospect | Verified observation | Website offer | Priority |
|---|---|---|---:|
| Example clinic | Contact action is difficult to find on the mobile homepage | Mobile-first service page with WhatsApp appointment CTA | 78/100 |

The report includes the source URL, check date and score breakdown. If the claim cannot be verified, it is marked as unverified or excluded.

## Who it is for

- Freelance web designers and developers
- Local website agencies
- Codex users building a more repeatable sales process
- Professionals who want to research before making a cold approach

## Responsible Google Maps use

Google Maps can support interactive, session-based discovery. Its terms restrict scraping, bulk export, storage and reuse of Maps content. This skill does not replace the applicable Google terms or an authorized API workflow.

Read [Google Maps and data use](references/google-maps-and-data-use.md) before building a production integration.

## Validation

The included validator checks the required files, skill metadata and essential safety rules:

```bash
python3 scripts/validate_skill.py
```

## Contributing

Ideas, issues and improvements are welcome. Useful contributions include better audit rubrics, localized outreach examples, clearer documentation and more reliable verification checks.

## License

Released under the [MIT License](LICENSE).
