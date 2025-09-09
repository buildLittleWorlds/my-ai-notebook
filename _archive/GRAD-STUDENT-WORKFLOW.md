# Graduate Student Workflow: Building a New **Archive** Entry (Orders-first)

**You are adding to the archive itself.** The **Archive** is the collection of primary documents; the **Archivists' Debate** is just backstory/context you may cite. The catalog files slips by **Order** (primary) with **Region** as secondary provenance【】, and the hub already exposes both an **Orders index** and a legacy **Finder by Region**【】【】.

---

## 0) Prereqs & Where your file goes

* Run the site locally with Jekyll: `bundle install` → `bundle exec jekyll serve` (URL in README)【】.
* Your new entry lives in the **`_archive/`** collection and renders with the `notebook` layout【】.
* Use the Order-Primary filename pattern: `[order]-[region]-[descriptive-slug]-[code].md` (e.g., `mediation-capital-window-aperture-a1.md`, `doubling-quarry-hunt-silhouettes-d1.md`)【】【】.

---

## 1) Choose your **source** (“ore”)

Pick one thread from the Densworld “ore” files (e.g., **Yeller Quarry**, **Densmok**, **North/Northo**, **Tower/Sticks**, **Dead River**, **Capital**, **Capeast**). These supply your **verbatim clips**. Example ore lines you might mine:

* Yeller Quarry witness account (class drift between respectability/appetite)【】.
* Densmok coder/night-work scene (devices, counting, screen-to-body drift)【】【】.

> Rule of thumb: **your unit of truth is a *clip*** (verbatim or near-verbatim), wrapped in protocol and indexed【】.

---

## 2) Classify by **Order** (primary) → then mark **Region** (secondary)

Use the Orders as working lenses to decide **what the slip *does***:

* **Boundary**: edges that won’t hold (Dens meters vs testimony)【】
* **Doubling**: proliferations; copies without origin (Quarry roads; Castelia fivefold)【】
* **Craving**: desire that makes artifacts (Densmok rigs; Capeast aftermath)【】
* **Silence & Withdrawal**: hands before words; drills that become method (Tower catechism; Sticks quiet-hours)【】
* **Violence & Secret Life**: parallel harm ledgers; North murder songs【】
* **Mediation & Aperture**: devices, windows, carts constrain access【】

Then tag **Region** using the standard geography list (Capital, Dens/Densmok, Quarry, North/Northo, Tower/Sticks, Dead River, Capeast)【】.

---

## 3) Pull 2–5 **Clips** using Protocol 7.3

Follow the **“How to Cite a Clip”** template already in the notebooks aggregate:

```
Slip: [CODE] — [TITLE]
Provenance: [REGION] · [FORM]
Clip: || [VERBATIM EXCERPT] ||
Order(s): [ORDER-1][; ORDER-2]
Commentary: [ARCHIVIST NOTE, 1–3 sentences]
```

Keep contradictions; they are evidence【】【】.

**Example clip pulls (ready to paste):**

* `|| I’d known rich folk … sneak away to Yeller Quarry … eat off greasy tables and get off on greasy thighs … then drive back home to shower off and straighten out. ||` → Provenance: Quarry · Witness Account → **Orders:** Violence & Secret Life; Craving【】
* `|| Two people with their eyes closed … A plot is the intersection of their stares. ||` → Provenance: Densmok · Device Scene/Software Note → **Orders:** Mediation & Aperture (form constrains truth)【】

---

## 4) Create the **frontmatter** & file

Use the site’s standard **Notebook Entry Format**:

```yaml
---
title: "Archive Post [CODE] — [REGION]: [TITLE] ([DOCUMENT TYPE])"
order: "[ONE OF SIX ORDERS]"
region: "[GEOGRAPHIC REGION]"
catalog_code: "[ALPHANUMERIC CODE]"
excerpt: "[KEY QUOTE FROM COMMENTARY]"
---
```

This is exactly what the collection expects【】.
**File path:** `_archive/[order]-[region]-[descriptive-slug]-[code].md` (e.g., `_archive/mediation-densmok-plot-aperture-b3.md`)【】.

---

## 5) Write the three sections

