# Site Structure Overview

This document explains how Professor Plate's Notebook is organized as both a scholarly resource and a practical training laboratory for graduate students in literary theory.

## Site Architecture Summary

**Professor Plate's Notebook** operates as a **self-referential academic ecosystem** combining:
- Real theoretical work (blog posts, systematic frameworks)
- Fictional archival practice (The Densworld Archive system)
- Institutional methodology (debates over interpretive classification)
- Pedagogical scaffolding (grad student workflows and context guides)

**Five Main Collections:**
1. **Posts** (`_posts/`) - Out-of-character academic writing serving as the site's "engine" (110+ files)
2. **Romantic** (`_romantic/`) - Systematic Romantic theory framework with two-rail method (11 components)
3. **AI Hermeneutics** (`_ai_hermeneutics/`) - AI interpretation framework showing AI as intensification (20 components)
4. **Archive** (`_archive/`) - Fictional archive entries organized by Orders-first filing (20+ files)
5. **Debate** (`_debate/`) - Meta-archival methodology discussions across four historical phases (20+ files)

## Graduate Student Pedagogical System

**Training Architecture:** Every collection contains pedagogical scaffolding:

### Context & Workflow Files
**POSTS Collection Training:**

**ROMANTIC Collection Training:**
- **Context**: Romantic Quick Kit is the site’s systematic, outofcharacter framework for interpreting Romantic literature and thought. It provides methods and concepts you can actually apply while reading—formal, instructional, and crossreferenced (not exploratory posts, and not fiction) . Keep the kit nonfictional: no incharacter scenes or invented Densworld documents here; those belong to Archive/Debate .
- **Workflow**: You are writing systematic, outofcharacter theory pages that teach a reusable Romantic method or concept. Pages are instructional, definitive, and crosslinked—not exploratory posts and not fiction .

**AI_HERMENEUTICS Collection Training:**
- **Context**: AI Hermeneutics Kit is the site’s systematic, outofcharacter framework for interpreting AIgenerated texts. Its purpose is to show how AI’s challenges are intensifications of longrunning hermeneutic questions; pages move from theory to practical methods of reading . The kit is organized as a hub with component pages across Foundations, Deleuze, Butler, and more, all linked from `/aihermeneutics/aihermeneuticskit/` .
- **Workflow**: You’re writing systematic theory pages that adapt critical frameworks for AI text interpretation—rigorous, practical, and crosslinked (not exploratory posts; not fiction) .

**ARCHIVE Collection Training:**

**DEBATE Collection Training:**


## Conceptual Frameworks by Collection

### Blog Posts — Five Recurring Subject Bands
From the posts context file:

### Romantic Kit — Two-Rail Method
**Governing Method**: Psychological pattern of choices + Grammatical conventions → demonstrable Authenticity

### AI Hermeneutics Kit — Central Thesis
**Core Philosophy**: AI interpretive problems aren't totally new; they amplify existing hermeneutic tensions (author-function, performativity, distanciation, dialogue, risk)

### Archive — Orders-First Filing Philosophy
**Core Principle**: "In Densworld, mechanisms generate geographies, and patterns outlast places" — file by what documents **do**, not where they come from

**The Six Orders (Primary Classification):**
1. **Boundary** — edges that won’t hold
2. **Doubling** — copies without origin
3. **Craving** — appetite as engine
4. **Silence & Withdrawal** — truth through quiet practice
5. **Violence & Secret Life** — parallel harm ledgers
6. **Mediation & Aperture** — devices/windows that govern access .

**Densworld Regions (Secondary Classification):**

### Debate — Three Archivist Temperaments & Four Phases
**Three Institutional Voices:**
**The central question:**
* **Clerkly** — Procedural custodians; fear chaos; short, precise sentences; fixate on custody, stamps, protocol. “Filed under Dens. Contradiction noted.”
* **Romantic** — Narrative witnesses; fear fragmentation and silence; dramatize tensions; let minor voices speak. “She swore the ditch had grown; the town agreed.”

**Four Historical Phases:**
* **Phase I — Regional Drawers (Years 1–12).** Provenance-first doctrine; clerkly dominance; early systematizing seeds.
* **Phase II — Faults in Geography (Years 13–20).** Contradictions spill across boroughs; the three voices fully appear.
* **Phase III — Orders Proposal (Year 22).** Six Orders proposed; philosophical dominance; clerkly resistance.
* **Phase IV — Implementation & Objections (Year 23+).** Orders-first directive, cross-indexing; hearings on catalog feedback effects.

