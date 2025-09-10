---
layout: post
title: "Sharpening the Blur"
post_number: 37
date: 2025-06-26 10:00:00 -0500
---

A lot of the critique of AI is built on a folk theory of how the technology works. The idea is that an LLM is like a "blurry jpeg of the web," as [Ted Chiang famously put it](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web). It takes everything on the internet, averages it all out, and gives you back the most generic, "mid" version. This explains why the output often feels soulless and unoriginal. It's the ultimate act of what I've been calling ["levelling"](/post-9): the flattening of difference into a bland, predictable mean.

The problem is that this isn't technically how LLMs work. It's a metaphor for the feeling of using one with a simple prompt, but it misrepresents the machine itself. An LLM doesn't store a "copy" of the internet, blurry or otherwise. It builds a statistical model of the relationships among words. It learns the patterns, structures, and vast possibilities of language. It's a model for generating language, not a database of existing language.

A recent academic paper, ["Evidence Against LLM Homogenization in Creative Writing,"](https://kiaghods.com/assets/pdfs/LLMHomogenization.pdf) takes on this folk theory directly. The researchers found that, yes, if you give an LLM a vague prompt (what they call a "cold-start problem"), it will produce homogenous, "average" text. But this isn't a design flaw; it's a feature of a probabilistic system defaulting to the most common pathways.

Their key finding is what happens when you give the model a better starting point. When they provided the LLM with even a small amount of context (the beginning of a human-written story) the homogenization disappeared. The model was able to continue the story with as much diversity and creative variation as human writers. The "blur" can be sharpened.

This gets at what it might mean to be "creative" with these tools. The LLM has learned a vast map of interconnected concepts, what we can call "latent space." A generic prompt places the model in the most crowded, central part of that map. The output will naturally be generic. The art of prompting, then, is the art of pushing the model into the more unusual, original, and less-traveled regions of that space.

This is also why the paper's other experiment is so significant. They found they could increase the diversity of the output simply by giving the LLM a few random words to use as "inspiration." Why does this work? Because it forces the model to synthesize a connection between disparate concepts. It has to chart a new path through its latent space. An unusual prompt, seeded with random or unexpected words, has an incredibly high probability of forcing the model to generate language that has never existed before.

This reframes the entire debate. The problem isn't that LLMs are incapable of creativity because they are just "full of averages." The problem is that most prompts don't work creatively. They don't move the model into a space where novelty is possible. The machine isn't a plagiarist or an averager; it's a probabilistic engine waiting for a prompt interesting enough to push it beyond the mean.