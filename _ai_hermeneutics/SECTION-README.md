# AI Hermeneutics Collection — Section Guide

## Purpose & Role in Site Structure

**AI Hermeneutics Kit** is a **real theoretical framework** (out-of-character) providing systematic methods for interpreting AI-generated texts. This builds on traditional hermeneutics to address new interpretive challenges posed by algorithmic authorship.

### Position in Site Ecosystem:
1. **Blog Posts** (real-world essays, out-of-character)
2. **Romantic Quick Kit** (real theory, out-of-character)  
3. **AI Hermeneutics Kit** ← *You are here* (real theory, out-of-character)
4. **The Archive** (fictional Densworld documents, in-character)
5. **The Debate** (fictional Densworld meta-discussion, in-character)

## Framework Structure

### Hub Pages:
- **Landing page**: `/ai-hermeneutics/` (basic introduction)
- **Main hub**: `ai-hermeneutics-kit.md` (comprehensive framework overview with links)

### Component Pages (18 total):

#### Theoretical Foundations (4 pages):
- `ai-kit-author-function.md` — From Romantic soul to algorithmic system
- `ai-kit-interpretive-dialogue.md` — When the text reads the reader
- `ai-kit-dangerous-book.md` — Texts that transform and transgress
- `ai-kit-hermeneutics-of-risk.md` — New forms of dialogue and danger

#### Deleuzian Applications (4 pages):
- `ai-kit-deleuze-goodwill.md` — The text as Deleuzian machine
- `ai-kit-deleuze-forces.md` — Active vs. reactive diagnostic for AI
- `ai-kit-deleuze-monotony.md` — AI as monstrous monotony
- `ai-kit-deleuze-assemblage.md` — Human-AI desiring-machine

#### Butlerian Frameworks (4 pages):
- `ai-kit-butler-performativity.md` — AI as performative subject
- `ai-kit-butler-interiority.md` — Surface of soul, illusion of depth
- `ai-kit-butler-parody.md` — Copy of copy, end of original
- `ai-kit-butler-regulation.md` — Coherent author as regulatory fiction

#### Additional Frameworks (6 pages):
- `ai-kit-distanciation.md` — Critical distance in AI interpretation
- `ai-kit-death-of-author.md` — Algorithmic death, interpretive birth
- `ai-kit-genealogy.md` — Tracing AI discourse formations
- Plus glossary and reference materials

## Writing Voice & Style

- **Systematic and instructional**: Building coherent analytical frameworks
- **Theoretically rigorous**: Drawing on established critical theory
- **Practically oriented**: Designed for actual interpretive application
- **Cross-disciplinary**: Integrating philosophy, literary theory, media studies

## Content Guidelines

### Central Argument:
AI interpretive challenges are **intensifications** of existing hermeneutical questions, not entirely new problems. Traditional critical theory provides applicable frameworks when properly adapted.

### Key Theoretical Sources:
- **Foucault**: Author-function, genealogy, discourse analysis
- **Gadamer**: Interpretive dialogue, horizon-fusion, risk
- **Deleuze & Guattari**: Machines, assemblages, forces, monotony
- **Judith Butler**: Performativity, interiority, parody, regulation
- **Ricoeur**: Distanciation, text autonomy

### What Belongs Here:
- Systematic frameworks for interpreting AI-generated texts
- Adaptations of traditional hermeneutics for algorithmic authorship
- Theoretical foundations for AI text analysis
- Cross-references between different critical approaches
- Practical interpretive methods and applications

### What Does NOT Belong Here:
- Work-in-progress reflections (those go in `_posts/`)
- Romanticism-specific methods (those go in `_romantic/`)
- Fictional applications or Densworld examples (those stay out of theory)

## Technical Specifications

### File Naming:
```
ai-kit-[topic].md
ai-kit-[theorist]-[concept].md
ai-hermeneutics-kit.md (main hub)
```

### Required Front Matter:
```yaml
---
layout: kit
title: "Page Title with Subtitle"
kit_type: ai_hermeneutics
---
```

### Navigation Structure:
- Homepage tile → `/ai-hermeneutics/` landing → `ai-hermeneutics-kit.md` hub → individual pages
- Organized by theoretical approach (foundations, Deleuze, Butler, etc.)
- URLs: `/ai-hermeneutics/:name/`

### Cross-Reference Linking:
Use Jekyll's relative_url filter for all internal links:
```markdown
[link text]({{ '/ai-hermeneutics/ai-kit-topic/' | relative_url }})
```

## Relationship to Other Collections

### From Blog Posts → AI Hermeneutics Kit:
Exploratory blog posts about AI interpretation get systematized into comprehensive kit pages

### Romantic Kit ↔ AI Hermeneutics Kit:
Some interpretive principles adapt between traditional and AI texts, others require fundamental reconceptualization

### Theory Collections ≠ Fictional Collections:
This provides real academic frameworks for AI interpretation. It does NOT contain fictional examples or Densworld applications.

## Current Status

- **18 component pages** providing comprehensive AI interpretation toolkit
- **Multi-theoretical approach** integrating diverse critical frameworks
- **Practical focus** on interpretive application
- **Historically grounded** while addressing contemporary challenges

This collection serves as the site's most systematic theoretical contribution—a coherent framework for interpreting texts in the age of algorithmic authorship, grounded in traditional hermeneutics but responsive to new interpretive challenges.