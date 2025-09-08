
# Archivists’ Debate — Planning & IA (Internal)

## 0) Purpose & Audience

* **Purpose:** Document and dramatize the Capital archivists' long-running argument about *how to file reality*—not just **Region** vs **Order**, but the deeper three-way psychological tension between **Clerkly** (procedural custodians), **Romantic** (narrativizing witnesses), and **Philosophical** (systematizing legislators) approaches to evidence. The debate reveals whether cataloging *mirrors* the world, *makes* it, or *preserves* it.
* **Audience:** In-world archivists (primary), public readers (secondary). Voice should feel like internal papers that leaked into a public-facing shelf, but each document must embody one of the three distinct temperamental approaches.
* **Outcome:** A navigable mini-site that (a) explains the shift to the Orders through competing temperamental lenses, (b) preserves dissent as psychological rather than merely methodological, and (c) cross-links back to archive slips showing how the same evidence speaks differently through different temperaments.

---

## 1) Page Skeleton & Roles

### `archivists-debate.html` — Hub / Table of Contents

**Sections** (anchored pills in-page):

* `#phase-1` **Phase I — Regional Drawers (Years 1–12)**
  Establishes the original filing-by-borough doctrine (Provenance First). **Temperamental balance:** Clerkly dominance, with occasional philosophical seeds. Romance barely appears. Documents embody procedural precision with hints of systematic ambition.
* `#phase-2` **Phase II — Faults in Geography (Years 13–20)**
  Field and colloquy materials showing geography alone can't hold contradictions (edges that move, copies without origin, authors that dissolve). **Temperamental balance:** All three temperaments emerge clearly for the first time. Phase II is the hinge where romantic voices find space, clerkly reports document failures, philosophical proposals begin.
* `#phase-3` **Phase III — Orders Proposal (Year 22)**
  The reform: six **Orders** (Boundary; Doubling; Craving; Silence & Withdrawal; Violence & Secret Life; Mediation & Aperture). **Temperamental balance:** Philosophical dominance with clerkly resistance. Romance largely absent—this is abstract systematizers vs. anxious custodians.
* `#phase-4` **Phase IV — Implementation & Objections (Year 23– )**
  Rollout docs: cross-index directives, hearings about catalog effects on testimony, edge-case rulings. **Temperamental balance:** All three temperaments collide, generating institutional self-consciousness about the Archive's world-shaping role.
* `#appendix` **Appendix — Selected Sources**
  Short annotated bibliography that anchors debate claims to world evidence (for readers and clerks).

**How the hub “does history”:**

* Chronological **Phases** = institutional timeline.
* Within each Phase, **document links** (memos, minutes, hearings) record the evolving stance.
* Cross-links to **slips** (A1–I1 etc.) show how filing choices change interpretation.

---

## 2) Link Map (What each hub item should point to)

For each bullet below, create a short HTML page (400–900 words) in `/debate/`. Use the file names shown (you can adjust slugs, but keep the overall pattern).

### Phase I — Regional Drawers (Clerkly dominance, philosophical seeds)

* **`/debate/phase1-memo-1-2.html`** — *Memo 1.2: Establishment of Borough Drawers* **(Philosophical)**
  Rationale: geography as least-falsifiable attribute; custody chain; drawer list; early codes. Early systematizing disguised as protocol.
* **`/debate/phase1-minute-3-7.html`** — *Minute 3.7: Provenance First* **(Clerkly)**
  Meeting notes that codify "Region → Form → Title" as the primary filing sequence. Pure procedural precision.
* **`/debate/phase1-circular-5-1.html`** — *Circular 5.1: Chain-of-Slips Protocol* **(Clerkly)**
  How slip custody works (stamps, initials, window rules). Mechanical focus on procedures. Seeds later fights about apertures.

### Phase II — Faults in Geography (All three temperaments emerge)

* **`/debate/phase2-field-edges-report.html`** — *Field Report: Dens Boundary vs Testimony* **(Clerkly)**
  Shows ditch meters vs oral accounts; the "edge" moves; geography misleads without a boundary Order tag. Mechanical documentation of contradictions.
