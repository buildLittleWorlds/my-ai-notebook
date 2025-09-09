# Debate Collection — Section Guide

## Purpose & Role in Site Structure

**The Debate of the Archivists** contains **fictional meta-documents** (in-character) about how to organize the Archive. These are institutional memoranda, meeting minutes, and policy documents that reveal the ongoing tension between different archival philosophies within Densworld.

### Position in Site Ecosystem:
1. **Blog Posts** (real-world essays, out-of-character)
2. **Romantic Quick Kit** (real theory, out-of-character)  
3. **AI Hermeneutics Kit** (real theory, out-of-character)
4. **The Archive** (fictional Densworld documents, in-character)
5. **The Debate** ← *You are here* (fictional Densworld meta-discussion, in-character)

### Functional Separation Within Densworld:
- **The Archive** (`_notebooks/`) = Primary documents being filed and studied
- **The Debate** (`_debate/`) = Institutional discussions about how to organize those documents

This separation creates a richer fictional world where readers can experience both the raw materials and the "behind-the-scenes" curatorial process.

## Institutional Drama Structure

### The Central Question:
*Does the archive mirror the world's structure, or does the archive's language help shape it?*

### Four-Phase Historical Development:

#### **Phase I (Years 1-12): Regional Drawers**
- **System**: Geographic filing by region (Dens, Capital, Quarry, etc.)
- **Status**: Initial establishment, seemingly working
- **Documents**: Early procedural memos, regional assignments

#### **Phase II (Years 13-20): Faults in Geography** 
- **System**: Geographic filing begins breaking down
- **Problems**: Documents don't fit regional categories, cross-border materials
- **Documents**: Case studies of filing failures, emergency measures

#### **Phase III (Year 22): Orders Proposal**
- **Innovation**: Introduction of the six interpretive Orders
- **Debate**: Philosophical arguments about classification principles
- **Documents**: Proposal documents, colloquy minutes, objections

#### **Phase IV (Year 23+): Implementation & Objections**
- **System**: Orders filing in practice with ongoing resistance  
- **Tensions**: Competing archival temperaments clash over methods
- **Documents**: Implementation reports, counter-proposals, hearings

### Three Archivist Temperaments:
- **Clerkly Archivists**: Procedural custodians, distrust story and metaphysics
- **Romantic Archivists**: Narrativizing witnesses who want coherent stories
- **Philosophical Archivists**: Systematizing legislators confident in categorical truth

## Writing Voice & Style

- **Institutional voice**: Formal, bureaucratic, but revealing personality through details
- **In-character**: Written by fictional Densworld archival staff
- **Documentary realism**: Authentic-feeling procedural language
- **Revealing subtext**: Personal tensions visible through official language

## Content Guidelines & Document Types

### Document Types:
- **Memo**: Administrative communications
- **Minute**: Meeting records and proceedings
- **Field Report**: On-site archival assessments  
- **Colloquy Note**: Theoretical discussions
- **Counter-Memo**: Responses and objections
- **Directive**: Official policy statements
- **Hearing**: Formal proceedings and testimonies
- **Ruling**: Administrative decisions
- **Brief**: Argumentative position papers
- **Case Note**: Specific filing problems

### What Belongs Here:
- Institutional discussions about filing methodology
- Historical development of the Orders system
- Conflicts between different archival approaches
- Meta-commentary on the classification process itself
- Bureaucratic personality and office politics

### What Does NOT Belong Here:
- Primary source documents (those go in `_notebooks/`)
- Real-world theory (those go in theory collections)
- Out-of-character reflection (those go in `_posts/`)

## Technical Specifications

### Required Front Matter Template:
```yaml
---
layout: debate
title: "Document Title — Descriptive Subtitle"
phase: "Phase I" # or II, III, IV with description
doc_type: "Memo" # Document type from list above
order_focus: ["Order1", "Order2"] # array format, or "n/a"
regions: ["Region1", "Region2"] # always array format
archive_date: "Year N, QN" # Densworld dating
date: 2024-01-01 # Jekyll standard date
clerk_initials: "XX" # Document author initials  
status: "Adopted" # Document status
excerpt: "Brief description of significance"
permalink: /debate/filename-slug/
---
```

### File Naming Convention:
```
phase[N]-[type]-[descriptive-slug].md
```
Example: `phase3-colloquy-orders-proposal.md`

### Navigation Structure:
- Main hub: `archivists-debate.md` organizes by four phases
- Each phase section contains 2-6 key documents
- Individual URLs: `/debate/:name/`

### Hub Page Linking:
**Critical**: Always use Jekyll's relative_url filter for GitHub Pages compatibility:
```markdown
- **[Document Title]({{ '/debate/filename-slug/' | relative_url }})**
  *brief description*
```

## Integration with Archive Collection

### Cross-Referencing Requirements:
- Debate documents should reference actual Archive entries when discussing filing examples
- Orders discussed in Debate should align with Orders implemented in Archive
- Regional problems mentioned in Debate should correspond to regional materials in Archive
- Timeline consistency between institutional development and archived materials

### Fictional World Coherence:
The Debate reveals the institutional process behind the Archive's organization. Readers can experience both the mysterious primary documents and the bureaucratic struggles to categorize them.

## Current Status

- **Hub document**: `archivists-debate.md` with four-phase organization
- **Multiple supporting documents** across all phases
- **Consistent institutional voice** with personality variations
- **Authentic bureaucratic tensions** between competing methodologies

This collection provides the meta-fictional framework that makes the Archive's unusual organization feel earned and realistic—showing the institutional history that led to filing by interpretive Orders rather than geographic regions.