# Who’s who (role handles you can use in issues/commits)

| Grad | Handle → Role                              | Section             | What it means (1-liner)                                                                                                             |
| ---- | ------------------------------------------ | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| A    | **Conductor** → Structure & Integrations   | whole site          | Owns build, layouts, link health, front-matter linting, nav, and cross-collection wiring (no daily file required)                   |
| B    | **Engine** → Blog                          | `_posts/`           | Daily out-of-character post; ends with a Densworld Addendum seed connecting to Archive (Order + Region) OR Debate (Phase + Doc Type + Temperament) |
| C    | **Romantic Kitmaker** → Romantic Quick Kit | `_romantic/`        | Systematic theory page (two-rail method), with a tiny Addendum seed connecting to Archive (Order + Region) OR Debate (Phase + Doc Type + Temperament) |
| D    | **AI Hermeneut** → AI Hermeneutics Kit     | `_ai_hermeneutics/` | Systematic AI-reading method page, cross-linked to the hub (out-of-character), with Addendum seed connecting to Archive OR Debate |
| E    | **Slipwright** → Archive                   | `_archive/`         | In-character Capital archivist slip, **Orders-first** (Order primary, Region secondary), using Protocol 7.3 clips                   |
| F    | **Debate Clerk** → Debate                  | `_debate/`          | In-character institutional doc (pick Phase + Temperament + Doc Type) with proper front matter and Clips; cross-link back to slips   |

# Daily checklists (5 creators ship 1 file/day)

## Engine (Blog)

* Draft a 500–900-word post in one of five bands (Hermeneutics, AI & Interpretation, Romantic method, Pedagogy/Practice, Bridgework)&#x20;
* **End with a Densworld Addendum seed**: connect to Archive (Order + Region) OR Debate (Phase + Doc Type + Temperament), 1–3 sentences for what could be realized next
* File pattern/layout: `_posts/YYYY-MM-DD-post-[number].md` using `layout: post` (increment post\_number)&#x20;

**Definition of done**: seed present; at least one cross-link to a Kit hub or prior post; builds locally.

## Romantic Kitmaker (Romantic Quick Kit)

* Pick a focused concept (e.g., Authenticity, Organic Form, Gefühl, Technology & the Machine) and write a short **systematic** page using the six-part template (Definition → How-to → History → Cross-refs → Applications → **Addendum**)&#x20;
* **Keep it non-fictional**; Addendum is out-of-character and tiny (2–4 sentences), connecting to Archive (Order + Region) OR Debate (Phase + Doc Type + Temperament)
* Front matter:

  ````yaml
  ---
  layout: kit
  title: "Page Title"
  kit_type: romantic
  ---
  ``` :contentReference[oaicite:20]{index=20}
  ````

**Definition of done**: two-rail clarity; Addendum seed; back-link pill to hub; at least two cross-refs to existing kit pages .

## AI Hermeneut (AI Kit)

* Add a concise method page: Theoretical foundation → AI application → Interpretive method → Contemporary relevance → Cross-Refs → Addendum (out-of-character, connecting to Archive OR Debate)
* Anchor to hub and related pages (e.g., **Death of the Author**, author-function)&#x20;

**Definition of done**: actionable method; at least one cross-ref; builds locally.

## Slipwright (Archive)

* Choose a thread from ore (e.g., **pickbox cart**, **roads that bud**, **edges to edges**, **map that makes a town**) and assemble **2–5 Clips** with **Protocol 7.3** (Slip code, Provenance, `|| clip ||`, Order(s), 1–3-sentence commentary) &#x20;
* **File by Order first**, Region second; three sections: **Provenance → Extract → Archivist’s Commentary**; maintain contradictions as evidence &#x20;
* Filename/front matter pattern:

  * `_archive/[order]-[region]-[slug]-[code].md`
  * Minimal front matter model:

    ````yaml
    ---
    title: "Archive Post X — Region: Title (form)"
    order: "Mediation & Aperture"
    region: "Capital"
    catalog_code: "X"
    layout: archive
    excerpt: "One-liner for listing."
    ---
    ``` :contentReference[oaicite:28]{index=28}
    ````

**Definition of done**: Order-first clear; 2–5 properly formatted Clips; commentary argues why the Order fits; optional cross-index to one Debate doc .

