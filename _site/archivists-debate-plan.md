
# Archivists’ Debate — Planning & IA (Internal)

## 0) Purpose & Audience

* **Purpose:** Document and dramatize the Capital archivists’ long-running argument about *how to file reality*: by **Region** (old system) vs by **Order** (metaphysical categories), and whether cataloging *mirrors* the world or *makes* it.
* **Audience:** In-world archivists (primary), public readers (secondary). Voice should feel like internal papers that leaked into a public-facing shelf.
* **Outcome:** A navigable mini-site that (a) explains the shift to the Orders, (b) preserves dissent, and (c) cross-links back to archive slips as living evidence.

---

## 1) Page Skeleton & Roles

### `archivists-debate.html` — Hub / Table of Contents

**Sections** (anchored pills in-page):

* `#phase-1` **Phase I — Regional Drawers (Years 1–12)**
  Establishes the original filing-by-borough doctrine (Provenance First).
* `#phase-2` **Phase II — Faults in Geography (Years 13–20)**
  Field and colloquy materials showing geography alone can’t hold contradictions (edges that move, copies without origin, authors that dissolve).
* `#phase-3` **Phase III — Orders Proposal (Year 22)**
  The reform: six **Orders** (Boundary; Doubling; Craving; Silence & Withdrawal; Violence & Secret Life; Mediation & Aperture). Includes the manifesto and responses.
* `#phase-4` **Phase IV — Implementation & Objections (Year 23– )**
  Rollout docs: cross-index directives, hearings about catalog effects on testimony, edge-case rulings.
* `#appendix` **Appendix — Selected Sources**
  Short annotated bibliography that anchors debate claims to world evidence (for readers and clerks).

**How the hub “does history”:**

* Chronological **Phases** = institutional timeline.
* Within each Phase, **document links** (memos, minutes, hearings) record the evolving stance.
* Cross-links to **slips** (A1–I1 etc.) show how filing choices change interpretation.

---

## 2) Link Map (What each hub item should point to)

For each bullet below, create a short HTML page (400–900 words) in `/debate/`. Use the file names shown (you can adjust slugs, but keep the overall pattern).

### Phase I — Regional Drawers

* **`/debate/phase1-memo-1-2.html`** — *Memo 1.2: Establishment of Borough Drawers*
  Rationale: geography as least-falsifiable attribute; custody chain; drawer list; early codes.
* **`/debate/phase1-minute-3-7.html`** — *Minute 3.7: Provenance First*
  Meeting notes that codify “Region → Form → Title” as the primary filing sequence.
* **`/debate/phase1-circular-5-1.html`** — *Circular 5.1: Chain-of-Slips Protocol*
  How slip custody works (stamps, initials, window rules). Seeds later fights about apertures.

### Phase II — Faults in Geography

* **`/debate/phase2-field-edges-report.html`** — *Field Report: Dens Boundary vs Testimony*
  Shows ditch meters vs oral accounts; the “edge” moves; geography misleads without a boundary Order tag.
* **`/debate/phase2-colloquy-fivefold.html`** — *Colloquy Note: Fivefold Silhouette Copies*
  Authenticity problem framed as **Doubling**, not place; provenance is noisy, recurrence is crisp.
* **`/debate/phase2-case-pickbox.html`** — *Case Note: The Pickbox & Authorless Burden*
  Cart testimony refuses authorship. Suggests **Mediation & Aperture** as primary class.

### Phase III — Orders Proposal

* **`/debate/phase3-memo-orders.html`** — *Memorandum: Toward a Unified Scheme of Archival Ordering* (Varro)
  Defines six Orders; proposes Orders-first filing; Regions = secondary tags.
* **`/debate/phase3-counter-memo-metaphysics-risk.html`** — *Counter-Memo: On the Danger of Metaphysics* (Kettel)
  Argues labels *shape* witness speech; warns of catalog creating cases.
* **`/debate/phase3-brief-crossindex.html`** — *Brief: Cross-Index Standards v1*
  Introduces mandatory dual-tagging: **Order(s)** + **Region(s)**; minimum one cross-reference per slip.

### Phase IV — Implementation & Objections

* **`/debate/phase4-directive-orders-first.html`** — *Directive: Orders-First, Regions-Second*
  Official policy; compliance date; retrofits to legacy drawers; exception path.
* **`/debate/phase4-hearing-create-the-case.html`** — *Hearing: “Does the Catalog Create the Case?”*
  Testimony from Sticks clinics & North singers about label feedback into practice.
* **`/debate/phase4-edge-cases-window.html`** — *Edge Case Ruling: Capital Aperture & Stair Throttle*
  Window/stair architecture filed under **Mediation & Aperture**; explains why physical design is catalog-relevant.

### Appendix — Selected Sources (Pointers, not essays)

* **`/debate/appendix-sources.html`** — one page with grouped bullets:

  * **Boundary** (Dens contradictions; ditch logs)
  * **Doubling** (Quarry journeys; fivefold impressions)
  * **Craving** (Densmok rigs; coder-singers)
  * **Silence & Withdrawal** (Sticks journals; Tower catechism)
  * **Violence & Secret Life** (North murder songs; counting-five)
  * **Mediation & Aperture** (Capital window; pickbox cart)

> Each Appendix bullet links outward to at least **two** live slips and **one** debate doc that cites them.

---

## 3) Content Spec for Each Debate Doc

**Header block (at top of each `/debate/*.html`):**

* Title (e.g., *Memo 1.2 — Establishment of Borough Drawers*)
* **Phase:** I / II / III / IV
* **Doc Type:** Memo / Minute / Field Report / Colloquy Note / Hearing / Directive / Brief / Ruling
* **Order Focus:** one or more of the six (if Phase I, can be “n/a”)
* **Region(s):** if relevant to evidence
* **Date & Clerk Initials:** e.g., Year 22, Q1 — JV
* **Status Badge:** Draft / Adopted / Superseded

