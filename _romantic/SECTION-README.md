# Romantic Collection — Section Guide

## Purpose & Role in Site Structure

**Romantic Quick Kit** is a **real theoretical framework** (out-of-character) providing systematic methods and concepts for reading Romantic literature and thought. This is academic theory designed for practical application.

### Position in Site Ecosystem:
1. **Blog Posts** (real-world essays, out-of-character)
2. **Romantic Quick Kit** ← *You are here* (real theory, out-of-character)  
3. **AI Hermeneutics Kit** (real theory, out-of-character)
4. **The Archive** (fictional Densworld documents, in-character)
5. **The Debate** (fictional Densworld meta-discussion, in-character)

## Framework Structure

### Hub Pages:
- **Landing page**: `/romantic/` (basic introduction)
- **Main hub**: `romantic-quick-kit.md` (comprehensive framework overview with links)

### Component Pages (9 total):
- `romantic-kit-hermeneutics.md` — Core interpretive method
- `romantic-kit-authenticity.md` — The evidenced 'self'
- `romantic-kit-organic-form.md` — Art, nature, and unity
- `romantic-kit-contexts-germany.md` — German philosophical foundations
- `romantic-kit-contexts-england.md` — English literary developments  
- `romantic-kit-contexts-america.md` — American adaptations
- `romantic-kit-glossary.md` — Key terms and concepts

## Writing Voice & Style

- **Instructional and systematic**: "How to read for..." "Apply this method by..."
- **Academic but practical**: Complex theory made usable
- **Definitive**: Presents established frameworks rather than open questions
- **Cross-referenced**: Extensive internal linking between concepts

## Content Guidelines

### Core Method: Two-Rail Hermeneutics
All pages build on the fundamental interpretive approach:
- **Psychological side**: The work's unique pattern of choices
- **Grammatical side**: The conventions it engages with
- **Authenticity**: Demonstrable coherence between the two

### Key Concepts Covered:
- **Authenticity** as aesthetic achievement, not confession
- **Organic Form** as self-generated structure
- **Gefühl** as pre-reflective awareness
- **National contexts** shaping different Romantic expressions
- **Historical development** from German philosophy to literary practice

### What Belongs Here:
- Systematic theoretical frameworks for reading Romanticism
- Practical interpretive methods and applications
- Historical context and development of Romantic thought
- Cross-references to specific texts and examples

### What Does NOT Belong Here:
- Work-in-progress reflections (those go in `_posts/`)
- AI-specific interpretive methods (those go in `_ai_hermeneutics/`)
- Fictional applications or examples (those stay out of theory collections)

## Technical Specifications

### File Naming:
```
romantic-kit-[topic].md
romantic-quick-kit.md (main hub)
```

### Required Front Matter:
```yaml
---
layout: kit
title: "Page Title"
kit_type: romantic
---
```

### Navigation Structure:
- Homepage tile → `/romantic/` landing → `romantic-quick-kit.md` hub → individual pages
- Each page includes "Back to Quick Kit Menu" navigation
- URLs: `/romantic/:name/`

### Cross-Reference Linking:
Use Jekyll's relative_url filter for all internal links:
```markdown
[link text]({{ '/romantic/romantic-kit-topic/' | relative_url }})
```

## Relationship to Other Collections

### From Blog Posts → Romantic Kit:
Blog post explorations of Romantic themes get formalized into systematic kit pages

### Romantic Kit → AI Hermeneutics Kit:
Some interpretive methods developed for Romantic texts are adapted for AI analysis

### Theory Collections ≠ Fictional Collections:
The Romantic Kit provides real academic frameworks. It does NOT contain fictional applications or examples from Densworld.

## Current Status

- **9 component pages** providing comprehensive Romantic theory toolkit
- **Fully cross-linked** with extensive internal navigation
- **Practical focus** on interpretive application rather than historical survey
- **National contexts** balanced with universal principles

This collection serves as a systematic theoretical resource, complementing the exploratory voice of blog posts and providing analytical tools applicable to both traditional texts and contemporary interpretation challenges.