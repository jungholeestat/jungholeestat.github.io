---
layout: academic
title: News
permalink: /news/
description: News and announcements from JungHo Lee.
---

<section class="jl-talks-view" aria-labelledby="news-heading">
  <h1 class="jl-talks-heading" id="news-heading">News</h1>
  <ol class="jl-talk-list">
    {% assign announcements = site.news | sort: 'date' | reverse %}
    {% for announcement in announcements %}
      <li>
        <time datetime="{{ announcement.date | date: '%Y-%m-%d' }}">{{ announcement.date | date: '%b %Y' }}</time>
        <div>{{ announcement.content | markdownify }}</div>
      </li>
    {% endfor %}
  </ol>
</section>