**Body sections (suggested):**

1. **Abstract (2–4 sentences)** — what question this doc addresses.
2. **Exhibits** — links to slips (A1–I1) and ore passages; include 1–2 quoted “clips” (use the Protocol 7.3 **How to Cite a Clip** aside pattern).
3. **Argument** — 2–6 short paragraphs; administrative tone; show how filing choice affects meaning.
4. **Disposition** — Adopted / Filed Without Action / Sent to Colloquy.
5. **Cross-Refs** — “See also: \[Phase II field report], \[Phase III counter-memo].”

**Clip protocol:** reuse the `<aside class="cite-sidebar">` (“How to Cite a Clip”) or a compact variant. Every debate doc should include at least **one** fully formatted Clip.

---

## 4) Taxonomy & Cross-Index (The “Orders”)

Primary metaphysical **Orders** (top-level classes):

1. **Boundary** — unstable edges; town/wilderness; lines that move.
2. **Doubling** — replication; journeys spawning journeys; originals-without-origin.
3. **Craving** — desire as generative force; appetites that make artifacts.
4. **Silence & Withdrawal** — renunciation; non-speech methods; ritual cadence.
5. **Violence & Secret Life** — parallel ledgers of harm; murder songs; numerologies.
6. **Mediation & Aperture** — windows, devices, carts; constraints on access and authorship.

**Filing rule:** Orders-first (1–3 tags allowed) → **Form** (Memo/Minute/etc.) → **Region(s)** (secondary).
**Cross-index minimum:** Each debate doc must link to **≥2** slips and **≥1** doc in a *different* Phase.

---

## 5) Navigation & UI Conventions

* **Hub pills** jump to `#phase-*` anchors; each Phase lists 2–4 documents max (start small; grow later).
* **Debate docs** include breadcrumbs: `Archivists’ Window → Debate → Phase N`.
* **Callouts:** Use the same `.notice` / `.quickkit-pill` styles for internal consistency.
* **Badges:** Small inline badges for *Draft / Adopted / Superseded* (CSS classes: `.badge-draft`, `.badge-adopted`, `.badge-superseded`).
* **Tooling:** Optional `<details><summary>` for clerk marginalia (dissent, sarcasm, redactions).

---

## 6) File Naming & Slugs

* Hub: `archivists-debate.html`
* Debate docs: `/debate/phase{N}-{type}-{slug}.html`

  * Examples:

    * `phase1-memo-1-2.html`
    * `phase2-field-edges-report.html`
    * `phase3-counter-memo-metaphysics-risk.html`
    * `phase4-hearing-create-the-case.html`
* Appendix: `/debate/appendix-sources.html`

**Why:** consistent, human-readable URLs; easy to sort by Phase.

---

## 7) Cross-Link Policy (From Slips → Debate)

Each slip (e.g., `archivist-b1.html`) should add a tiny **footer line**:

> “Filed under **\[Order]**. See **Debate: Phase II — \[doc title]** for the filing rationale.”

* Keep it a single sentence; link both the **Order** anchor in `notebooks.html` **and** the relevant debate doc.
* This creates bidirectional flow: **evidence** → **policy** → **evidence**.

---

## 8) Editorial Standards (Voice + Evidence)

* **Voice:** calm, administrative, exact; let unease leak via *what is filed*, not purple prose.
* **Evidence discipline:** Each debate doc must include **at least two Clips** (excerpts) and list their **slip codes**.
* **Contradictions:** never “resolve” contradictory witness cards; log them; contradictions are evidence.
* **Footers:** Always include Disposition (what the committee did with the doc).

---

## 9) Rollout Plan (MVP → Full)

**MVP (ship now):**

* Hub (`archivists-debate.html`) with Phase sections.
* 1 doc per Phase (4 total) + Appendix page.
* Add one cross-link footer to 3–5 key slips.

**Phase 2:**

* Fill each Phase to 3 docs.
* Add “counter-memo” and a “hearing” to show dissent.

**Phase 3:**

* Add timeline rail (Year ticks) and status badges.
* Add index by **Doc Type** (Memo / Minute / Hearing) for internal users.

---

## 10) Reuse: “How to Cite a Clip” Aside

* Include the `<aside class="cite-sidebar">` once per debate doc (top or right after Provenance).
* For multi-clip docs, keep the aside once; then use the **Template** block to standardize excerpt formatting.
* Encourage clerks to use double bars `||` or `<blockquote>` for verbatim.

---

## 11) Success Criteria

* Readers can answer:

  1. *Why* the Orders superseded Regions.
  2. *How* filing changes interpretation.
  3. *Where* to find the canonical sources supporting an Order.

* Internal:

  * Every slip is cross-indexed to at least one debate doc.
  * Every debate doc cites ≥2 slips; Appendix entries point to both.

---

## 12) Quick “Next Docs” Backlog (suggested first 6 to write)

1. **Phase I — Memo 1.2** (Borough Drawers): origin policy; codes & seals.
2. **Phase II — Field Report: Dens Edges**: meters vs mouths; why *Boundary* beats Region.
3. **Phase III — Varro’s Orders Memo**: six Orders; Orders-first rule; sample re-shelving.
4. **Phase III — Counter-Memo**: risks of metaphysical labels (catalog ≈ world-maker).
5. **Phase IV — Directive: Orders-First**: adoption date; cross-index standard; exceptions.
6. **Phase IV — Hearing: Create the Case?**: witness testimony about labels feeding back.