## Densworld Integration System

**The Systematic Seeding Process:**
1. **Blog Posts** test ideas → generate Densworld Addendum seeds (Order + Region + optional Debate doc type)
2. **Theory Collections** formalize recurring concepts → also end with Densworld Addendum seeds
3. **Archive/Debate Collections** realize fictional scenarios suggested by blog/theory seeds
4. **Result**: Self-referential academic ecosystem demonstrating theory-in-practice

**Densworld Addendum Requirements:**
- Every blog post and kit page must end with 2-6 sentence out-of-character seed
- Must propose specific Order and Region for potential fictional development
- Optionally suggests Debate document type (memo, minute, hearing, etc.)
- Remains out-of-character (hand-off seed, not fiction itself)

## Navigation Flow & Relationships

### Homepage Structure (index.md → home.html layout)
The homepage presents three grouped sections:

**Writing Section:**
- Blog Posts → `/posts/` (posts-list.html layout)

**Theoretical Frameworks Section (paired):**
- Romantic Quick Kit → `/romantic/` → `/romantic/romantic-quick-kit/` (main hub)
- AI Hermeneutics Kit → `/ai-hermeneutics/` → `/ai-hermeneutics/ai-hermeneutics-kit/` (main hub)

**Archive System Section (paired):**
- The Archive → `/archive/` (archive-hub.html layout with auto-generated Order listings)
- The Debate of the Archivists → `/debate/` → `/debate/archivists-debate/` (main hub)

### Voice & Character Distinctions

**Out-of-Character Sections:**
- **Blog Posts**: First-person, reflective, provisional thinking by Professor Plate
- **Kits**: Instructional, systematic, definitive frameworks for practical application

**In-Character Sections:**
- **Archive**: Capital archivists analyzing fragments with Protocol 7.3
- **Debate**: Institutional documents in three temperamental voices (Clerkly, Romantic, Philosophical)

### How Collections Are Related

**Blog Posts ←→ Kits**: Blog posts develop ideas that become formalized in the two theoretical frameworks

**Kits ←→ Archive**: The theoretical frameworks provide interpretive methods; both seed fictional development

**Archive ←→ Debate**: The debate documents explain the methodology behind the archive's organization system

**Integration Flow**: Real scholarship → systematic frameworks → fictional realization → methodological reflection


## Collection Organization Details

### Posts Collection (`_posts/`) — The Site's Intellectual Engine
**Purpose:** Out-of-character academic writing serving as the site's "engine" — real essays by Professor Plate
**Voice:** First-person, reflective, conversational but scholarly; provisional thinking that questions assumptions
**Hub Page:** `posts.md` → `/posts/` (posts-list.html layout)
**Individual Posts:** Use post.html layout
**Count:** 113 files
**Integration:** Every post must end with Densworld Addendum seed (Order + Region + optional Debate doc type)
**Navigation:** Simple chronological list with post numbers

### Romantic Collection (`_romantic/`) — Systematic Romantic Theory Framework
**Purpose:** Systematic method and key concepts for interpreting Romantic literature and thought
**Governing Method:** Two-rail approach (Psychological pattern of choices + Grammatical conventions → demonstrable Authenticity)
**Voice:** Instructional, definitive, cross-referenced ("How to read for [concept]")
**Landing Page:** `romantic.md` → `/romantic/` (simple overview)
**Main Hub:** `_romantic/romantic-quick-kit.md` → `/romantic/romantic-quick-kit/` (detailed framework)
**Individual Pages:** 11 files using kit.html layout
**Standard Template:** Definition → Method → Historical Development → Cross-References → Applications → Densworld Addendum
**Organization:** Topics grouped into Method, Core Concepts, and Historical Contexts
**Components:**
- GRAD-STUDENT-WORKFLOW: Page Title
- romantic-kit-authenticity: Authenticity (The Evidenced 'Self')
- romantic-kit-contexts-america: Contexts: America (The Democratic Self)
- romantic-kit-contexts-england: Contexts: England (The Poetic Revolution)
- romantic-kit-contexts-germany: Contexts: Germany (The Philosophical Engine)
- romantic-kit-glossary: Glossary & Key Concepts
- romantic-kit-hermeneutics: A Romantic Method for Reading
- romantic-kit-organic-form: The Organic vs. The Mechanical (A Theory of Form)
- romantic-kit-technology-machine: Technology & The Machine (The Shadow of the Organic)
- romantic-quick-kit: Romantic Quick Kit

