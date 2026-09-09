---
layout: academic
title: Research
permalink: /research/
section: research
description: Public research by JungHo Lee in causal inference, statistical learning, and numerical analysis.
---

<div class="jl-research-view">
  <h1 class="jl-research-heading">Research</h1>
  {% assign years = site.data.research | group_by: 'year' %}
  {% for year in years %}
    <section aria-label="Research from {{ year.name }}">
      <h2 class="jl-research-year">{{ year.name }}</h2>
      {% for paper in year.items %}
        {% include academic-paper.liquid paper=paper %}
      {% endfor %}
    </section>
  {% endfor %}
</div>
