# Graduate Student Workflow — Writing **Archive** Slips (Orders-first)

> You’re contributing **in-character** documents to the Capital Archive. Read the Archive **GRAD-STUDENT-CONTEXT** first for the historian’s overview and the Archive’s method; then use this step-by-step to produce your slip. Archive files by **Order (primary)**, with **Region (secondary)** as provenance  .

---

## 0) What belongs here (and tone)

* **This section is for slips**: primary documents compiled by Capital archivists, written **in character**, fragment-preserving, interpretive, and deliberately unresolved .
* Keep the Archive/Debate boundary straight: you may **cite** Debate for context, but you’re filing **Archive** evidence, not writing Debate minutes .
* Voice & house style: precise, clerkly-professional; preserve contradictions rather than reconciling them .

---

## 1) Choose your **source thread** (“ore”)

Pick one thread that the context file highlights (examples below). You’ll mine it for **verbatim clips**:

* **Capital/Apertures** (window tolerances; stairs as throttles) → Mediation & Aperture .
* **Dens / Densmok** (edge that won’t hold; plot device) → Boundary / Mediation & Aperture (often cross-tags) .
* **Yeller Quarry** (roads that bud; Hunt woodcuts) → Doubling .
* **North / Northo** (murder songs; pickbox cart) → Violence & Secret Life (cross Mediation & Aperture) .
* **Tower / Sticks** (catechism; quiet-hours) → Silence & Withdrawal .
* **Dead River** (map installs a town; carried flame) → Mediation & Aperture + Doubling .

> Rule of thumb: your **unit of truth is a clip** (verbatim or near-verbatim) that you bracket and comment, not a paraphrase. Protocol follows in Step 4.

---

## 2) Classify **Order first → Region second**

Use the Orders as working lenses to decide **what the slip *does***; Regions record **where** it came from:

* **Orders (primary):** Boundary; Doubling; Craving; Silence & Withdrawal; Violence & Secret Life; Mediation & Aperture .
* **Regions (secondary):** Capital; Dens/Densmok; Quarry; North/Northo; Tower/Sticks; Dead River; Capeast .

Why this order? Densworld shows **device before place**—maps make towns, windows make policy, carts make rooms—so we shelve by what a document **performs** (the Order) and only then mark provenance (the Region) .

---

## 3) Sketch your slip (3 sections, always in this order)

1. **Provenance** (Region · record form)
2. **Extract** (2–5 clips)
3. **Archivist’s Commentary** (1–3 sentences per clip set)

Keep conflicts intact; disagreement is **evidence** (it can even determine the Order, e.g., Boundary/Doubling) . Your commentary argues the **Order-first** reasoning, not just geography .

---

## 4) Cite clips by **Protocol 7.3** (required)

Use the Archive’s in-house protocol when you quote:

**How to cite a clip (Protocol 7.3)**

* **Slip Code** — local identifier (e.g., A1)
* **Provenance** — Region + record form (e.g., Capital · Licensing Notes)
* **Quotation Mark** — bracket excerpts with `|| … ||`
* **Cross-Order Tag** — primary Order (+ optional cross-tag)
* **Commentary Line** — 1–3 sentences on how the clip pressures the Orders .

**Template + mini example**

```
Slip: [CODE] — [TITLE]
Provenance: [REGION] · [FORM]
Clip: || [VERBATIM EXCERPT] ||
Order(s): [ORDER-1][; ORDER-2]
Commentary: [ARCHIVIST NOTE, 1–3 sentences]
```



---

## 5) File naming & front matter

**Filename pattern** (Order-primary):
`[order]-[region]-[descriptive-slug]-[code].md` (e.g., `mediation-capital-window-aperture-a1.md`) .

**Front matter** (use the Archive entry format + `layout: archive`):

```yaml
---
title: "Archive Post A1 — Capital: Window Aperture, South Arcade (caliper check log)"
order: "Mediation & Aperture"
region: "Capital"
catalog_code: "A1"
excerpt: "This window is not a door. The rule is design: knowledge may pass; bodies may not."
layout: archive
---
```

(adapted from A1/A2 examples) .

---

## 6) Cross-index smartly

* Add a **cross-Order** tag when your clips clearly operate in two realities (e.g., Mediation & Aperture **cross** Doubling for the pickbox cart) .
* **Optional:** mention one **Debate** doc in a footnote if it frames your filing (e.g., “On the Necessity of Cross-Indexing Densmok”), but keep the slip itself strictly Archive  .

---

## 7) Tone, temperaments, and what *not* to do

* Write as a **Capital archivist**; your job is to **measure pressures** and keep contradictions, not to solve them  .
* Expect (and avoid impersonating) institutional **temperaments** in the margins: **clerkly**, **romantic**, **philosophical**—they shape policy, not your prose .
* Don’t smuggle in **fictional narration**; your “story” is the arrangement of clips + commentary.

---

## 8) Build & test locally (quick dev loop)

* Serve the site (`bundle exec jekyll serve`), then load `…/archive/[order]-[region]-[slug]-[code]/` to verify front matter renders and links work. Your entry will appear under its **Order** in the Archive hub (and in the Region finder) automatically .

---

## 9) Worked micro-example (you can model your first slip on this)

**Filename:** `_archive/mediation-densmok-plot-aperture-b3.md`

```yaml
---
title: "Archive Post B3 — Densmok: Plot by Aperture (device scene & store notes)"
order: "Mediation & Aperture"
region: "Densmok"
catalog_code: "B3"
excerpt: "Two closed eyes make a plot; the device makes the truth pass, not the bodies."
layout: archive
---
```

**Provenance** — Densmok · Night-work at Softwares (storefront); coder scene; screen output note.
**Extract**

> || Two people with their eyes closed… **A plot is the intersection of their stares.** ||
> **Archivist’s Commentary** — The **form** makes the truth: a rule that **constrains bodies** so only a plotted **intersection** may pass. File **Mediation & Aperture**; cross-index A1 **Window Aperture** (Capital) for the same principle: **knowledge may pass; bodies may not**  .

---

## 10) Submission checklist (copy/paste and tick)

* ✅ **Order first; Region second** (cross-index if the device crosses towns) .
* ✅ **Clips follow Protocol 7.3** (Slip/Provenance/Clip/Orders/Commentary) .
* ✅ **Three sections** present (Provenance → Extract → Archivist’s Commentary) and the commentary argues **Order-first** .
* ✅ **Contradictions preserved** (mark, don’t fix) .
* ✅ **Filename & front matter** match Archive specs (Order-primary pattern; entry fields)  .

---

## Appendix — Quick classifiers (use while deciding your Order)

* **Boundary** — unstable edges; lines that move (e.g., Dens’s town/wilderness) .
* **Doubling** — replication without origin (e.g., Quarry roads that bud; Hunt “fivefold” images) .
* **Craving** — appetite as engine (e.g., Dead River handouts/TV/comic franchise) .
* **Silence & Withdrawal** — method installed then voiced recedes (Tower catechism; Sticks quiet-hours) .
* **Violence & Secret Life** — public ledger vs private harm (North murder songs) .
* **Mediation & Aperture** — devices/apertures making access (Capital window; pickbox cart; map that makes a town)  .

> When you’re unsure, re-read **“Why the Archive Files by Orders First.”** It’s the pole star for every filing decision you make .
