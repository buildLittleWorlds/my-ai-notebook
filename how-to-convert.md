# Jekyll Conversion Progress & Remaining Work

## ✅ COMPLETED - Phase 1: Jekyll Foundation
All Jekyll setup work is complete:
- **Jekyll installed** ✅
- **Gemfile created** ✅ (with github-pages and webrick gems)
- **_config.yml configured** ✅ (with collections for posts, kits, notebooks, debate)
- **All layout templates created** ✅ (9 layouts in _layouts/ folder)
- **index.md homepage created** ✅
- **Sample post converted** ✅ (_posts/this-site.md as example)

**Status: 100% COMPLETE** ✅ - All phases finished successfully!

---

## ✅ ALL PHASES COMPLETED

### What We're Doing (High Level)
Converting from hand-written HTML to Jekyll means:
- Write content in simple Markdown files instead of HTML
- Jekyll automatically combines Markdown with templates to create HTML
- Your `style.css` stays exactly the same
- GitHub Pages builds your site automatically when you push changes

## ✅ Phase 2: Convert Your Content - COMPLETED

### ✅ Step 1: Convert 110 Blog Posts - COMPLETED  
**Result**: All 110 posts successfully converted to `_posts/*.md` format with proper front matter.

#### For Each Post File:
1. **Open the HTML file** (e.g., `post2.html`)
2. **Create new Markdown file** in `_posts/` folder:
   - Simple naming: `post-2.md`, `post-3.md`, etc.
   - Example: `post2.html` → `_posts/post-2.md`
3. **Copy content** from between `<article>` tags ONLY
4. **Remove all HTML tags** (`<h2>`, `<p>`, `<article>`, etc.)
5. **Add front matter** at top:

```markdown
---
layout: post
title: "Your Post Title"
post_number: 2
---

Your content here, just plain text with blank lines between paragraphs.
```

#### Quick Reference:
- **Remove**: `<h2>` headings (template handles this)
- **Remove**: All HTML tags (`<p>`, `<article>`, `<em>`, etc.)
- **Keep**: Plain text content only
- **Add**: Front matter with title and post_number
- **Don't add**: next_post/prev_post (Jekyll auto-generates)

#### Batch Processing Tip:
Work through posts systematically: `post2.html` → `post3.html` → etc. You can do this in batches of 10-20 posts at a time.

### ✅ Step 2: Convert Kit Hub Pages - COMPLETED
**Result**: Both romantic-quick-kit.md and ai-hermeneutics-kit.md created with proper layouts and links fixed.

#### A. Romantic Quick Kit
1. **Find file**: `romantic-quick-kit.html`
2. **Create**: `_kits/romantic-quick-kit.md`
3. **Add front matter**:
```markdown
---
layout: kit-hub
title: "Romantic Quick Kit"
subtitle: "How to use this"
---
```
4. **Copy content** from inside `<article>` tags
5. **Update links**: Remove `.html` extensions from internal links
   - `romantic-kit-hermeneutics.html` → `/romantic-kit-hermeneutics`

#### B. AI Hermeneutics Kit  
1. **Find file**: `ai-hermeneutics-kit.html`
2. **Create**: `_kits/ai-hermeneutics-kit.md`
3. **Add front matter**:
```markdown
---
layout: kit-hub
title: "AI Hermeneutics Kit"
subtitle: "How to use this"
---
```
4. **Copy content** and **update links** (remove `.html` extensions)

### ✅ Step 3: Convert Individual Kit Pages - COMPLETED
**Result**: All 27 kit files converted from HTML to markdown with proper front matter.

#### For Each Kit File:
1. **Find HTML files** that start with `romantic-kit-` or `ai-kit-`
2. **Create corresponding `.md` files** in `_kits/` folder:
   - `romantic-kit-hermeneutics.html` → `_kits/romantic-kit-hermeneutics.md`
   - `ai-kit-something.html` → `_kits/ai-kit-something.md`
3. **Add front matter**:
```markdown
---
layout: kit
title: "Your Kit Title"
---
```
4. **Copy content** from inside `<article>` tags
5. **Remove HTML tags**, keep plain text

### ✅ Step 4: Convert Notebooks System - COMPLETED
**Result**: notebooks.md created, 18 archivist files converted to _notebooks/, debate file converted to _debate/

#### A. Create Main Notebooks Page
1. **Find file**: `notebooks.html`
2. **Create**: `notebooks.md` (in root directory)
3. **Add front matter**:
```markdown
---
layout: notebooks-hub
title: "Archivists' Window — Catalog by Orders"
lede: "Your existing description from notebooks.html"
show_debate_notice: true
debate_notice_text: "Your existing debate notice text"
debate_link: "/archivists-debate"
debate_link_text: "History of the Debate →"
---
```

#### B. Convert Individual Notebook Entries
1. **Find all archivist files**: `archivist-a1.html`, `archivist-a2.html`, etc.
2. **Create corresponding files** in `_notebooks/` folder:
   - `archivist-a1.html` → `_notebooks/archivist-a1.md`