* **Provenance** — *where the material came from and in what form* (e.g., “Quarry · Witness account; alley bills; repair ledger”)【】.
* **Extract** — your **clips** in blockquotes / `|| … ||` with minimal framing【】.
* **Archivist’s Commentary** — 2–6 paragraphs that argue why this fits the chosen **Order** (not just the Region). Keep mismatches in view; do not reconcile them【】【】.

> Touchstone examples to imitate:
>
> * **A1 — Capital: Window Aperture** (Mediation & Aperture)【】【】
> * **D1/D2 — Yeller Quarry: Doubles** (provenance vs. copies)【】【】
> * **I1 — Sticks: Withdrawal Logs** (silence as method)【】【】

---

## 6) Cross-index (optional but encouraged)

Your notebook entry can point to **one** Debate doc that frames your choice (history/context), e.g.:

* Phase II **“Edges to Edges”** (why Withdrawal is a method) → `/debate/phase2-colloquy-edges-to-edges/`【】
* Phase II **Counting/Cart** cases (doubling; device-first filing)【】

Remember: the Debate is meta-history; the **Notebook** is the shelf. Use the Debate sparingly to **justify** the Order-first filing the hub already announces【】.

---

## 7) Build & test

* `bundle exec jekyll serve` → Navigate to `.../archive/[order]-[region]-[descriptive-slug]-[code]/` and check frontmatter renders, links work【】.
* Your entry will appear under the correct **Order** in the Archive hub (and in the Region finder) automatically【】【】.

---

## 8) Submission checklist (Notebooks)

* [ ] File in `_archive/` named `[order]-[region]-[descriptive-slug]-[code].md`【】
* [ ] Frontmatter matches **Entry Format**【】
* [ ] **Order** chosen from the six; **Region** marked as provenance【】【】
* [ ] ≥2 Clips, Protocol 7.3 formatting; contradictions intact【】【】
* [ ] **Commentary** argues the Order-first reasoning (not just geography)【】

---

## 9) Worked mini-example (you can copy-edit into a real post)

**Filename:** `_archive/mediation-densmok-plot-aperture-b3.md`

```yaml
---
title: "Archive Post B3 — Densmok: Plot by Aperture (device scene & store notes)"
order: "Mediation & Aperture"
region: "Densmok"
catalog_code: "B3"
excerpt: "Two closed eyes make a plot; the device makes the truth pass, not the bodies."
---
```

**Provenance**
Densmok · Night-work at **Softwares** (storefront); coder scene; screen output note.

**Extract**

> || Two people with their eyes closed. No touching. No speaking. No moving to make noise. Each stares ahead. **A plot is the intersection of their stares.** ||【】

**Archivist’s Commentary**
The **form** makes the truth: a rule that **constrains bodies** so that only a plotted **intersection** may pass. This fits **Mediation & Aperture**—like the Capital’s window (“no door; slips only”), the Densmok apparatus filters access by design【】. Cross-index to **A1 Window Aperture** for the shared principle that **knowledge may pass; bodies may not**【】. Region remains Densmok (provenance), but the shelf is the **Order**.

(*Optional “Further reading” link for the student editor: Phase II **Edges to Edges** on method-as-withdrawal, for kinship of technique becoming bodily habit【】.*)

---

## 10) Quick “what next” prompts (pick one and go)

* **Quarry → Violence & Secret Life (cross Craving):** Take the Yeller double-life stanza/witness stream and build a slip on **parallel ledgers** (respectability vs appetite)【】.
* **Dead River → Doubling:** Build a **Counting-Five** dossier (tap, cart, shrine misses) using the case register style from existing entries【】【】.
* **Tower/Sticks → Silence & Withdrawal:** Pair a Tower drill clip with a Sticks quiet-hours ledger to show **silence as method**【】【】.

---

### Why this workflow matches the site’s logic

* The Archive hub explicitly **adopts Orders-first** and points readers to the Debate only as history【】.
* The README anchors **Orders** and **Regions** and defines the **entry format** your file must follow【】【】.
* The aggregate shows how to **cite clips** and to **preserve contradictions** inside the slip itself【】【】.
