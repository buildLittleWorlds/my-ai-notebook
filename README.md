# Professor Plate's Notebook - Jekyll Site Documentation

## Overview

This is a Jekyll-powered academic blog focused on literary theory, hermeneutics, and critical analysis. The site combines traditional blog posts with specialized theoretical frameworks ("kits") and an innovative fictional archive system ("notebooks"). It serves as both a scholarly resource and a creative exploration of archival practices and interpretive methods.

## Site Structure & Four Main Sections

### 1. **Blog Posts** (`_posts/` collection)
- **Purpose**: Traditional academic blog posts containing essays, arguments, and notes in progress
- **Content**: Literary criticism, theoretical discussions, methodological explorations
- **Layout**: Uses `post` layout
- **URL Pattern**: `/:title/`
- **File Pattern**: `_posts/post-[number].md`
- **Front Matter**: 
  ```yaml
  layout: post
  title: "Post Title"
  post_number: [integer]
  ```
- **Navigation**: Accessible via main homepage tile and `/posts/` page

### 2. **Kits** (`_kits/` collection) - Theoretical Frameworks
Two main kit systems providing interpretive frameworks:

#### A. **Romantic Quick Kit** (`/romantic-quick-kit/`)
- **Purpose**: Method and key concepts for reading Romanticism
- **Hub File**: `_kits/romantic-quick-kit.md` (uses `kit-hub` layout)
- **Individual Pages**: `romantic-kit-[topic].md` files covering:
  - Hermeneutics (reading method)
  - Authenticity (self & sincerity)
  - Organic form (art, nature, unity)
  - Technology & the machine
  - Historical contexts (Germany, England, America)
  - Glossary of terms

#### B. **AI Hermeneutics Kit** (`/ai-hermeneutics-kit/`)
- **Purpose**: Framework for interpreting AI-generated texts
- **Hub File**: `_kits/ai-hermeneutics-kit.md` (uses `kit-hub` layout)  
- **Individual Pages**: `ai-kit-[topic].md` files covering:
  - Theoretical foundations (author-function, interpretive dialogue, dangerous texts)
  - Deleuze applications (goodwill, forces, assemblages, monotony)
  - Butler frameworks (performativity, interiority, parody, regulation)
  - Additional frameworks (distanciation, death of author, genealogy)
  - Glossary and reference materials

**Kit Technical Details**:
- **Layouts**: `kit-hub` for main pages, `kit` for individual pages
- **URL Pattern**: `/kits/:name/`
- **Cross-linking**: Extensive internal linking between related concepts
- **Style**: Academic but accessible, with practical reading applications

### 3. **Quarry Notebooks** (`_notebooks/` collection) - The Archive System
A fictional but rigorous archival system presenting fragments and testimonies organized by interpretive "Orders" rather than geography.

#### **Archival Concept**:
- **Premise**: Documents from various regions (Dens, Quarry, Capital, North Town, etc.) filed by what reality they perform rather than geographic origin
- **Structure**: Each entry is a "slip" with catalog code, provenance, extract, and commentary
- **Voice**: Archivists analyzing and categorizing found materials

#### **The Six Orders** (Primary Classification System):
1. **Boundary** - Where edges blur between forms (town/wilderness, categories)
2. **Doubling** - Replication, copies, journeys within journeys, originals without origin
3. **Craving** - Desire as generative force, drives, appetites, proliferations  
4. **Silence & Withdrawal** - Where speech collapses, truth through quiet practice
5. **Violence & Secret Life** - Parallel ledgers of harm and hidden motives
6. **Mediation & Aperture** - Windows, devices, how the world is constrained by how it's seen

#### **Geographic Regions** (Secondary Classification):
- **Capital** - Bureaucratic center, licensing, formal procedures
- **Dens/Densmok** - Edge settlements, wilderness boundaries
- **Quarry** - Source of materials, journeys, multiplicities
- **North Town/Northo** - Murder songs, secret lives, doubled identities
- **Tower/Sticks** - Withdrawal practices, catechisms, clinic work
- **Dead River** - Counting systems, numerical mysteries
- **Capeast** - Festival sites, women's arrival stories

#### **Entry Format**:
```yaml
---
title: "Archive Post [CODE] — [REGION]: [TITLE] ([DOCUMENT TYPE])"
order: "[ONE OF SIX ORDERS]"
region: "[GEOGRAPHIC REGION]"  
catalog_code: "[ALPHANUMERIC CODE]"
excerpt: "[KEY QUOTE FROM COMMENTARY]"
---

**Catalog Code:** [CODE]

## Provenance
[Source information, how document was acquired]

## Extract
[Quoted material from original documents, often in blockquotes]

## Archivist's Commentary  
[Interpretive analysis of why this fits the assigned Order]
```

