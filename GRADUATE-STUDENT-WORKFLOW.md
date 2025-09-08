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

### A. Phase Classification
- **Phase I** (Years 1-12): Regional filing system establishment
- **Phase II** (Years 13-20): Geographic system failures
- **Phase III** (Year 22): Orders proposal and debate  
- **Phase IV** (Year 23+): Implementation and objections

### B. Document Type
- `Memo` - Policy documents, proposals
- `Minute` - Meeting transcripts, proceedings
- `Field Report` - Evidence from regions, measurements vs. testimony
- `Colloquy Note` - Academic discussions, theory debates
- `Counter-Memo` - Opposition documents, warnings
- `Directive` - Official policy adoptions
- `Hearing` - Testimony records, witness statements
- `Ruling` - Edge case decisions, clarifications
- `Brief` - Technical standards, procedures

### C. Order Focus (1-3 primary)
- `Boundary` - Unstable edges, moving lines
- `Doubling` - Replication, copies without origin
- `Craving` - Desire as generative force
- `Silence & Withdrawal` - Non-speech methods, ritual
- `Violence & Secret Life` - Parallel harm ledgers
- `Mediation & Aperture` - Access constraints, devices

---

## Step 2: Create the Jekyll File

### A. File Naming Convention
**Pattern:** `phase{N}-{type}-{descriptive-slug}.md`

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
- `title:` (descriptive title in quotes)
- `phase:` (I, II, III, or IV)
- `doc_type:` (from list in Step 1B)
- `order_focus:` (array of 1-3 Orders from Step 1C)
- `regions:` (relevant geographic areas)
- `date:` (fictional archive date)
- `clerk:` (your initials or fictional clerk)
- `status:` (Adopted/Filed/Referred/Superseded)
- `permalink:` (must match filename)

---

## Step 3: Format Your Content

### A. Required Content Structure
Your prose document must include these sections:

```markdown
## Abstract
2-4 sentences describing what question this document addresses.

## Exhibits
Links to archive slips and quoted clips using Protocol 7.3 format.

### Clip Example (Required - at least 1):
**Clip (A1):**
|| Face-window shall be circular; no door; slips only. ||
**Provenance:** Capital · Inspection Log (caliper checks)
**Order(s):** Mediation & Aperture
**Commentary:** Access is designed; paper passes; bodies do not.

## Main Content
2-6 paragraphs of your argument/analysis in administrative tone.

## Disposition
**Adopted** / **Filed Without Action** / **Referred to Committee** / **Superseded**

## Cross-References
- **[Slip Code]** — Brief description with Order
- **Phase [N] — [Document Title]** — Related debate document
```

### B. Voice and Style Requirements
- **Administrative tone** - exact, procedural, institutional
- **Present contradictions** - don't resolve conflicts in evidence
- **Quote verbatim** - use `|| quoted material ||` for clips
- **Cross-index everything** - minimum 2 slip references, 1 cross-phase document

---

## Step 4: Technical Validation

### A. File Validation Checklist
- [ ] File is in `_debate/` directory
- [ ] Filename follows `phase{N}-{type}-{slug}.md` pattern
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
- Voice consistency with existing debate documents
- Proper use of fictional archive terminology
- Cross-references to existing materials
- Administrative tone maintained throughout

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

1. **Classification:** Phase IV (implementation), Field Report, Mediation & Aperture
2. **Filename:** `phase4-field-window-static-incidents.md`
3. **Location:** `_debate/phase4-field-window-static-incidents.md`
4. **Frontmatter:** Use template with your specific values
5. **Content:** Restructure into Abstract → Clips → Analysis → Disposition → Cross-refs
6. **Test:** Local Jekyll serve to verify rendering
7. **Commit:** Following git workflow above

This process ensures your prose document integrates seamlessly with the existing Jekyll architecture while maintaining the rigorous fictional archive voice.