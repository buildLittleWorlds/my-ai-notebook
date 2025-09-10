# GRAD-STUDENT-CONTEXT — AI Hermeneutics Kit

## What this section is (and isn’t)

**AI Hermeneutics Kit** is the site’s **systematic, out-of-character framework** for interpreting AI-generated texts. Its purpose is to show how AI’s challenges are **intensifications** of long-running hermeneutic questions; pages move from theory to **practical methods** of reading . The kit is organized as a hub with component pages across Foundations, Deleuze, Butler, and more, all linked from `/ai-hermeneutics/ai-hermeneutics-kit/`  .

**Belongs here**

* **Interpretive frameworks** for AI texts; **adaptations** of traditional theory (Foucault/Gadamer/Deleuze/Butler/etc.); **practical methods**; **cross-theoretical syntheses** .

**Does *not* belong here**

* Work-in-progress reflections → `_posts/`
* Romantic-specific methods → `_romantic/`
* **Fictional Densworld examples** (keep theory collections non-fictional) .

## Where this kit sits in the site

On the homepage, **AI Hermeneutics** is one of the two theory pillars (paired with Romantic), distinct from **Blog Posts** (writing) and the fictional **Archive/Debate** system (worldbuilding) .

## Governing perspective (how the kit thinks)

**Central thesis.** AI interpretive problems aren’t totally new; they **amplify** existing ones. Properly adapted, traditional theory still works—just re-tooled for algorithmic authorship .

**Major streams.**
Foundations: **Author-function**, **Interpretive dialogue**, **Hermeneutics of risk**; Deleuzian: **machine**, **forces**, **assemblage**; Butlerian: **performativity**, **interiority**, **parody**, **regulation**; plus **genealogy**, **distanciation**, **death of the author** .

## The shape of the collection (what’s in the kit)

* **Hub** (`ai-hermeneutics-kit.md`): overview + links + integration map .
* **Component pages** grouped by Foundations/Deleuze/Butler/Additional frameworks; \~18–20 files total  .

## Typical work you’ll do here

1. **Translate a theory** (e.g., Foucault’s author-function) into AI-era terms and **show an analytic method** for AI text.
2. **Build a method page** (e.g., reception/paratext diagnostics) that a reader can actually apply.
3. **Cross-link** adjacent frameworks so readers can triangulate an approach.
   All in **kit voice**: systematic, theoretically rigorous, practically oriented, cross-disciplinary .

## File and layout basics (the boring but necessary stuff)

* **Naming**:

  ```
  ai-kit-[topic].md
  ai-kit-[theorist]-[concept].md
  ai-hermeneutics-kit.md   (hub)
  ```


* **Front matter**:

  ```yaml
  ---
  layout: kit
  title: "Page Title with Subtitle"
  kit_type: ai_hermeneutics
  ---
  ```


* **Location**: `_ai_hermeneutics/your-filename.md` .
* **Hub/back link**: use the “← Back to AI Hermeneutics Kit” pill (see hub page HTML) .

## Standard page template (use this every time)

1. **Theoretical Foundation** — what theory you’re adapting
2. **AI Application** — how it maps to AI-generated texts
3. **Interpretive Method** — step-by-step toolset
4. **Contemporary Relevance** — why it matters now
5. **Cross-References** — links to related kit pages&#x20;
   **6) Densworld Addendum (seed)** — 2–4 sentences, out-of-character (details below)

> Tip: reception/narratology/paratext lenses are especially actionable for AI (Leerstellen; implied reader; paratext thresholds like prompts/model cards) .

---

# Densworld Addendum for AI Hermeneutics pages (short, required)

**Why add this to a theory page?**
We keep the kit non-fictional, but each page should end with a tiny **out-of-character seed** that connects your theory to either the Archive or Debate system—just like your blog-post practice. Choose the path that best fits your framework.

**Choose Your Connection Path:**

### Archive Connection (for concrete scenarios)
When your theory suggests **concrete Densworld scenarios, devices, or practices**:
* A **concrete image/device/practice** your theory suggests (one beat, not a scene)
* A **proposed Order** and **likely Region** for where archivists might file a future document

### Debate Connection (for methodological questions)  
When your theory suggests **interpretive methodology questions or archival policy issues**:
* A concrete archival methodology problem your theory raises
* A likely **Phase** (Phase I-IV of archival development)
* A likely **Document Type** and **Archivist Temperament**

**Template snippets** (append under your "Cross-References"):

```markdown
### Densworld Addendum (seed) — Archive Focus
**Order:** [Boundary | Doubling | Craving | Silence & Withdrawal | Violence & Secret Life | Mediation & Aperture]  
**Region:** [Capital | Dens/Densmok | Quarry | North/Northo | Tower/Sticks | Dead River | Capeast]

[2-4 sentences describing the concrete scenario/device your theory suggests]

### Densworld Addendum (seed) — Debate Focus  
**Phase:** [Phase I | Phase II | Phase III | Phase IV]  
**Document Type:** [memo | minute | field report | hearing | counter-memo | directive | ruling | brief | case note | colloquy note]  
**Likely Temperament:** [Clerkly | Romantic | Philosophical]

[2-4 sentences describing the methodological question or policy debate your theory suggests]
```

**Three micro-examples (Archive vs. Debate paths):**

* **Author-Function (Archive path).** A Capital bureau treats **model cards** as "authors," requiring every public statement to cite a **hash** of the deployed weights. → **Order: Mediation & Aperture; Region: Capital** (archive entry documents hash-citation practices).
* **Author-Function (Debate path).** Should "algorithmic authorship" documents require new filing categories beyond traditional author-function classifications? → **Phase III Hearing; Philosophical temperament** proposes sub-orders; **Clerkly** argues existing categories suffice.
* **Interpretive Dialogue (Archive path).** A Tower clinic experiments with "fused horizon" reading groups where a text's **safety banner** is discussed alongside the output, altering uptake. → **Order: Boundary; Region: Tower/Sticks**.

---

## Quick orientation for a brand-new grad student

1. Skim the **hub** to see components and navigation .
2. Read one **Foundations** page (Author-function, Dialogue, Risk) to anchor the central thesis  .
3. Choose a **framework stream** (Deleuze/Butler/etc.) and a **concrete AI reading task** to pair it with .
4. Draft using the **standard template**, then tack on the **Densworld Addendum (seed)**.
5. Add **cross-links** between related kit pages and back to the hub .

## Success criteria (how we know a page fits)

* **Thesis alignment** (AI as intensification) is explicit and accurate .
* **Usable method** (your “Interpretive Method” is actionable).
* **Cross-references** connect the hub and at least two related pages .
* **Addendum seed** follows either Archive format (Order + Region) or Debate format (Phase + Doc Type + Temperament) for future fictional development.

## Submission checklist (copy/paste and tick)

* ✅ **Right section?** Systematic AI hermeneutics (not a post; not Romantic; not fiction) .
* ✅ **Filename & front matter** follow kit specs  .
* ✅ **Back-to-hub pill** in place .
* ✅ **Six-part structure** (Foundation → AI Application → Method → Relevance → Cross-Refs → **Addendum** ) .
* ✅ **Addendum seed** follows either Archive format (Order + Region) or Debate format (Phase + Doc Type + Temperament).