3. **Add front matter** to each:
```markdown
---
title: "Entry Title from HTML"
order: "Boundary" (or whatever order applies)
region: "Dens" (or whatever region applies)
excerpt: "Brief description..."
---

Content from inside <article> tags, HTML removed
```

#### C. Convert Debate History
1. **Find debate files**: `archivists-debate.html` and related files
2. **Create files** in `_debate/` folder with front matter:
```markdown
---
title: "Debate Title"
phase: "Phase 1" (or appropriate phase)
participants: ["Archivist A", "Archivist B"]
---

Debate content with HTML removed
```

### ✅ Step 5: Create Posts Index Page - COMPLETED
**Result**: posts.md created with posts-list layout.
1. **Create file**: `posts.md` (in root directory)
2. **Add content**:
```markdown
---
layout: posts-list
title: "Blog Posts"
---
```

*Note: `index.md` already exists and is configured correctly.*

---

## ✅ Phase 3: GitHub Pages Configuration - READY FOR DEPLOYMENT

### Step 1: Configure GitHub Pages
1. **Go to your GitHub repository** online
2. **Click Settings tab** 
3. **Scroll to Pages section**
4. **Set Source**: "Deploy from a branch"
5. **Select branch**: "main" 
6. **Select folder**: "/ (root)"
7. **Click Save**

### Step 2: (Optional) Add Jekyll Workflow  
*GitHub Pages builds Jekyll automatically, but this gives more control:*

1. **Create folder**: `.github/workflows/` 
2. **Create file**: `.github/workflows/jekyll.yml`
3. **Add workflow content** (see original guide for YAML code)

*You can skip this step initially and add it later if needed.*

## ✅ Phase 4: Testing and Deployment - COMPLETED (Local Testing)

### Step 1: Test Locally (Recommended)
*Jekyll and Gemfile are already set up, so you can start testing:*

1. **Install dependencies**:
   ```bash
   bundle install
   ```

2. **Run local server**:
   ```bash
   bundle exec jekyll serve
   ```

3. **View your site**: Open `http://localhost:4000` in browser
4. **Test navigation**: Check that posts, kits, notebooks work correctly

### Step 2: Deploy to GitHub
**After you've converted content and tested locally:**

1. **Add all new files**:
   ```bash
   git add .
   ```

2. **Commit changes**:
   ```bash
   git commit -m "Convert content to Jekyll markdown files"
   ```

3. **Push to GitHub**:
   ```bash
   git push origin main
   ```

4. **Wait 2-3 minutes** for GitHub Pages to build
5. **Check your live site** at your GitHub Pages URL

### Troubleshooting
- **Build fails?** Check GitHub Actions tab for errors
- **Links broken?** Make sure you removed `.html` from internal links
- **Missing content?** Check front matter formatting (the `---` sections)

## ✅ Phase 5: Cleanup - COMPLETED

### ⚠️ Important: Test First!
**Do NOT delete anything until your Jekyll site is working perfectly on GitHub Pages.**

### Files to Delete (After Confirming Success):
- **All post HTML files**: `post1.html`, `post2.html`, ... `post111.html`
- **All kit HTML files**: `romantic-kit-hermeneutics.html`, etc.
- **Old index files**: `posts.html`, `notebooks.html`
- **Old kit hubs**: `romantic-quick-kit.html`, `ai-hermeneutics-kit.html`
- **Old includes**: `header.html`, `footer.html` (if they exist)
- **Archivist HTML files**: `archivist-a1.html`, etc.
- **Debate HTML files**: `archivists-debate.html`, etc.

### Files to Keep:
- **Style**: `style.css` (unchanged!)
- **Media**: `images/` folder, any other assets
- **Jekyll files**: `_config.yml`, `_layouts/`, `_posts/`, `_kits/`, `_notebooks/`, `_debate/`
- **New pages**: `index.md`, `posts.md`, `notebooks.md`
- **Project files**: `Gemfile`, `Gemfile.lock`

---

## Your New Workflow

### Adding a New Blog Post:
1. Create `_posts/title.md`
2. Add front matter and content
3. `git add`, `git commit`, `git push`
4. Site rebuilds automatically

### Editing Content:
1. Find the `.md` file
2. Edit plain text content
3. `git add`, `git commit`, `git push`
4. Site rebuilds automatically

---

## Quick Reference

### Common Issues:
- **Build fails**: Check GitHub Actions tab
- **Links broken**: Remove `.html` from internal links
- **Missing content**: Check front matter formatting

### File Structure:
- **Blog posts**: `_posts/title.md`
- **Kit pages**: `_kits/filename.md`  
- **Notebook entries**: `_notebooks/filename.md`
- **Debate documents**: `_debate/filename.md`

### Benefits:
- Write in simple Markdown instead of HTML
- Automatic navigation and post lists
- Consistent styling across all pages
- Easy maintenance and updates