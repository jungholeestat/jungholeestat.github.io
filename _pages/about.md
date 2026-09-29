---
layout: academic
title: About
permalink: /
section: about
---

<section aria-label="About" class="jl-intro" id="about">
<figure class="jl-portrait">
<img alt="Portrait of JungHo Lee" fetchpriority="high" height="472" src="{{ '/assets/img/prof_pic.jpg' | relative_url }}" width="354"/>
</figure>
<div>
<p class="jl-eyebrow">Statistics · Carnegie Mellon</p>
<p class="jl-bio">I am a PhD student in Statistics at CMU, advised by Edward Kennedy and Dave Choi. My research focuses on causal inference and statistical learning.</p>
<div class="jl-inline-links">
<a aria-label="Curriculum vitae" href="https://drive.google.com/file/d/104Zyw8kQXTD_HcrGPtgh_-vjvOzUfWLl/view?usp=sharing" rel="noopener" target="_blank">CV</a>
<a href="https://scholar.google.com/citations?hl=en&amp;user=dX7fpu4AAAAJ" rel="noopener" target="_blank">Google Scholar</a>
<a href="#contact">Contact</a>
</div>
</div>
<aside class="jl-interests">
<h2>Research interests</h2>
<div class="jl-interest-group"><h3>Causal inference</h3>
<p>Experimental design, instrumental variable methods, interference</p></div>
<div class="jl-interest-group"><h3>Statistical learning</h3>
<p>Nonparametric statistics, measurement error</p></div>
<div class="jl-interest-group"><h3>Applications</h3>
<p>Public policy, healthcare</p></div>
</aside>
</section>
<section aria-labelledby="selected-research-heading">
  <div class="jl-section-title"><h2 id="selected-research-heading">Selected research</h2></div>
  {% assign selected_papers = site.data.research | where: 'selected', true %}
  {% for paper in selected_papers %}
    {% include academic-paper.liquid paper=paper selected=true number=forloop.index %}
  {% endfor %}
</section>