## Debate Clerk (Debate)

* Pre-classify: **Phase (I–IV)**, **Doc Type** (Memo/Minute/Field Report/etc.), **Temperament** (Clerkly/Romantic/Philosophical), **Order focus** (1–3), **Regions** (secondary)&#x20;
* **Front matter** exactly per template (Roman numeral `phase`, arrays for `order_focus` & `regions`, `clerk_initials`), filename `phaseN-{type}-{slug}.md`&#x20;
* Body: `## Abstract` → `## Exhibits` (≥1 Clip with `|| … ||` and temperament-matched commentary) → `## Disposition` → `## Cross-References` (link to the slip you’re reacting to) &#x20;
* Maintain **bidirectional links** (Debate doc ↔ relevant Archive slip)&#x20;

**Definition of done**: valid front matter; at least one Clip; explicit Order focus; link back to at least one Archive slip.

---

# Master daily rhythm (team version)

1. **10–15 min stand-up** in your tracker: Engine posts which **Addendum seed(s)** are available for the day; others reply which seed they’re taking. (This enforces the site’s integration flow: scholarship → kit → archive → debate)&#x20;
2. **90 minutes build** (each role).
3. **30 minutes cross-link** (add hub links, related pages, footer cross-refs).
4. **10 minutes file hygiene** (naming, front matter validation).
5. **PR + quick review** (Conductor reviews; content peers sanity-check voice per section guidelines).

Conductor runs the dev server & checks nav after merges:

