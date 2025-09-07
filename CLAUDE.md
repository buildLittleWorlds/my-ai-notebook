# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-powered academic blog called "Professor Plate's Notebook" focused on literary theory, hermeneutics, and critical analysis. The site combines traditional blog posts with specialized theoretical frameworks ("kits") and an innovative fictional archive system ("notebooks").

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

### GitHub Pages Deployment
This site is configured for GitHub Pages deployment with baseurl `/my-ai-notebook`. The site builds automatically on push to the main branch.

## Site Architecture

### Four Main Collections
1. **Posts** (`_posts/`) - Traditional academic blog posts (110+ files)
2. **Kits** (`_kits/`) - Theoretical frameworks: Romantic Quick Kit and AI Hermeneutics Kit (27+ files)  
3. **Notebooks** (`_notebooks/`) - Fictional archive entries organized by six interpretive "Orders" (18+ files)
4. **Debate** (`_debate/`) - Meta-archival methodology discussions

### Collection Configuration
- **Kits**: `/kits/:name/` - Individual framework pages with hub pages at `/romantic-quick-kit/` and `/ai-hermeneutics-kit/`
- **Notebooks**: `/notebooks/:name/` - Archive entries accessible via `/notebooks/` hub
- **Debate**: `/debate/:name/` - Archival methodology documents
- **Posts**: `/:title/` - Blog posts accessible via `/posts/`

### Layout System
- `default.html` - Base layout with site header/footer and conditional navigation
- `home.html` - Homepage with four main section tiles
- `post.html` - Blog post layout
- `posts-list.html` - Blog index
- `kit-hub.html` - Main kit landing pages
- `kit.html` - Individual kit pages  
- `notebooks-hub.html` - Archive index with auto-generated listings
- `notebook.html` - Individual archive entries
- `debate.html` - Debate documents

## Content Structure

### Archive System (Notebooks Collection)
The notebooks implement a rigorous fictional archive organized by six interpretive "Orders":
1. **Boundary** - Where edges blur between forms
2. **Doubling** - Replication, copies, journeys within journeys  
3. **Craving** - Desire as generative force
4. **Silence & Withdrawal** - Where speech collapses
5. **Violence & Secret Life** - Parallel ledgers of harm
6. **Mediation & Aperture** - How the world is constrained by perception

Each entry follows strict formatting with catalog codes, provenance, extracts, and archivist commentary.

### Kit System
Two comprehensive theoretical frameworks:
- **Romantic Quick Kit** - Method and concepts for reading Romanticism
- **AI Hermeneutics Kit** - Framework for interpreting AI-generated texts

Both include hub pages that link to detailed individual concept pages.

## Technical Details

### Jekyll Configuration
- Jekyll 3.9.5 (GitHub Pages compatible)
- Uses kramdown with GFM input
- Custom permalink structure
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-sitemap

### Styling
- Custom CSS with Space Mono monospace font
- Responsive design with clean academic aesthetics
- Located in `style.css` at project root

### Navigation
Homepage provides four main tiles leading to each collection. Kit hub pages have extensive cross-linking between related concepts.

## Content Guidelines

### Voice and Style
- **Posts**: First person, reflective, work-in-progress
- **Kits**: Instructional, systematic, practical application focus
- **Notebooks**: Archival voice, analytical, preserving ambiguity
- **Debate**: Meta-critical, methodological discussions

### File Naming Conventions
- Posts: `post-[number].md`
- Kits: `[kit-name]-kit-[topic].md`
- Notebooks: `archivist-[letter][number].md`
- Use lowercase, hyphens for spaces

The site functions as an integrated system where blog posts develop ideas that become formalized in kits, which provide frameworks for analyzing materials preserved in the notebooks.