### 4. **Debate Collection** (`_debate/` collection) - Archival History
- **Purpose**: Documents the internal debate about how to organize the archive
- **Main File**: `_debate/archivists-debate.md`
- **Content**: Four phases of archival reorganization:
  - Phase I: Regional Drawers (geographic filing)
  - Phase II: Faults in Geography (problems with regional system)
  - Phase III: Orders Proposal (introduction of the six Orders)
  - Phase IV: Implementation & Objections (ongoing tensions)
- **Central Question**: Does the archive mirror world structure or shape it through language?

## Technical Implementation

### Jekyll Configuration
- **Jekyll Version**: 3.9.5 (GitHub Pages compatible)
- **Theme**: Custom layouts and styling
- **Plugins**: jekyll-feed, jekyll-seo-tag, jekyll-sitemap
- **Baseurl**: `/my-ai-notebook` (for GitHub Pages)

### Collections Setup (`_config.yml`):
```yaml
collections:
  kits:
    output: true
    permalink: /kits/:name/
  notebooks:
    output: true  
    permalink: /notebooks/:name/
  debate:
    output: true
    permalink: /debate/:name/
```

### Layout System
- **`default.html`** - Base layout with navigation
- **`home.html`** - Homepage with four main tiles
- **`post.html`** - Individual blog posts
- **`posts-list.html`** - Blog post index
- **`kit-hub.html`** - Main kit pages (romantic/AI)
- **`kit.html`** - Individual kit pages
- **`notebooks-hub.html`** - Notebooks index (auto-generates from collection)
- **`notebook.html`** - Individual notebook entries
- **`debate.html`** - Debate documents

### Navigation Structure
Homepage (`/`) provides four main entry points:
1. Blog Posts → `/posts/` → individual posts
2. Romantic Quick Kit → `/romantic-quick-kit/` → individual romantic kit pages  
3. AI Hermeneutics Kit → `/ai-hermeneutics-kit/` → individual AI kit pages
4. Quarry Notebooks → `/notebooks/` → individual notebook entries + `/archivists-debate/`

### Development Workflow
```bash
# Install dependencies
bundle install

# Run development server  
bundle exec jekyll serve
# Site available at: http://127.0.0.1:4000/my-ai-notebook/

# Build for production
bundle exec jekyll build
```

## Content Philosophy & Style

### Academic Approach
- **Scholarly but accessible** - Complex theory made readable
- **Practical application** - Frameworks designed for actual use in reading
- **Cross-disciplinary** - Combines literary theory, philosophy, media studies

### Fictional Archive Approach  
- **Rigorous methodology** - Archive follows consistent internal logic
- **Interpretive focus** - Documents classified by what they *do* not just what they *are*
- **Fragmented narrative** - Story emerges through archival organization
- **Meta-archival** - Self-conscious about how classification systems shape meaning

### Voice & Tone
- **Blog Posts**: First person, reflective, work-in-progress
- **Kit Pages**: Instructional, systematic, practical
- **Notebook Entries**: Archival voice, analytical, preserving ambiguity
- **Overall**: Serious scholarly work with creative formal innovation

## File Organization
```
/
├── _config.yml           # Jekyll configuration
├── _layouts/             # HTML templates  
├── _includes/            # Reusable components
├── _posts/               # Blog posts (110+ files)
├── _kits/                # Theoretical frameworks (27+ files)
├── _notebooks/           # Archive entries (18+ files)
├── _debate/              # Archival methodology debates
├── index.md              # Homepage
├── posts.md              # Blog index
├── notebooks.md          # Archive index  
├── style.css             # Custom styling
├── Gemfile               # Ruby dependencies
└── backup-files-for-pre-jekyll-blog/ # Legacy HTML files
```

## Usage for LLM Analysis

When analyzing individual pages, consider:

1. **Collection Context** - Which of the four main sections does this belong to?
2. **Internal Logic** - How does this fit the established voice and methodology?
3. **Cross-References** - What connections exist to other parts of the site?
4. **Functional Role** - Is this instructional (kits), reflective (posts), analytical (notebooks), or meta-critical (debate)?

The site works as an integrated system where blog posts develop ideas that become formalized in kits, which provide frameworks for analyzing the kind of fragmented materials preserved in the notebooks, while the debate documents reflect on the whole enterprise.