````bash
bundle exec jekyll serve
# visit /, /posts/, /romantic/, /ai-hermeneutics/, /archive/, /debate/
``` :contentReference[oaicite:36]{index=36}

---

# Guardrails & templates you’ll use constantly

- **Orders & Regions (copy/paste list)**: Boundary; Doubling; Craving; Silence & Withdrawal; Violence & Secret Life; Mediation & Aperture. Regions: Capital; Dens/Densmok; Quarry; North/Northo; Tower/Sticks; Dead River; Capeast :contentReference[oaicite:37]{index=37}  
- **Why Orders-first?** Because in Densworld, *mechanisms generate geographies*; devices like windows, maps, carts, puzzles, and carried flame **govern access** and create places; we file by what a doc **does**, then tag where it came from :contentReference[oaicite:38]{index=38} :contentReference[oaicite:39]{index=39}  
- **Clip Protocol 7.3** (Archive): Slip Code, Provenance, `|| clip ||`, Orders, Commentary (+ example) :contentReference[oaicite:40]{index=40}  
- **Debate voice**: choose **one** temperament per doc; rotate across the collection (Clerkly / Romantic / Philosophical) :contentReference[oaicite:41]{index=41}

---

# Week-1 queue (ready-to-ship titles, filenames, and seeds)

Each day, five new files (one per content role except the Conductor). All are grounded in the ore you provided and the training docs.

### Day 1
- **Engine (Post)**: *Edges to Edges: When Language Turns into Technique* → ends with seed **Order: Silence & Withdrawal; Region: Tower/Sticks** (catechism; quiet-hours) :contentReference[oaicite:42]{index=42} :contentReference[oaicite:43]{index=43}  
- **Romantic Kit**: `romantic-kit-organic-vs-mechanical-mini.md` — mini on form using two-rail; seed **Order: Boundary; Region: Quarry** (self-assembling wheel) :contentReference[oaicite:44]{index=44}  
- **AI Kit**: `ai-kit-author-function-in-practice.md` — short method page linking **Death of the Author**; seed **Order: Mediation & Aperture; Region: Capital** (window logic for text provenance) :contentReference[oaicite:45]{index=45}  
- **Archive**: `_archive/mediation-capital-window-caliper-a3.md` — “Capital: Window Calipers & Grit Distortion (inspection log)” with Clips on *no door; slips only* + tolerances (*Aperture as method*) :contentReference[oaicite:46]{index=46} :contentReference[oaicite:47]{index=47}  
- **Debate**: `_debate/phase4-ruling-window-and-stairs.md` — **Phase IV** Ruling (Clerkly): **Mediation & Aperture**—window/stair design is catalog-relevant; includes `|| No door; slips only. Stairs throttle crowds… ||` and links to the new A3 slip :contentReference[oaicite:48]{index=48}

### Day 2
- **Engine**: *Maps That Make Towns* → seed **Order: Mediation & Aperture + Doubling; Region: Dead River** (map installs town; maps beget maps) :contentReference[oaicite:49]{index=49}  
- **Romantic Kit**: `romantic-kit-technology-and-machine-mini.md` — “grit-screen” micro with seed **Mediation & Aperture; Regions: Capital ↔ Dens/Densmok** :contentReference[oaicite:50]{index=50}  
- **AI Kit**: `ai-kit-reading-dangerous-texts.md` — textual power & risk; method checklist; (Ricoeur/Gadamer framing already in kit) :contentReference[oaicite:51]{index=51} :contentReference[oaicite:52]{index=52}  
- **Archive**: `_archive/mediation-dead-river-map-installation-f3.md` — Clips from DR ore (“no river… map named it”) + commentary :contentReference[oaicite:53]{index=53}  
- **Debate**: `_debate/phase3-brief-map-without-river.md` — **Phase III** Brief (Philosophical): argue Orders-first via map/device logic; cross-ref Day-2 slip.

### Day 3
- **Engine**: *Counting-Five: Pattern Before Person* → seed **Order: Violence & Secret Life (cross Mediation); Regions: North↔Quarry** (pickbox + fivefold sightings) :contentReference[oaicite:54]{index=54} :contentReference[oaicite:55]{index=55}  
- **Romantic Kit**: `romantic-kit-authenticity-and-echoers.md` — authentication by echo; seed **Order: Doubling; Regions: North→Capital** (trial singers / deposition rule) :contentReference[oaicite:56]{index=56}  
- **AI Kit**: `ai-kit-interpretive-risk-and-answerability.md` — method for reading opaque systems; hub links.  
- **Archive**: `_archive/violence-north-murder-songs-e1.md` — murder-song index vs “missionary is the killer” margin; Order **Violence & Secret Life** :contentReference[oaicite:57]{index=57}  
- **Debate**: `_debate/phase2-case-pickbox-authorless-burden.md` — **Phase II** Case Note (Philosophical): cart as **aperture/method**; cross-link to pickbox Archive items :contentReference[oaicite:58]{index=58}

### Day 4
- **Engine**: *Respectable Commute → Secret Ledgers* → seed **Order: Violence & Secret Life; Region: Quarry** (public vs private appetite) :contentReference[oaicite:59]{index=59}  
- **Romantic Kit**: `romantic-kit-forms-that-teach.md` — “hands learn, voice recedes”; seed **Silence & Withdrawal; Region: Tower/Sticks** :contentReference[oaicite:60]{index=60}  
- **AI Kit**: `ai-kit-dialogue-vs-simulation.md` — living speech vs empty forms → method; cross-link to Romantic Kit.  
- **Archive**: `_archive/silence-sticks-withdrawal-register-i3.md` — intake cards (Cassie/E./Ria) Clips; commentary on practice-as-truth :contentReference[oaicite:61]{index=61} :contentReference[oaicite:62]{index=62}  
- **Debate**: `_debate/phase2-colloquy-on-withdrawal.md` — **Phase II** Colloquy (Romantic): defend “silence as method,” citing the new slip :contentReference[oaicite:63]{index=63}

### Day 5
- **Engine**: *Apertures Everywhere (Windows, Carts, Flames)* → seed **Mediation & Aperture** with cross-Order tags.  
- **Romantic Kit**: `romantic-kit-grammar-and-choice-mini.md` — quick two-rail drill; seed into Archive.  
- **AI Kit**: `ai-kit-reading-without-authors-checklist.md` (links to Death of the Author) :contentReference[oaicite:64]{index=64}  
- **Archive**: `_archive/mediation-dead-river-carried-flame-f4.md` — Yeller’s canistered fire as device passage :contentReference[oaicite:65]{index=65}  
- **Debate**: `_debate/phase4-hearing-on-cross-indexing-apertures.md` — **Phase IV** Hearing (Clerkly): mandate cross-indexing of device-threads; link to window, cart, flame slips.

> If you want more seeds: Toolbox & exemplar Clips are summarized in the Archive aggregator (pickbox cart; roads that bud; fivefold; “edges to edges”; Capital window/stairs; Dead River map & flame) with Order hints you can lift directly :contentReference[oaicite:66]{index=66} :contentReference[oaicite:67]{index=67}.

---

# Conductor’s (Structure) daily loop

- **Build & link health**: run `jekyll serve`; scan home tiles → hubs → individual items per collection; confirm permalinks render (Posts, Kits, Archive, Debate) :contentReference[oaicite:68]{index=68}  
- **Front-matter lint pass**:  
  - Posts: pattern `_posts/YYYY-MM-DD-post-[n].md` + `layout: post` :contentReference[oaicite:69]{index=69}  
  - Romantic/AI Kits: `layout: kit` + `kit_type` set; ensure back-link pill to hub :contentReference[oaicite:70]{index=70}  
  - Archive: filenames Order-first + required fields; 3-section body present; Protocol 7.3 Clips present :contentReference[oaicite:71]{index=71} :contentReference[oaicite:72]{index=72}  
  - Debate: filename pattern + front-matter correctness (Roman numeral `phase`, arrays, `clerk_initials`) :contentReference[oaicite:73]{index=73}  
- **Bidirectional links**: ensure Debate ↔ Archive footers exist per doc (small footer line is fine) :contentReference[oaicite:74]{index=74}  
- **Navigation & hubs**: confirm each new file appears where expected (posts index, kit hubs, archive hub per Order, debate hub per Phase) :contentReference[oaicite:75]{index=75}  
- **Style gate**: out-of-character voice in Posts/Kits; in-character in Archive/Debate (don’t mix) :contentReference[oaicite:76]{index=76}

---

# Coordination rules you all agree to

1) **One seed, many realizations.** Every Engine post and each Kit page ends with a seed (Orders + Region). At least one of those seeds must be *actioned the same day* by Slipwright or Debate Clerk (preferably both). This keeps the ecosystem wired :contentReference[oaicite:77]{index=77}.

2) **Orders-first discipline.** Slipwright always files by Order first; Debate documents defend/contest that method across phases. Use canonical lists while classifying :contentReference[oaicite:78]{index=78} :contentReference[oaicite:79]{index=79}.

3) **Clips or it didn’t happen.** Archive and Debate both show evidence via Clips (`|| … ||`), preserving contradictions; that’s not a bug—it’s evidence :contentReference[oaicite:80]{index=80} :contentReference[oaicite:81]{index=81}.

4) **Bidirectional links.** Any Debate doc that cites an Archive slip must link to it; that slip should add a footer link back to the Debate doc (Conductor enforces weekly) :contentReference[oaicite:82]{index=82}.

5) **Voice boundaries.** Posts/Kits are out-of-character; Archive/Debate are in-character institutional voices; keep them distinct (Conductor flags violations) :contentReference[oaicite:83]{index=83}.

---

## Quick ore-to-page cheat sheet (copy this when you’re stuck)

- **Pickbox cart** → Archive: **Mediation & Aperture** (traveling aperture) + cross **Doubling/Violence**; Debate Phase II case on “authorless burden” :contentReference[oaicite:84]{index=84} :contentReference[oaicite:85]{index=85}  
- **“Edges to edges”** puzzle drill → Archive: **Silence & Withdrawal** (speech installs method; hand keeps it) → Debate Phase II colloquy on withdrawal :contentReference[oaicite:86]{index=86} :contentReference[oaicite:87]{index=87}  
- **Map that makes a town** (Dead River) → Archive: **Mediation & Aperture + Doubling**; Debate Phase III brief on Orders-first filing :contentReference[oaicite:88]{index=88}  
- **Counting-five / fivefold silhouettes** → Archive: **Doubling / Violence & Secret Life**; Debate Phase II note on pattern vs person :contentReference[oaicite:89]{index=89} :contentReference[oaicite:90]{index=90}

---

If you adopt these handles, checklists, and the Week-1 queue, you’ll be shipping 25 coherent files across five days while keeping the structure sane. The site’s architecture was built to support exactly this kind of **integrated daily production**—posts seed, kits formalize, archive realizes, debate reflects—so use it! :contentReference[oaicite:91]{index=91}
````