* **`/debate/phase2-colloquy-fivefold.html`** — *Colloquy Note: Fivefold Silhouette Copies* **(Philosophical)**
  Authenticity problem framed as **Doubling**, not place; provenance is noisy, recurrence is crisp. Systematic reframing of evidence.
* **`/debate/phase2-case-pickbox.html`** — *Case Note: The Pickbox & Authorless Burden* **(Romantic)**
  Cart testimony refuses authorship. Suggests **Mediation & Aperture** as primary class. Narrative attention to witness voices and mysterious objects.
* **`/debate/phase2-colloquy-withdrawal.html`** — *Colloquy Note: On Withdrawal as Filing Principle* **(Romantic)**
  Minor archivist narrativizes silence practices; argues gaps are evidence. Testimonial approach to non-speech methods.

### Phase III — Orders Proposal (Philosophical dominance vs. clerkly resistance)

* **`/debate/phase3-memo-orders.html`** — *Memorandum: Toward a Unified Scheme of Archival Ordering* (Varro) **(Philosophical)**
  Defines six Orders; proposes Orders-first filing; Regions = secondary tags. Systematic legislating of metaphysical categories.
* **`/debate/phase3-counter-memo-metaphysics-risk.html`** — *Counter-Memo: On the Danger of Metaphysics* (Kettel) **(Clerkly)**
  Argues labels *shape* witness speech; warns of catalog creating cases. Anxious procedural pushback against philosophical overreach.
* **`/debate/phase3-brief-crossindex.html`** — *Brief: Cross-Index Standards v1* **(Philosophical)**
  Introduces mandatory dual-tagging: **Order(s)** + **Region(s)**; minimum one cross-reference per slip. Technical systematization.
* **`/debate/phase3-counter-memo-provenance-stubbornness.html`** — *Counter-Memo: On the Stubbornness of "Provenance First"* (Varro) **(Philosophical)**
  Challenges Minute 3.7; argues geography has hardened into superstition. Philosophical irritation at clerkly caution.

### Phase IV — Implementation & Objections (Three-way collision)

* **`/debate/phase4-directive-orders-first.html`** — *Directive: Orders-First, Regions-Second* **(Philosophical)**
  Official policy; compliance date; retrofits to legacy drawers; exception path. Systematic implementation of the new order.
* **`/debate/phase4-memo-densmok-crossindex.html`** — *Memorandum: On the Necessity of Cross-Indexing Densmok* (Gravent) **(Philosophical)**
  Definitive directive on Densmok as "hinge" requiring multiple Order tags. Philosophical masterwork on cross-regional phenomena.
* **`/debate/phase4-counter-memo-overreach.html`** — *Counter-Memo: Against Overreach in Filing Densmok* (Keffel) **(Clerkly)**
  Response to Gravent; argues against mandatory cross-indexing for all slips. Clerkly resistance to systematic overreach.
* **`/debate/phase4-hearing-create-the-case.html`** — *Hearing: "Does the Catalog Create the Case?"* **(Romantic)**
  Testimony from Sticks clinics & North singers about label feedback into practice. Dramatic presentation of witness voices concerned about archival world-making.
* **`/debate/phase4-edge-cases-window.html`** — *Edge Case Ruling: Capital Aperture & Stair Throttle* **(Clerkly)**
  Window/stair architecture filed under **Mediation & Aperture**; explains why physical design is catalog-relevant. Legalistic ruling on procedural implementation.

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
* **Temperament:** Clerkly / Romantic / Philosophical (determines voice and approach)
* **Order Focus:** one or more of the six (if Phase I, can be "n/a")
* **Region(s):** if relevant to evidence
* **Date & Clerk Initials:** e.g., Year 22, Q1 — JV
* **Status Badge:** Draft / Adopted / Superseded

**Body sections (suggested):**

