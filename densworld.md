---
layout: default
title: "Densworld"
lede: "Short fictional pieces set in Densworld."
permalink: /densworld/
---

<div class="top-links">
<a href="{{ '/' | relative_url }}" class="quickkit-pill-small">← Blog Home</a>
</div>

## About Densworld

These are short fictional pieces set in the imaginary world of Densworld. Each piece explores different aspects of this fictional realm through brief narratives and vignettes.

## Stories

<nav aria-label="Densworld Stories">
  <ul class="post-list">
    {% assign private_docs = site.private | sort: 'date' | reverse %}
    {% for story in private_docs %}
    <li><a href="{{ story.url | relative_url }}">{{ story.title }}</a></li>
    {% endfor %}
  </ul>
</nav>

<div class="bottom-links">
<a href="{{ '/' | relative_url }}" class="quickkit-pill">← Back to Blog Home</a>
</div>