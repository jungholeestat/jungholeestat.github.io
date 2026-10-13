---
layout: academic
title: Research
permalink: /research/
section: research
description: Public research by JungHo Lee in causal inference, statistical learning, and numerical analysis.
---

<div class="jl-research-view" id="research">
  <h1 class="jl-research-heading">Research</h1>
  <div class="jl-research-controls" hidden>
    <div class="jl-search-wrap">
      <span class="jl-search-icon" aria-hidden="true"></span>
      <input id="research-search" type="search" aria-label="Search research" placeholder="Search titles, authors, or topics…" autocomplete="off">
    </div>
    <div class="jl-research-filters" role="group" aria-label="Filter research by topic">
      <button type="button" data-tag="" aria-pressed="true">All</button>
      {% assign topics = 'Causal inference|Experiments|Nonparametric statistics|AI|Others' | split: '|' %}
      {% for topic in topics %}
        <button type="button" data-tag="{{ topic | escape }}" aria-pressed="false">{{ topic }}</button>
      {% endfor %}
    </div>
    <div class="jl-research-status">
      <span id="research-count" role="status" aria-live="polite"></span>
      <button id="research-reset" type="button" hidden>Clear filters</button>
    </div>
  </div>
  {% assign years = site.data.research | group_by: 'year' %}
  {% for year in years %}
    <section aria-label="Research from {{ year.name }}" data-research-year="{{ year.name }}">
      <h2 class="jl-research-year">{{ year.name }}</h2>
      {% for paper in year.items %}
        {% include academic-paper.liquid paper=paper filterable=true %}
      {% endfor %}
    </section>
  {% endfor %}
  <p class="jl-research-empty" hidden>No papers match your search.</p>
</div>
<script src="{{ '/assets/js/research.js' | relative_url | bust_file_cache }}" defer></script>
