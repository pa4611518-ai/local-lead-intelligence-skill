# Local Lead Intelligence

> Find fewer local-business prospects, but find the right ones: public evidence, practical website opportunities and respectful outreach drafts.

`Local Lead Intelligence` is a Codex skill for web freelancers and small agencies. It helps transform focused market research into a short, prioritized pipeline of local businesses that may benefit from a website, landing page or conversion improvement.

It is not a scraping tool or an auto-messaging bot. It uses small, human-reviewed batches and only saves a lead after it has been independently verified from a permitted public source.

## What it does

1. Defines a target market: niche, city, ideal client and offer.
2. Researches focused candidates through permitted, public sources.
3. Independently checks each public website before making claims.
4. Identifies concrete website and conversion opportunities.
5. Scores opportunities transparently.
6. Recommends the smallest useful website solution.
7. Produces lead briefs, reports and personalized outreach **drafts**.
8. Keeps sending under human approval.

## Why it is useful

Generic lead lists are usually noisy. This skill makes the sales conversation more credible because every lead includes:

- a source link
- a date checked
- a neutral observation
- a specific opportunity
- a suitable solution
- a visible score breakdown
- a message based on a real observation

## Example prompt

```text
Use Local Lead Intelligence to find up to 10 dental clinics in Bacabal, MA.
I sell mobile-first institutional sites with WhatsApp appointment buttons.
Avoid large chains. Check official websites independently, score the leads,
and create outreach drafts only for the top 5. Do not send anything.
```

## Output example

| Business | Public observation | Suggested offer | Priority |
|---|---|---|---:|
| Example Clinic | Contact action is not visible on mobile homepage | Mobile-first page with services and WhatsApp CTA | 78/100 |

The observation must have an evidence URL and date. If it cannot be verified, it is marked as unverified rather than presented as fact.

## Responsible Google Maps use

Google Maps can help with interactive, session-based discovery, but its terms restrict scraping, bulk export, storage and reuse of Maps content. This skill:

- does not scrape Google Maps;
- does not build lead databases from Maps listings;
- recommends authorized API workflows when an integration is needed;
- uses official business websites as the basis for website-quality claims;
- encourages a small, manually reviewed batch instead of bulk extraction.

Read [Google Maps and data use](references/google-maps-and-data-use.md) before building a production workflow.

## Audit scope

The skill checks public signals such as:

- site availability and HTTPS
- mobile navigation, readability and tap targets
- clarity of services and location
- visible paths to contact, WhatsApp, booking or quote
- visible trust signals
- observed broken pages or content issues

It does **not** claim a site is broadly insecure, legally non-compliant, slow, badly ranked or commercially ineffective without an appropriate test and evidence.

## Sales workflow

```text
Focused market → Candidate → Verify → Score → Offer → Draft → Human approval → Send → Track
```

Use the included templates:

- `templates/lead-brief.md`
- `templates/batch-report.md`
- `templates/outreach-draft.md`

## Installation

Copy this folder into your Codex skills directory, then ask Codex to use `local-lead-intelligence` for a focused niche and city.

## Limits that protect the workflow

- Default batch: 10 prospects; the skill will not exceed 20 unless you explicitly request it.
- It de-duplicates businesses before scoring.
- It does not bypass logins, CAPTCHAs, access blocks or private account areas.
- It does not send or follow up with outreach without your separate approval for each action.

## License

Released under the [MIT License](LICENSE).
