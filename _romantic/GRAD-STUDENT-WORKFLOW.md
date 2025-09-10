# Graduate Student Workflow — Romantic Quick Kit

## Quick overview (what you’re making)

You are writing **systematic, out-of-character theory pages** that teach a reusable Romantic method or concept. Pages are instructional, definitive, and cross-linked—not exploratory posts and not fiction   .

---

## Step 0 — Place your work correctly

**Belongs in the Romantic Kit**

* Practical methods (“How to read for \[concept]”), systematic definitions, applications, historical contexts, and cross-references .

**Does *not* belong here**

* Work-in-progress reflections → `_posts/`
* AI-specific methods → `_ai_hermeneutics/`
* Any fictionalized examples → keep fiction out of theory collections .

---

## Step 1 — Pick your page type

* **Core Method** (e.g., Hermeneutics) and **Key Concepts** (Authenticity; Organic Form; Gefühl; etc.) .
* **Context** (Germany / England / America) .
* **Reference** (Glossary / cross-index) .

Write in **kit voice**: instructional, systematic, definitive, cross-referenced (“Apply this method by…” “To read for…”) .

---

## Step 2 — Outline with the standard template (+ the Addendum)

Start from this **six-part** structure (the first five are required by the kit; #6 is our new hand-off):

1. **Conceptual Definition**
2. **How to Read For \[Concept]** (actionable steps)
3. **Historical Development**
4. **Cross-References** (link related kit pages)
5. **Application Examples** (brief, concrete)&#x20;
   **6) Densworld Addendum (seed)** — 2–4 sentences, out-of-character; see Step 6.

> All pages should visibly lean on the **two-rail method** (psychological + grammatical → authenticity) as your analytic backbone .

---

## Step 3 — Draft the core analysis (use the two-rail method)

* **Psychological**: name the work’s pattern of choices
* **Grammatical**: name the conventions it engages
* **Authenticity**: *demonstrate* their coherence with evidence (don’t assert) .

Keep examples textual/analytical (no in-character scenes) .

---

## Step 4 — Technical specs (files, front matter, nav)

**Naming**

```
romantic-kit-[topic].md
romantic-quick-kit.md  (hub)
```



**Front matter**

```yaml
---
layout: kit
title: "Page Title"
kit_type: romantic
---
```



**Location**: place files in `_romantic/` .
**Top nav pill** (add to top of every page):

```markdown
<div class="top-links">
  <a href="{{ '/romantic/romantic-quick-kit/' | relative_url }}" class="quickkit-pill">← Back to Quick Kit Menu</a>
</div>
```



---

## Step 5 — Cross-linking (how to wire the kit together)

* Link back to the hub and across related concepts using `relative_url`  .
* Model link text on:
  `…the [two-rail method](/romantic/romantic-kit-hermeneutics/) → [authenticity](/romantic/romantic-kit-authenticity/)…` .

---

## Step 6 — The **Densworld Addendum (seed)** (short, required)

Every Romantic Kit page ends with a **tiny, non-fictional hand-off** to either the Archive or Debate system. Choose the connection path that best fits your concept—concrete artifacts/scenes suggest Archive entries; methodological questions suggest Debate documents.

**Choose Your Connection Path:**

### Option A: Archive Connection
When your concept suggests **concrete Densworld scenes, artifacts, or practices**:
* A **concrete image, device, practice, or scene-seed** your concept suggests
* A **proposed Order** and **likely Region** (see canonical lists below)

### Option B: Debate Connection  
When your concept suggests **methodological questions or archival policy issues**:
* A concrete archival policy problem or interpretive question your concept raises
* A likely **Phase** (Phase I-IV of archival development)  
* A likely **Document Type** and **Archivist Temperament** (see lists below)

**Template snippets** (append under "Application Examples"):

```markdown
### Densworld Addendum (seed) — Archive Focus
**Order:** [Boundary | Doubling | Craving | Silence & Withdrawal | Violence & Secret Life | Mediation & Aperture]  
**Region:** [Capital | Dens/Densmok | Quarry | North/Northo | Tower/Sticks | Dead River | Capeast]

[2-4 sentences describing the concrete scene/artifact your concept suggests]

### Densworld Addendum (seed) — Debate Focus  
**Phase:** [Phase I | Phase II | Phase III | Phase IV]  
**Document Type:** [memo | minute | field report | hearing | counter-memo | directive | ruling | brief | case note | colloquy note]  
**Likely Temperament:** [Clerkly | Romantic | Philosophical]

[2-4 sentences describing the methodological question or policy debate your concept suggests]
```

---

## Step 7 — Final polish & submission checklist

Before you PR, confirm:

* ✅ **Right section** (kit, not post/AI kit/fiction)&#x20;
* ✅ **Front matter + filename + location** match specs &#x20;
* ✅ **Top nav pill** points to the hub&#x20;
* ✅ **Six-part structure** (Definition → How → History → Cross-Refs → Applications → **Addendum**)&#x20;
* ✅ **Two-rail method** is explicit in your analysis&#x20;
* ✅ **Cross-links** to the hub and at least 2 related kit pages&#x20;
* ✅ **Addendum seed** follows either Archive format (Order + Region) or Debate format (Phase + Doc Type + Temperament)

---

## Appendix — Canonical tags (for your Addendum)

### For Archive Connections:
* **Orders**: Boundary; Doubling; Craving; Silence & Withdrawal; Violence & Secret Life; Mediation & Aperture
* **Regions**: Capital; Dens/Densmok; Quarry; North Town/Northo; Tower/Sticks; Dead River; Capeast

### For Debate Connections:
* **Phases**: Phase I (Years 1-12, Regional drawers); Phase II (Years 13-20, Geographic faults); Phase III (Year 22, Orders proposal); Phase IV (Year 23+, Implementation)
* **Document Types**: memo, minute, field report, hearing, counter-memo, directive, ruling, brief, case note, colloquy note  
* **Temperaments**: Clerkly (procedural, protocol-focused); Romantic (narrative, witness-focused); Philosophical (systematic, category-focused)
