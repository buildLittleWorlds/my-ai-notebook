# Graduate Student Technical Workflow: Adding Debate Documents to Jekyll Site

## Overview
This guide provides step-by-step instructions for converting your prose document into a properly formatted Jekyll collection item and integrating it into the "Archivists' Debate" section of Professor Plate's Notebook.

## Prerequisites
- You have a prose document ready to add to the site
- You have access to the repository with write permissions
- Jekyll is installed and the site runs locally (`bundle exec jekyll serve`)

---

## Step 1: Determine Document Classification

Before creating your file, identify these elements from your prose document:

### A. Phase Classification (determines when and what temperamental balance)
- **Phase I** (Years 1-12): Regional filing system establishment  
  *Temperamental balance:* Clerkly dominance, with occasional philosophical seeds. Romance barely appears.
- **Phase II** (Years 13-20): Geographic system failures  
  *Temperamental balance:* All three temperaments emerge clearly for the first time.
- **Phase III** (Year 22): Orders proposal and debate  
  *Temperamental balance:* Philosophical dominance with clerkly resistance. Romance largely absent.
- **Phase IV** (Year 23+): Implementation and objections  
  *Temperamental balance:* All three temperaments collide, generating institutional self-consciousness.

### B. Document Type (with temperamental tendencies)
- `Memo` - Policy documents, proposals (*often philosophical*)
- `Minute` - Meeting transcripts, proceedings (*typically clerkly*)
- `Field Report` - Evidence from regions, measurements vs. testimony (*usually clerkly, sometimes philosophical*)
- `Colloquy Note` - Academic discussions, theory debates (*often romantic*)
- `Counter-Memo` - Opposition documents, warnings (*any temperament in opposition mode*)
- `Directive` - Official policy adoptions (*typically philosophical*)
- `Hearing` - Testimony records, witness statements (*romantic-philosophical*)
- `Ruling` - Edge case decisions, clarifications (*clerkly*)
- `Brief` - Technical standards, procedures (*philosophical*)

### C. Temperament (REQUIRED - choose one)
- **Clerkly**: Procedural, anxious, exact. "Filed under Dens. Contradiction noted." Focus on custody, protocols, stamps.
- **Romantic**: Narrative, testimonial, dramatic. "She swore the ditch had grown; the town agreed." Focus on individual voices, stories.
- **Philosophical**: Abstract, systematic, legislative. "Evidence demonstrates Boundary Order through unstable geographical determination." Focus on categories, patterns.

### D. Order Focus (1-3 primary)
- `Boundary` - Unstable edges, moving lines
- `Doubling` - Replication, copies without origin
- `Craving` - Desire as generative force
- `Silence & Withdrawal` - Non-speech methods, ritual
- `Violence & Secret Life` - Parallel harm ledgers
- `Mediation & Aperture` - Access constraints, devices

---

## Step 2: Create the Jekyll File

### A. File Naming Convention
**Pattern:** `phaseN-{type}-{descriptive-slug}.md`

**Examples:**
- `phase1-memo-borough-drawers.md`
- `phase2-field-dens-boundary-report.md`
- `phase3-counter-memo-metaphysics-risk.md`
- `phase4-hearing-create-the-case.md`

### B. File Location
Place your file in: `_debate/your-filename.md`

### C. Required YAML Frontmatter
Copy this template and fill in your specific values:

```yaml
---
layout: debate
title: "Your Document Title"
phase: "I"
doc_type: "Memo"
temperament: "Clerkly"
order_focus: ["Boundary", "Mediation & Aperture"]
regions: ["Dens", "Capital"]
date: "Year 22, Q1"
clerk: "YourInitials"
status: "Adopted"
permalink: /debate/your-filename/
---
```

**Required Fields:**
- `layout: debate` (always use this)
- `title:` (descriptive title in quotes with subtitle after em-dash)
- `phase:` (I, II, III, or IV - single Roman numerals only)
- `doc_type:` (from list in Step 1B)
- `temperament:` (Clerkly/Romantic/Philosophical - REQUIRED)
- `order_focus:` (array of 1-3 Orders from Step 1D, or "n/a")
- `regions:` (array format even for single region)
- `archive_date:` (fictional archive date in "Year N, QN" format)
- `date: 2024-01-01` (standardized Jekyll date)
- `clerk_initials:` (NOT "clerk:" - must be "clerk_initials:")
- `status:` (Adopted/Filed/Referred/Superseded)
- `excerpt:` (brief description for listings)
- `permalink:` (must match filename exactly: /debate/filename-without-.md/)

---

## Step 3: Format Your Content