### AI Hermeneutics Collection (`_ai_hermeneutics/`) — AI Interpretation Framework
**Purpose:** Framework for interpreting AI-generated texts, showing AI challenges as intensifications of traditional hermeneutic questions
**Central Thesis:** AI problems aren't alien; they amplify existing interpretive tensions (author-function, performativity, distanciation, dialogue, risk)
**Voice:** Systematic, theoretically rigorous, practically oriented, cross-disciplinary
**Landing Page:** `ai-hermeneutics.md` → `/ai-hermeneutics/` (simple overview)
**Main Hub:** `_ai_hermeneutics/ai-hermeneutics-kit.md` → `/ai-hermeneutics/ai-hermeneutics-kit/` (detailed framework)
**Individual Pages:** 20 files using kit.html layout
**Standard Template:** Theoretical Foundation → AI Application → Interpretive Method → Contemporary Relevance → Cross-References → Densworld Addendum
**Organization:** Grouped into Theoretical Foundations, Critical Frameworks (Deleuze, Butler, Further), and Reference Materials
**Components:**
- ai-hermeneutics-kit: AI Hermeneutics Kit
- ai-kit-author-function: The Author-Function: From Romantic Soul to Algorithmic System
- ai-kit-butler-interiority: The Surface of the Soul: AI and the Illusion of Interiority
- ai-kit-butler-parody: The Copy of a Copy: AI, Parody, and the End of the Original
- ai-kit-butler-performativity: Beyond the Author: The AI as a Performative Subject
- ai-kit-butler-regulation: The Coherent Author as a Regulatory Fiction
- ai-kit-dangerous-book: The Dangerous Book: On Texts That Transform and Transgress
- ai-kit-death-author: The Death of the Author (From Theory to Reality)
- ai-kit-deleuze-assemblage: The Human-AI Assemblage: A New Desiring-Machine
- ai-kit-deleuze-forces: Active vs. Reactive: A Deleuzian Diagnostic for AI Production
- ai-kit-deleuze-goodwill: Beyond Goodwill: The Text as a Deleuzian Machine
- ai-kit-deleuze-monotony: Monstrous Monotony: The AI as a Deleuzian Machine
- ai-kit-distanciation: Distanciation & AI
- ai-kit-genealogy: Genealogy of Interpreters (Historical Perspectives on AI Texts)
- ai-kit-glossary: Glossary & Key Concepts
- ai-kit-hermeneutics-of-risk: AI and the Hermeneutics of Risk: New Forms of Dialogue and Danger
- ai-kit-interpretive-dialogue: The Interpretive Dialogue: When the Text Reads the Reader
- ai-kit-machine-speaks: The Machine Speaks (Philosophy of AI Language)
- GRAD-STUDENT-WORKFLOW: Page Title with Subtitle

### Archive Collection (`_archive/`) — The Capital Archive & Densworld System
**Purpose:** Fictional but rigorous archival practice presenting fragments from Densworld, organized by Orders (what documents do) rather than geography
**Filing Philosophy:** Orders-first (primary) then Region (secondary provenance) — "mechanisms generate geographies, patterns outlast places"
**Voice:** Capital archivists analyzing fragments; professional, fragment-preserving, interpretive, deliberately unresolved
**Method:** Each slip follows Protocol 7.3 (Slip Code → Provenance → Clip → Order(s) → Commentary)
**Hub Page:** `archive.md` → `/archive/` (archive-hub.html layout)
**Individual Entries:** 23 files using archive.html layout
**Organization:** Auto-generated sections by six Orders, plus regional finder
**Six Orders Classification System:**
- Boundary (3 entries)
- Craving (2 entries)
- Doubling (2 entries)
- Mediation & Aperture (6 entries)
- Silence & Withdrawal (6 entries)
- Violence & Secret Life (3 entries)

