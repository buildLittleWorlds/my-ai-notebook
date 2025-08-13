# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML blog called "My AI Notebook" by Daniel Plate. It's a personal blog exploring AI, creativity, writing, and philosophical reflections on technology. The blog consists of static HTML pages with consistent styling and navigation.

## Architecture

- **Static HTML**: Pure HTML/CSS site with no build process or dependencies
- **Structure**: 
  - `index.html`: Main page with navigation links to all posts
  - `post[N].html`: Individual blog post pages (currently posts 1-37)
  - `style.css`: Global styles using Space Mono font
  - `postx.html`: Template or draft post

## File Structure

- Each post follows a consistent HTML template with:
  - Standard header with site title linking back to home
  - Article content in semantic markup
  - Navigation links (Back to Home | Next Post)
  - Consistent footer with copyright

## Content Management

- Posts are numbered sequentially (post1.html, post2.html, etc.)
- The main index.html contains a manually maintained navigation list in reverse chronological order
- New posts require:
  1. Creating a new postN.html file following the existing template
  2. Adding the post link to the navigation list in index.html
  3. Updating the "Next Post" link in the previous post

## Styling

- Uses Space Mono monospace font from Google Fonts
- Consistent color scheme (#333 text on white background)
- Responsive design with max-width container
- Hover effects on navigation links
- Code blocks styled with background and border-radius

## Development

This is a static site with no build process. Changes can be made directly to HTML/CSS files. The site appears to be version controlled with git.

## Content Themes

The blog focuses on AI and creativity, exploring topics like:
- AI's impact on writing and authorship
- Philosophical reflections on technology
- Literary analysis and cultural criticism
- Personal thoughts on AI tools and their creative potential