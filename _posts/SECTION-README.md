# Blog Posts Collection — Section Guide

## Purpose & Role in Site Structure

**Blog Posts** are the **out-of-character academic writing** on this site. This is where Professor Plate shares real thoughts, arguments, and work-in-progress reflections on literary theory, AI, hermeneutics, and critical analysis.

### Position in Site Ecosystem:
1. **Blog Posts** ← *You are here* (real-world essays, out-of-character)
2. **Romantic Quick Kit** (real theory, out-of-character)  
3. **AI Hermeneutics Kit** (real theory, out-of-character)
4. **The Archive** (fictional Densworld documents, in-character)
5. **The Debate** (fictional Densworld meta-discussion, in-character)

## Writing Voice & Style

- **First person**: "I think," "This puzzles me," "I've been wondering"
- **Reflective and provisional**: Work-in-progress, questions in development
- **Academic but accessible**: Complex ideas in readable prose
- **Conversational**: Direct address to readers, informal asides

## Content Guidelines

### What Belongs Here:
- Literary theory arguments and explorations
- Reflections on AI and interpretation
- Methodological questions about reading
- Academic observations and hypotheses
- Personal scholarly journey documentation

### What Does NOT Belong Here:
- Fictional archive materials (those go in `_archive/`)
- Systematic theory frameworks (those go in `_romantic/` or `_ai_hermeneutics/`)
- Meta-discussions about archival practices (those go in `_debate/`)

## Technical Specifications

### File Naming Convention:
```
2024-MM-DD-post-[number].md
```
Example: `2024-01-05-post-4.md`

### Required Front Matter:
```yaml
---
layout: post
title: "Post Title"
post_number: [integer]
date: 2024-01-02 10:00:00 -0500
---
```

### Navigation:
- Accessible from homepage tile "Blog Posts"
- Listed on `/posts/` index page  
- Individual URLs: `/:title/`

## Relationship to Other Collections

### From Blog Posts → Theory Collections:
Ideas developed in blog posts often get formalized into systematic frameworks in the two theory collections:
- Complex arguments about Romanticism → `_romantic/` kit pages
- Ideas about AI interpretation → `_ai_hermeneutics/` kit pages

### From Blog Posts → Fictional Collections:
Blog post insights may inspire fictional archive scenarios, but the collections remain separate:
- Theoretical insights about classification → fictional `_debate/` documents
- Ideas about interpretation → fictional `_archive/` entries

## Current Status

- **110+ posts** covering literary criticism, AI theory, methodological questions
- **Chronological organization** by publication date
- **Thematic coherence** around hermeneutics and critical theory

This collection serves as the foundational voice of the site—the real academic thinking that grounds both the theoretical frameworks and fictional explorations found elsewhere.