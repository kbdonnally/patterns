---
layout: page-text
title: SLab Homepages
permalink: /homepages/
---

## Notes from SLab Design Google Doc

**Organization of homepage sections**
- Hero statement and smaller text

**Priority (for visually chunking sections of page by color/design)**
- Top: FAQ, Contact Us (email, consult form, newsletter in one section)
- Next: Find us (our spaces diagram), events, Open Office Hours
- Then: Student Opportunities, makerspace, spatial tech
- Drop people and charter sections, link those from within text in FAQ section near top

**Features**
- Ribbon linking to Library homepage, near top of SLab homepage? And/or just homepage section near top with Library logo?
- Navbar has clear search icon + search field

## List of Drafts

{% for page in site.homepages %}
* ### [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
{% endfor %}