### A. Required Content Structure
**CRITICAL: Do NOT include H1 (#) headings - Jekyll displays the frontmatter title automatically**

Your prose document must include these sections:

```markdown
## Abstract
2-4 sentences describing what question this document addresses in your chosen temperament voice.

## Exhibits
Include 1-2 quoted clips with proper formatting and temperament-appropriate commentary.

### Clip Example (Required - at least 1):
**Clip (A1):**
|| Face-window shall be circular; no door; slips only. ||
**Provenance:** Capital · Inspection Log (caliper checks)
**Order(s):** Mediation & Aperture
**Commentary (Temperament):** Commentary matching your temperament:
- Clerkly: "Filed under Capital. Protocol documented."
- Romantic: "The window speaks: bodies denied, paper permitted."  
- Philosophical: "Evidence of systematic access control through designed constraint."

## Main Content/Argument
2-6 paragraphs in your chosen temperament voice (not generic administrative).

## Disposition
**Adopted** / **Filed Without Action** / **Referred to Committee** / **Superseded**

## Cross-References
Use proper Jekyll linking syntax:
- **Phase [N] — [Document Title]({{ '/debate/phaseN-type-slug/' | relative_url }})**
```

### B. Voice and Style Requirements
- **Temperamental consistency** - must match your chosen temperament throughout
  - **Clerkly**: Terse, procedural, exact. "Filed under Dens. Contradiction noted."
  - **Romantic**: Narrative, testimonial, dramatic. "She swore the ditch had grown; the town agreed." 
  - **Philosophical**: Abstract, systematic, legislative. "Evidence demonstrates Boundary Order through unstable geographical determination."
- **Present contradictions** - don't resolve conflicts in evidence (but temperaments handle differently)
- **Quote verbatim** - use `|| quoted material ||` for clips
- **Cross-index everything** - minimum 2 slip references, 1 cross-phase document
- **Commentary must match temperament** - clerks preserve mechanically, romantics dramatize, philosophers systematize

---

## Step 4: Technical Validation

### A. File Validation Checklist
- [ ] File is in `_debate/` directory
- [ ] Filename follows `phaseN-type-slug.md` pattern
- [ ] YAML frontmatter is properly formatted (no tabs, proper quotes)
- [ ] Permalink matches filename
- [ ] At least one clip formatted with Protocol 7.3
- [ ] Disposition clearly stated
- [ ] Cross-references included

### B. Local Testing
1. Run `bundle exec jekyll serve`
2. Navigate to `http://127.0.0.1:4000/my-ai-notebook/debate/your-filename/`
3. Verify page renders correctly
4. Check that frontmatter displays properly
5. Test all internal links

---

## Step 5: Integration with Site Navigation

### A. Automatic Integration
Your document will automatically appear in:
- Debate collection listings
- Phase-based organization
- Order-based cross-indexing

### B. Manual Hub Updates (if needed)
If creating a new document type or phase subsection, you may need to update:
- `debate.html` or main debate hub page
- Navigation includes in `_includes/`

---

## Step 6: Git Workflow

### A. Commit Process
```bash
# Add your new file
git add _debate/your-filename.md

# Add any related updates
git add debate.html  # if you updated the hub

# Commit with descriptive message
git commit -m "Add Phase IV hearing on catalog feedback

- Documents testimony from North singers, Sticks clinicians
- Establishes Feedback Docket cross-indexing protocol
- Filed under Mediation & Aperture focus

🤖 Generated with Claude Code"

# Push to repository
git push origin main
```

### B. Commit Message Format
```
Add [Phase] [doc_type] on [topic]

- Brief bullet point of main content
- Key findings or policies established  
- Primary Order classifications

🤖 Generated with Claude Code
```

---

## Step 7: Quality Assurance

### A. Content Review
- **Temperamental voice consistency** - document must embody one temperament clearly
- Proper use of fictional archive terminology
- Cross-references to existing materials
- **Temperamental authenticity** - must feel written by a specific type of archivist, not generic admin
- Commentary on clips matches temperamental approach to evidence

### B. Technical Review  
- File builds without Jekyll errors
- All links functional
- Frontmatter renders correctly
- Mobile responsiveness maintained

---

## Troubleshooting

### Common Issues:
1. **YAML Error:** Check for tabs (use spaces), unclosed quotes, improper array syntax
2. **Page Not Found:** Verify permalink matches filename exactly
3. **Broken Links:** Ensure referenced files exist in correct collections
4. **Layout Issues:** Confirm `layout: debate` is specified

### Testing Commands:
```bash
# Check Jekyll build
bundle exec jekyll build

# Serve locally with debugging
bundle exec jekyll serve --trace

# Validate YAML frontmatter
bundle exec jekyll doctor
```

---

## Example: Converting Your Prose Document

If you have a prose document about window inspection procedures:

1. **Classification:** Phase IV (implementation), Field Report, **Clerkly temperament**, Mediation & Aperture
2. **Filename:** `phase4-field-window-static-incidents.md`
3. **Location:** `_debate/phase4-field-window-static-incidents.md`
4. **Frontmatter:** Use template with your specific values (include `temperament: "Clerkly"`)
5. **Content:** Restructure into Abstract → Clips → Analysis → Disposition → Cross-refs
6. **Temperamental voice:** Maintain clerkly precision throughout - "Two static incidents logged. Grit-induced distortion noted. Status: PASS."
7. **Test:** Local Jekyll serve to verify rendering
8. **Commit:** Following git workflow above

This process ensures your prose document integrates seamlessly with the existing Jekyll architecture while maintaining the rigorous fictional archive voice **and expressing one of the three distinct archivist temperaments.**

---

## Appendix: The Three Temperaments Quick Reference

### Clerkly Archivists (The Custodians)
**Fear:** Chaos, loss, falsification  
**Conviction:** "The Archive preserves; it does not interpret."  
**Voice:** Short, precise sentences. Focus on procedures, stamps, filing codes.  
**Evidence approach:** Mechanical preservation. Every contradiction filed, not resolved.

### Romantic Archivists (The Witnesses)
**Fear:** Fragmentation, silence, meaninglessness  
**Conviction:** "Every slip carries a witness; every witness carries a world."  
**Voice:** Narrative momentum, dramatic attention to individuals, opening questions.  
**Evidence approach:** Testimonial weaving. Contradictions are dramatic tension.

### Philosophical Archivists (The Systematizers)
**Fear:** Incoherence, arbitrariness, chaos  
**Conviction:** "The Archive reveals the world's orders."  
**Voice:** Abstract language, systematic ambition, confident legislation.  
**Evidence approach:** Systematic organization. Contradictions are dialectical pressure.

**Remember:** Each document must embody ONE temperament clearly, but all three voices must appear across the debate collection to maintain the institutional tension that keeps the Archive alive.