# Graduate Student Workflow — **Writing Debate Docs** (Phases • Temperaments • Orders)

Follow these steps to produce Debate documents that build the collection coherently and “in character.”

---

## 1) Classify your document before you write

**Pick:**

* **Phase (I, II, III, IV)** — sets historical posture and temperamental balance.
* **Doc Type** — Memo, Minute, Field Report, Colloquy Note, Counter-Memo, Directive, Hearing, Ruling, Brief, Case Note.
* **Temperament (one only):** Clerkly / Romantic / Philosophical, each with distinct voice markers.
* **Order focus (1–3):** Boundary; Doubling; Craving; Silence & Withdrawal; Violence & Secret Life; Mediation & Aperture.
* **Regions (secondary):** provenance tags only; Orders come first.

---

## 2) Filename, location, and front matter (required)

* **Location:** `_debate/`
* **Filename pattern:** `phaseN-{type}-{descriptive-slug}.md`
  e.g., `phase2-field-edges-report.md`, `phase4-hearing-create-the-case.md`.

**Front matter template (fill every field exactly):**

```yaml
---
layout: debate
title: "Document Title — Descriptive Subtitle"
phase: "II"            # I, II, III, or IV (single Roman numeral)
doc_type: "Field Report"
temperament: "Clerkly" # Clerkly | Romantic | Philosophical
order_focus: ["Boundary"]
regions: ["Dens"]
archive_date: "Year 19, Q2"
date: 2024-01-01       # Jekyll date
clerk_initials: "AB"   # NOT 'clerk:'
status: "Filed"
excerpt: "Brief one-line summary for listings"
permalink: /debate/phase2-field-edges-report/
---
```

Front-matter rules to enforce: Roman-numeral `phase`, arrays for `order_focus` and `regions`, `clerk_initials` not `clerk`, and permalink matching the filename path.

---

## 3) Content structure (no H1 in the body)

> Jekyll prints the title from front matter; **do not** add an H1 in the Markdown body.

**Required sections:**

1. `## Abstract` — 2–4 sentences, in your chosen temperament.
2. `## Exhibits` — include 1–2 **Clips** with `|| … ||` verbatim quoting and temperament-matched commentary.
   **Clip example:**
   `|| Face-window shall be circular; no door; slips only. ||`
   Commentary variants:

   * Clerkly: “Filed under Capital. Protocol documented.”
   * Romantic: “The window speaks: bodies denied, paper permitted.”
   * Philosophical: “Evidence of systematic access control through designed constraint.”
3. `## Main Content/Argument` — 2–6 short paragraphs **in voice**.
4. `## Disposition` — Adopted / Filed Without Action / Referred / Superseded.
5. `## Cross-References` — link to other Debate docs using `{{ '/debate/phaseN-type-slug/' | relative_url }}`.

**Voice discipline:**

* Clerkly = terse procedural; Romantic = narrative testimony; Philosophical = abstract/systematic.
* **Contradictions are evidence**; don’t “fix” them—handle them through your chosen temperament.

---

## 4) Validation & local testing

**Checklist:**

* In `_debate/`; filename pattern OK; YAML valid; permalink matches; ≥1 Clip; Disposition present; Cross-refs included.

**Dev loop:**
`bundle exec jekyll serve` → open `/debate/your-filename/` → check rendering, links, and metadata.

---

## 5) Site integration & navigation

Docs will auto-appear in Debate listings and phase groupings; add/update hub links if you create new subsections (breadcrumbs: *Archivists’ Window → Debate → Phase N*).

---

## 6) Git workflow (suggested)

```bash
git add _debate/your-filename.md
git commit -m "Add Phase II field report on Dens edge contradictions
- Clips from ditch meters vs stool testimony
- Filed under Boundary (Orders-first)"
git push origin main
```

(Feel free to expand with your repo’s commit message norms.)

---

## 7) Quality bar (editorial + technical)

* **Temperamental authenticity**: the doc reads like a specific kind of archivist with real stakes, not generic admin.
* **Evidence discipline**: ≥2 Clips and slip codes when appropriate; commentary shows how the **Order** lens changes interpretation.
* **Phase balance** across the collection: keep the historical temperament mix (I clerkly-heavy; II all three; III philosophical-heavy; IV collision).

---

## 8) Micro-models you can imitate

* **Phase II — Field Report (Clerkly) → Boundary**
  Abstract: meters vs mouths; edge moved overnight.
  Clip: `|| The ditch rose three cm overnight; stool testimony says the town grew. ||`
  Commentary (Clerkly): “Both recorded; contradiction noted. Filed under Boundary (Orders-first); Region: Dens.”

* **Phase IV — Edge-Case Ruling (Clerkly) → Mediation & Aperture**
  Abstract: window/stair design is catalog-relevant.
  Clip: `|| No door; slips only. Stairs throttle crowds, favor licensed knees. ||`
  Commentary (Clerkly): “Physical design enforces access; file under Mediation & Aperture”.