1. **Abstract (2–4 sentences)** — what question this doc addresses, written in the document's temperamental voice.
2. **Exhibits** — links to slips (A1–I1) and ore passages; include 1–2 quoted "clips" (use the Protocol 7.3 **How to Cite a Clip** aside pattern). **Commentary on clips must match temperament:** clerkly (mechanical preservation), romantic (testimonial weaving), philosophical (systematic organization).
3. **Argument** — 2–6 short paragraphs; **temperamental voice** (not generic administrative tone); show how filing choice affects meaning through the lens of the document's temperament.
4. **Disposition** — Adopted / Filed Without Action / Sent to Colloquy.
5. **Cross-Refs** — "See also: \[Phase II field report], \[Phase III counter-memo]."

**Clip protocol:** reuse the `<aside class="cite-sidebar">` ("How to Cite a Clip") or a compact variant. Every debate doc should include at least **one** fully formatted Clip with commentary that demonstrates the temperamental approach to the same evidence.

**Temperamental voice consistency:** Each document must maintain its temperamental voice throughout—clerkly documents use terse, procedural language; romantic documents use narrative, testimonial language; philosophical documents use abstract, systematic language.

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

## 8) Editorial Standards (Temperamental Voice + Evidence)

* **Voice:** Must embody one of three temperaments consistently:
  - **Clerkly:** Terse, procedural, exact. "Filed under Dens. Contradiction noted." Focus on stamps, protocols, custody chains.
  - **Romantic:** Narrative, testimonial, dramatic. "She swore the ditch had grown; when morning came, the town agreed." Focus on individual voices, stories, witnesses.
  - **Philosophical:** Abstract, systematic, legislative. "Evidence demonstrates Boundary Order through unstable geographical determination." Focus on categories, patterns, underlying principles.
* **Evidence discipline:** Each debate doc must include **at least two Clips** (excerpts) and list their **slip codes**. Commentary on clips must demonstrate the temperamental approach to evidence.
* **Contradictions:** never "resolve" contradictory witness cards; log them; contradictions are evidence. But temperaments handle contradictions differently: clerks preserve mechanically, romantics dramatize as narrative tension, philosophers systematize as dialectical pressure.
* **Temperamental authenticity:** Each document must feel like it was written by a specific type of archivist with distinct fears, hopes, and approaches to evidence—not just different policy positions.
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

* **Readers can answer:**

  1. *Why* the Orders superseded Regions (methodological evolution).
  2. *How* filing changes interpretation (the mirror vs. maker question).
  3. *Where* to find the canonical sources supporting an Order.
  4. **NEW:** *Who* the three types of archivists are and how they approach the same evidence differently (temperamental psychology).
  5. **NEW:** *When* each temperament dominated and why the balance shifted across phases (institutional evolution).

* **Internal:**

  * Every slip is cross-indexed to at least one debate doc.
  * Every debate doc cites ≥2 slips; Appendix entries point to both.
  * **NEW:** Each phase demonstrates the appropriate temperamental balance (Phase I clerkly-dominant, Phase II all three emerge, Phase III philosophical-dominant, Phase IV three-way collision).
  * **NEW:** Documents feel authentically written by distinct personality types, not just different policy positions.

---

## 12) Quick "Next Docs" Backlog (temperament-balanced expansion)

**Immediate priorities (ensure temperamental diversity):**

1. **Phase I — Memo 1.2** (Borough Drawers) **(Philosophical)**: origin policy; codes & seals. Early systematizing.
2. **Phase I — Minute 3.7** (Provenance First) **(Clerkly)**: pure procedural precision establishing regional filing.
3. **Phase II — Field Report: Dens Edges** **(Clerkly)**: meters vs mouths; mechanical documentation of boundary failures.
4. **Phase II — Colloquy Note: Withdrawal** **(Romantic)**: minor archivist narrativizing silence practices.
5. **Phase III — Varro's Orders Memo** **(Philosophical)**: six Orders; systematic legislation of metaphysical categories.
6. **Phase III — Counter-Memo: Metaphysics Risk** (Kettel) **(Clerkly)**: anxious pushback against philosophical overreach.
7. **Phase IV — Hearing: Create the Case?** **(Romantic)**: dramatic witness testimony about archival world-making.
8. **Phase IV — Counter-Memo: Overreach** (Keffel) **(Clerkly)**: resistance to mandatory cross-indexing.

**Goal:** Each phase should include all three temperamental voices, with appropriate balance reflecting the institutional evolution.
