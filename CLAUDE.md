# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-powered academic blog called "Professor Plate's Notebook" focused on literary theory, hermeneutics, and critical analysis. The site combines traditional blog posts with specialized theoretical frameworks ("kits") and an innovative fictional archive system organized by interpretive "Orders."

## Development Commands

### Local Development
```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve
# Site available at: http://127.0.0.1:4000/my-ai-notebook/

# Build for production
bundle exec jekyll build
```

### Content Aggregation
The site includes scripts to aggregate content from each collection into single files for analysis:

```bash
# Run all aggregation scripts at once
./run-all-aggregators.sh

# Run individual aggregation scripts
./aggregate-structural-files.sh
./_posts/aggregate-blog-posts.sh
./_romantic/aggregate-romantic-kit.sh
./_ai_hermeneutics/aggregate-ai-hermeneutics.sh
./_archive/aggregate-archive.sh
./_debate/aggregate-archivists-debate.sh
```

All aggregated files are output to `aggregated-md-files/` directory.

### GitHub Pages Deployment
This site is configured for GitHub Pages deployment with baseurl `/my-ai-notebook`. The site builds automatically on push to the main branch.

## Site Architecture

### Five Main Collections

1. **Posts** (`_posts/`) - Traditional academic blog posts (112 files)
2. **Romantic** (`_romantic/`) - Romantic theory framework (11 components)
3. **AI Hermeneutics** (`_ai_hermeneutics/`) - AI interpretation framework (20 components)
4. **Archive** (`_archive/`) - Fictional archive entries organized by six interpretive "Orders" (20 files)
5. **Debate** (`_debate/`) - Meta-archival methodology discussions (22 files)

### Collection Configuration
- **Romantic**: `/romantic/:name/` - Romantic theory components with hub page at `/romantic/romantic-quick-kit/`
- **AI Hermeneutics**: `/ai-hermeneutics/:name/` - AI hermeneutics components with hub page at `/ai-hermeneutics/ai-hermeneutics-kit/`
- **Archive**: `/archive/:name/` - Archive entries accessible via `/archive/` hub
- **Debate**: `/debate/:name/` - Archival methodology documents accessible via `/debate/archivists-debate/`
- **Posts**: `/:title/` - Blog posts accessible via `/posts/`

### Layout System
- `default.html` - Base layout with site header/footer and conditional navigation
- `home.html` - Homepage with three grouped section tiles
- `post.html` - Blog post layout
- `posts-list.html` - Blog index
- `kit.html` - Individual kit pages (both romantic and AI hermeneutics)
- `archive-hub.html` - Archive index with auto-generated Order listings
- `archive.html` - Individual archive entries
- `debate.html` - Debate documents

## Content Structure

### Homepage Structure (Three Grouped Sections)

**Writing Section:**
- Single tile: Blog Posts → `/posts/` (112 posts)

**Theoretical Frameworks Section (Paired Tiles):**
- Romantic Quick Kit → `/romantic/` → detailed hub at `/romantic/romantic-quick-kit/`
- AI Hermeneutics Kit → `/ai-hermeneutics/` → detailed hub at `/ai-hermeneutics/ai-hermeneutics-kit/`

**Archive System Section (Paired Tiles):**
- The Archive → `/archive/` → entries organized by six interpretive Orders
- The Debate of the Archivists → `/debate/` → methodology documents in chronological phases

### Archive System (Archive Collection)
The archive implements a fictional archive organized by six interpretive "Orders":

1. **Boundary** - Where edges blur between forms
2. **Doubling** - Replication, copies, journeys within journeys
3. **Craving** - Desire as generative force
4. **Silence & Withdrawal** - Where speech collapses
5. **Violence & Secret Life** - Parallel ledgers of harm
6. **Mediation & Aperture** - How the world is constrained by perception

Each entry follows strict formatting with catalog codes, provenance, extracts, and archivist commentary.

### Theoretical Framework System
Two comprehensive theoretical frameworks organized as separate collections:
- **Romantic Collection** (`_romantic/`) - Method and concepts for reading Romanticism (11 components)
- **AI Hermeneutics Collection** (`_ai_hermeneutics/`) - Framework for interpreting AI-generated texts (20 components)

Each collection includes a hub page that links to detailed individual concept pages.

## Technical Details

