# Graduate Student Workflow — Blog Posts

## Quick Overview

**Blog Posts** are the **real academic voice** of the site (out-of-character). You're writing as Professor Plate sharing genuine thoughts, arguments, and work-in-progress reflections on literary theory, AI, and hermeneutics.

### Key Principle:
This is **authentic academic blogging** — first person, reflective, conversational but scholarly. Think of it as sharing your thinking process with colleagues and students.

---

## Step 1: Identify Your Post Type

### What Belongs in Blog Posts:
- **Theoretical explorations**: "I've been thinking about..."
- **Methodological questions**: "How should we approach..."
- **AI & interpretation reflections**: "This puzzles me about..."
- **Literary criticism insights**: "Reading X made me realize..."
- **Work-in-progress thoughts**: "I'm not sure where this leads, but..."

### What Does NOT Belong Here:
- Systematic theory frameworks (those go in `_romantic/` or `_ai_hermeneutics/`)
- Fictional archive materials (those go in `_archive/`)
- Meta-archival discussions (those go in `_debate/`)

---

## Step 2: Choose Your Voice & Approach

### Blog Post Voice Markers:
- **First person**: "I think," "This strikes me as," "I've been wondering"
- **Conversational but scholarly**: Direct address to readers, informal asides
- **Provisional**: "This might be wrong, but..." "I'm still working through..."
- **Reflective**: Questions that open rather than close discussions

### Tone Examples:
✓ "This puzzles me about AI interpretation..."  
✓ "I've been reading Butler's work and wondering..."  
✓ "Something about this Romantic concept bothers me..."  
✗ "Butler's theory of performativity states..." (too systematic for blog posts)  
✗ "The archivist noted the following slip..." (fictional, belongs in `_archive/`)

---

## Step 3: Technical Specifications

### File Naming:
```
2024-MM-DD-post-[number].md
```
Example: `2024-01-15-post-25.md`

### Required Front Matter:
```yaml
---
layout: post
title: "Your Post Title"
post_number: [integer]
date: 2024-01-15 10:00:00 -0500
---
```

### File Location:
Place in: `_posts/your-filename.md`

---

## Step 4: Content Structure

### Flexible Structure Options:

#### Option A: Question-Driven Post
1. **Opening question/problem**: What's puzzling you?
2. **Exploration**: Work through the thinking
3. **Provisional conclusion**: Where you've landed (for now)

#### Option B: Reading Response Post  
1. **What you're reading**: Book, article, theory
2. **What strikes you**: Key insights or problems
3. **Implications**: How this affects your thinking

#### Option C: Methodological Post
1. **The method/approach**: What you're trying to do
2. **The problem**: Where it breaks down or gets complicated
3. **Possible solutions**: Tentative ways forward

---

## Step 5: Content Guidelines

### Length & Depth:
- **Short posts (200-500 words)**: Single insight, quick reflection
- **Medium posts (500-1000 words)**: Developed argument, reading response
- **Long posts (1000+ words)**: Complex exploration, multiple threads

### Academic Standards:
- **Cite sources** when referencing specific works
- **Define terms** when introducing complex concepts
- **Acknowledge uncertainty** — it's okay not to have answers
- **Connect to larger questions** in literary theory and hermeneutics

### Voice Consistency:
- Maintain **first person** throughout
- Keep **conversational but scholarly** tone
- Show **thinking process**, not just conclusions
- **Question assumptions**, including your own

---

## Step 6: Integration with Site Ecosystem

### How Blog Posts Connect to Other Collections:

#### To Theory Collections (`_romantic/`, `_ai_hermeneutics/`):
- Blog posts **explore** ideas that later get **systematized** in theory collections
- Use blog posts to **work through problems** before formalizing frameworks
- Reference theory collections when you've already developed systematic approaches

#### To Fictional Collections (`_archive/`, `_debate/`):
- Blog posts can **reflect on the creative process** behind fictional work
- Can discuss **interpretive principles** that get demonstrated fictionally
- Should **NOT** contain fictional content directly

### Linking Examples:
```markdown
I've been developing this idea systematically in my 
[Romantic Quick Kit]({{ '/romantic/romantic-quick-kit/' | relative_url }}), 
but here I want to think through some problems...

This connects to the interpretive challenges I've been exploring 
in the [AI Hermeneutics framework]({{ '/ai-hermeneutics/ai-hermeneutics-kit/' | relative_url }})...
```

---

## Step 7: Common Post Types & Prompts

### Theoretical Exploration Posts:
- "I've been rethinking [concept]. Here's what troubles me..."
- "Reading [author] made me question [assumption]..."
- "How should we handle [methodological problem]?"

### AI & Hermeneutics Posts:
- "Something weird happened when I was reading AI text..."
- "Traditional hermeneutics breaks down when..."
- "The author-function gets complicated with..."

### Literary Criticism Posts:
- "Romantic authenticity isn't what I thought..."
- "This passage from [work] reveals..."
- "The relationship between [concept A] and [concept B]..."

### Methodological Posts:
- "I'm trying a new approach to [problem]..."
- "The two-rail method works except when..."
- "Close reading vs. distant reading in the age of AI..."

---

## Step 8: Workflow Process

### Daily Practice:
1. **Read/research** — engage with primary and secondary sources
2. **Note questions** — what puzzles or interests you?
3. **Draft quickly** — capture thinking while it's active
4. **Revise for clarity** — make accessible without losing complexity
5. **Post and iterate** — use reader feedback to develop ideas further

### Weekly Planning:
- **Monday**: Theoretical exploration
- **Tuesday**: Reading response  
- **Wednesday**: Methodological question
- **Thursday**: AI/hermeneutics reflection
- **Friday**: Open/miscellaneous

### Monthly Themes:
- Develop **recurring threads** across multiple posts
- **Build complexity** over time through linked explorations
- **Connect to course content** if you're teaching
- **Respond to current events** in academic/literary world

---

## Step 9: Quality Standards

### Content Quality:
- **Intellectual honesty** — admit uncertainty, acknowledge counterarguments
- **Accessible complexity** — sophisticated ideas in readable prose
- **Original thinking** — engage critically, don't just summarize
- **Scholarly engagement** — cite sources, join conversations

### Technical Quality:
- **Clear writing** — edit for clarity and flow
- **Proper citations** — academic integrity in all references
- **Jekyll formatting** — ensure markdown renders correctly
- **Link functionality** — test all internal and external links

---

## Step 10: Example Post Structure

```markdown
---
layout: post
title: "The Problem with Romantic Sincerity"
post_number: 47
date: 2024-01-15 10:00:00 -0500
---

I've been working through the authenticity concept in my Romantic Quick Kit, 
but something keeps bothering me about how we usually think about sincerity...

[2-3 paragraphs exploring the problem]

This connects to a larger question about whether interpretation can ever 
be truly "authentic" to an author's intentions, especially when we're 
dealing with AI-generated texts...

[2-3 paragraphs developing the connection]

I don't have a clean answer yet, but I think the issue might be that 
we're using "sincerity" when we really mean something more like 
"systematic coherence"...

[Concluding thoughts, questions for further exploration]
```

This workflow helps maintain the **authentic academic voice** that distinguishes blog posts from both the systematic theory collections and the fictional archive materials.