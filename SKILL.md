---
name: local-lead-intelligence
description: Find and qualify local-business website opportunities responsibly. Use when the user wants to research businesses in a city or niche, identify public website and conversion gaps, prioritize prospects, prepare evidence-based mini-audits, recommend a website offer, draft personalized outreach for approval, or organize a website-sales pipeline. Never bulk-scrape Google Maps, store Maps content outside an allowed session, make unverified security claims, or send outreach without explicit approval.
---

# Local Lead Intelligence

Turn public, permission-respecting research into a short list of credible website-sales opportunities. Optimize for evidence, relevance and useful outreach, not volume.

## Operating principles

1. **Research one focused market at a time.** Start with niche, city, ideal customer and offer.
2. **Use permitted sources.** Prefer official business websites, public social profiles and user-provided lists. Google Maps may be used for interactive, session-based discovery or through an authorized Places API, respecting its terms, attribution and storage rules. Do not scrape, bulk-export, build a database from, or retain Maps business content beyond permitted use.
3. **Treat every signal as a hypothesis until verified.** A missing, broken or weak web presence must be supported by a public URL, a timestamp and a clear observation.
4. **No harmful labeling.** Do not call a business “insecure,” “bad,” “fake,” or “without a website” unless the evidence supports that exact claim. Say what was observed instead.
5. **No automatic outreach.** Prepare drafts only. The user reviews the evidence and explicitly approves every send.
6. **Respect privacy and contact preferences.** Use business contact channels that are publicly presented for commercial contact. Never infer private addresses or phone numbers, evade blocks, or repeatedly contact a business.
7. **Keep the report useful.** Ten well-supported prospects beat a hundred unverified rows.

## Intake

Gather or infer these parameters. If missing, use a clear assumption and let the user correct it:

- **Market:** business category or service
- **Location:** city, neighborhood or radius
- **Offer:** landing page, institutional website, booking website, catalogue, menu, redesign, or maintenance
- **Ideal profile:** service value, customer type, size indicators, language
- **Batch size:** default 10 verified prospects
- **Research sources:** user-provided list, official sites, public search, permitted Maps session/API

Default starter profile for a web freelancer: local businesses with high-value services, an active offline or social presence, and an obvious public website/conversion gap.

## Workflow

### 1. Define the search brief
Write a one-line search brief in this format:

> Find up to {batch size} {market} businesses in {location} that have a verifiable web-presence or conversion opportunity for a {offer}.

State exclusions, such as franchises, large chains, businesses already using a polished booking platform, or businesses with no public business contact channel.

### 2. Discover candidates
Use specific queries and rotate terms rather than collecting a bulk list. For each candidate, capture only the minimum needed to evaluate:

- Business name
- Public business URL or source URL
- Website URL, if publicly linked
- Public business contact channel, if relevant
- Discovery date

If a Maps result is used, treat it as a live discovery aid. Avoid copying Maps names, addresses, reviews, ratings or other content into a durable lead database unless the user has an authorized workflow that permits it.

### 3. Verify the public web presence
Open the company website independently when it exists. Check the following, and label each as **verified**, **not observed**, or **not tested**:

| Area | Verify | Evidence standard |
|---|---|---|
| Website availability | Homepage loads, redirects or errors | URL and observed result |
| HTTPS | Browser accesses `https://` without certificate warning | URL and timestamp |
| Mobile experience | Layout, navigation, readable text and tap targets at a mobile viewport | Screenshot/note of specific issue |
| Conversion path | Phone, WhatsApp, form, booking or primary CTA is easy to find | Describe its placement or absence |
| Offer clarity | What the business sells, where and for whom is understandable | Quote/paraphrase page section |
| Trust signals | Address, service area, reviews embedded by owner, portfolio, team or policies | Specific observed signal |
| Basic technical quality | Broken navigation, visible errors, blank sections, outdated copyright only if visible | URL and exact observation |

Do not claim malware, a data breach, legal non-compliance, poor SEO ranking or slow performance unless a suitable test was actually run and its outcome is reported. The absence of HTTPS is a technical observation, not proof that a business is broadly “unsafe.”

### 4. Identify a practical opportunity
Convert observations into a concrete, respectful offer. Examples:

- **No independently reachable website:** propose a focused landing page with services, proof and WhatsApp/contact action.
- **Social-only public presence:** propose an owned website that centralizes services, location, FAQ and lead capture.
- **Unclear service or weak CTA:** propose a conversion-focused redesign or single campaign page.
- **Mobile navigation/contact friction:** propose mobile-first improvement with click-to-call/WhatsApp and a simpler path.
- **No booking/menu/catalogue:** propose the smallest useful feature, not an oversized rebuild.

Never recommend a full redesign when a small fix would solve the observed problem.

### 5. Score transparently
Use the score as a prioritization aid, not as a fact about the business.

| Factor | Points | What earns it |
|---|---:|---|
| Clear public web gap | 0–30 | No reachable site, broken site or social-only presence, verified |
| Mobile/conversion friction | 0–20 | Specific public issue that hinders contacting or understanding the offer |
| Offer fit | 0–15 | A website solution matches the business model |
| Visible business activity | 0–15 | Recent public updates, clear service operation or other current signal |
| Impact potential | 0–10 | High-intent local service, booking, quote or catalogue benefit |
| Contact suitability | 0–10 | Public business contact channel and respectful outreach fit |

**Priority:** 70–100 high, 45–69 medium, under 45 low. Include the score breakdown in every report.

### 6. Prepare a lead brief
Use `templates/lead-brief.md`. Each lead must contain:

- verified observations and source URLs
- date checked
- opportunity statement
- recommended small-scope solution
- score and breakdown
- one respectful outreach draft
- uncertainty or follow-up needed

### 7. Draft outreach, never send it
Use `templates/outreach-draft.md`. The message must:

- mention one real, useful observation
- avoid insults, pressure or fear language
- avoid false promises about revenue, ranking or security
- offer a low-friction next step such as a free 2-minute review or homepage concept
- let the recipient decline or ignore without pressure
- be short enough for the selected channel

Ask for explicit approval before sending a message, and send only the version approved for that specific recipient.

### 8. Produce a concise batch report
Use `templates/batch-report.md`. Deliver:

1. top prospects ordered by score
2. evidence links and observations
3. suggested website offer per prospect
4. outreach drafts for the best prospects
5. what needs manual verification
6. suggested next action: review, create demo, approve outreach, or prepare proposal

## Quality gate

Before presenting a lead as ready:

- [ ] The prospect matches the niche and location.
- [ ] Every important claim has a public source URL and check date.
- [ ] “No website” was checked independently, not inferred from one listing.
- [ ] “No HTTPS” was verified on the actual website.
- [ ] Website recommendations match a visible opportunity.
- [ ] Score factors are shown, not hidden.
- [ ] Outreach is a draft, not a sent message.
- [ ] The wording is respectful and non-deceptive.

## Output rules

- Use a compact table for a batch of prospects.
- Link to sources; distinguish observations from recommendations.
- Say “not verified” when evidence is insufficient.
- Do not expose private data or publish lead lists.
- Do not claim compliance with Google terms for a workflow you did not verify.

## References

Read these when needed:

- `references/google-maps-and-data-use.md`
- `references/website-audit-rubric.md`
- `templates/lead-brief.md`
- `templates/outreach-draft.md`
- `templates/batch-report.md`