### Debate Collection (`_debate/`) — The Archive's Self-Argument
**Purpose:** In-character institutional documents about how the Capital Archive organizes reality — the Archive's methodological meta-debate
**Central Tension:** Does the archive mirror the world's structure, or does the archive's language help shape it?
**Voice:** Three archivist temperaments (Clerkly, Romantic, Philosophical) across four historical phases
**Document Types:** Memo, Minute, Field Report, Colloquy Note, Counter-Memo, Directive, Hearing, Ruling, Brief, Case Note
**Landing Page:** `debate.md` → `/debate/` (simple overview)
**Main Hub:** `_debate/archivists-debate.md` → `/debate/archivists-debate/` (chronological phases)
**Individual Documents:** 24 files using debate.html layout
**Organization:** Four chronological phases documenting transformation from Regional filing to Orders-first filing
**Four Historical Phases:**
* **Phase I — Regional Drawers (Years 1–12).** Provenance-first doctrine; clerkly dominance; early systematizing seeds.
* **Phase II — Faults in Geography (Years 13–20).** Contradictions spill across boroughs; the three voices fully appear.
* **Phase III — Orders Proposal (Year 22).** Six Orders proposed; philosophical dominance; clerkly resistance.
* **Phase IV — Implementation & Objections (Year 23+).** Orders-first directive, cross-indexing; hearings on catalog feedback effects.

## Layout System

**Layout Hierarchy:**
- `default.html` - Base layout with header, navigation pills, footer
- `home.html` - Homepage with grouped tile sections
- `post.html` - Individual blog posts with prev/next navigation
- `posts-list.html` - Blog index with numbered post links
- `kit.html` - Individual kit pages (both romantic and AI hermeneutics)
- `archive-hub.html` - Auto-generates Order sections and regional finder
- `archive.html` - Individual archive entries with metadata
- `debate.html` - Debate documents with phase information

## Key Densworld Elements

### Recurring Devices & Figures
From the Archive context documentation:
* **The Pickbox Cart.** A traveling aperture “opening inside into rooms upon rooms,” shadowed by five women—perennially misfiled by Region, correctly seen as device-first (Orders: **Mediation & Aperture**; cross **Violence & Secret Life / Doubling**)  .
* **The Map that Makes a Town.** Dead River exists **because a map names it**; maps beget maps (Orders: **Mediation & Aperture**, **Doubling**) .
* **Yeller’s Fivefold.** Castelia’s silhouette and North’s “yeller stanza” are a **code** tying number to harm and desire (Orders: **Violence & Secret Life**, cross **Doubling**)  .
* **Edges to Edges.** The Tower drill and Sticks quiet-hours show how **language becomes habit**, then falls silent (Order: **Silence & Withdrawal**)  .
* **Capital Apertures.** Windows/stairs as **filters**: the city’s truth is throttled by openings and tolerances (Order: **Mediation & Aperture**) .

### Key Figures:
* **The Mapmaker** — pulls the pickbox cart; sleeps while **five women** watch; routes touch Northo, North, Dead River, Capeast. The cart is **authorless burden** (debated); the women sometimes **precede the story** the records try to write  .
* **The Five Women** — walk “as one though they were five”; clothing patterns vary and trigger official **protests**; agency misread as offense (Orders: **Boundary**, **Silence & Withdrawal**, cross **Violence & Secret Life**)  .
* **Castelia** — artist of the **Hunt** woodcuts; provenance splinters into burrs, inks, copies (Order: **Doubling**) .
* **The Minor Archivist** — Capital clerk whose notes teach **aperture logic** (“I speak through the window”) (Order: **Mediation & Aperture**) .
* **Cassie, E., Ria** — Mirado Sticks “withdrawal” cases; each exhibits silence as method with differing complications (Order: **Silence & Withdrawal**) .
* **Queenmater (handouts)** — a street device teaching **Craving** in Dead River; also a forum flashpoint in Sticks logs  .

## Technical Configuration Details

**Jekyll Collections (from _config.yml):**
```yaml
collections:
  romantic:
    output: true
    permalink: /romantic/:name/
  ai_hermeneutics:
    output: true
    permalink: /ai-hermeneutics/:name/
  archive:
    output: true
    permalink: /archive/:name/
  debate:
    output: true
    permalink: /debate/:name/

```

**Navigation Integration:**
- Homepage tiles link directly to collection hub pages
- Site header (default.html) shows kit navigation pills on non-home pages
- Cross-linking between related concepts within collections
- Back-to-hub links on individual pages