### Jekyll Configuration
- Uses GitHub Pages gem with Jekyll 3.9.x compatibility
- Uses kramdown with GFM input
- Custom permalink structure
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-sitemap

### Styling
- Custom CSS with Space Mono monospace font
- Responsive design with clean academic aesthetics
- Located in `style.css` at project root

### Navigation Flow
- Homepage presents three grouped sections (Writing, Theoretical Frameworks, Archive System)
- Landing pages for each collection provide simple overviews
- Detailed hub pages within collections have extensive cross-linking
- Individual pages include back-to-hub navigation

## Content Guidelines

### Voice and Style
- **Posts**: First person, reflective, work-in-progress
- **Romantic**: Instructional, systematic, practical application focus for Romantic theory
- **AI Hermeneutics**: Instructional, systematic, practical application focus for AI interpretation
- **Archive**: Archival voice, analytical, preserving ambiguity
- **Debate**: Meta-critical, methodological discussions

### File Naming Conventions
- Posts: `post-[number].md`
- Romantic: `romantic-kit-[topic].md` or `romantic-quick-kit.md` for hub
- AI Hermeneutics: `ai-kit-[topic].md` or `ai-hermeneutics-kit.md` for hub
- Archive: `[order]-[region]-[descriptive-slug]-[code].md`
- Debate: `phase[N]-[type]-[descriptive-slug].md`
- Use lowercase, hyphens for spaces

## Debate Documents Workflow

### Adding New Debate Documents
When given markdown files in the `_debate/` collection with missing or incomplete frontmatter, follow this standardized workflow:

#### 1. Analyze Document Content
- **Phase Classification** (determines where it links from hub):
  - **Phase I** (Years 1-12): Regional filing system establishment
  - **Phase II** (Years 13-20): Geographic system failures
  - **Phase III** (Year 22): Orders proposal and debate
  - **Phase IV** (Year 23+): Implementation and objections

- **Document Type**: Memo, Minute, Field Report, Colloquy Note, Counter-Memo, Directive, Hearing, Ruling, Brief, Case Note

- **Order Focus**: Which of the six Orders the document addresses:
  - Boundary, Doubling, Craving, Silence & Withdrawal, Violence & Secret Life, Mediation & Aperture
  - Use "n/a" for Phase I docs or docs arguing against Orders

#### 2. Add Required Jekyll Frontmatter
```yaml
---
title: "Document Title (match content exactly)"
phase: "Phase [Roman] — [Description]"
doc_type: "[Document Type]"
order_focus: ["Order1", "Order2"] # array, or "n/a"
regions: ["Region1", "Region2"] # relevant geographic areas
archive_date: "Year [N], Q[N]"
date: 2024-01-01 # leave as standard
clerk_initials: "[Initials]" # from document author
status: "[Adopted/Filed/Canonical/etc]" # from document
excerpt: "Brief description of document's significance"
permalink: /debate/[filename-slug]/
---
```

#### 3. Update Navigation Hub
Add or update links in `/debate/archivists-debate.md` in the appropriate Phase section:

```markdown
- **[Document Title]({{ '/debate/filename-slug/' | relative_url }})**  
  *brief description of content and significance*
```

**Critical**: Always use `{{ '/debate/path/' | relative_url }}` filter for all links to ensure GitHub Pages compatibility.

#### 4. File Naming
- Use existing filename or follow pattern: `phase[N]-[type]-[descriptive-slug].md`
- Ensure permalink matches filename exactly

### Hub Page Structure
The main debate hub (`/_debate/archivists-debate.md`) organizes documents by four chronological phases. Each phase should have key documents that demonstrate the evolution of archival policy and the ongoing tension between regional vs. Orders-based filing.

### Integration Points
- Cross-reference debate documents with archive entries that use the Orders
- Ensure theoretical consistency between debate rationales and archive classifications
- Maintain the fictional "institutional voice" throughout all debate documents

## System Integration

The site functions as an integrated system where:
- Blog posts develop ideas that become formalized in theoretical frameworks
- Theoretical frameworks (romantic and AI hermeneutics collections) provide methods for analyzing materials
- Archive preserves materials using the interpretive Orders system
- Debate documents explain the methodology behind the archive's organization

This creates a self-referential academic ecosystem that demonstrates both the theory and practice of literary-critical methodology.