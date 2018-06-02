---
layout: page-text
permalink: /page/
title: Page Default Appearance
---

## Structure of Content

### How this file is compiled

{:.language-markup}
- This should be showing up _inside_ the `page-main-content` div, and the title is already entered above it.
	- Jekyll combines the default layout, fills that stuff in, then the page layout and fills the remaining stuff in
	- We don't have to type the title because it's programmed into the page layout
- File locations:
	- Layouts: `_layouts/default.html`, `_layouts/page.html`
	- The file where this sentence is written: `pages/page-default.md`
	- Where style instructions are stored: for this page, it's `assets/css/_sass/_page.scss`
		- All the stylesheets get put together in `assets/css/style.scss`
- Okay, cool, now we're gonna set some default styles to demonstrate how our stylesheet is set up. Visual cheatsheet!

## Components of Styles

### Defining margins & padding
- 60px set aside for navbar at top, and most pages add 3em of padding at bottom so they don't run into footer
- Page is using 12-column grid (by percentages)

### Grid structure: why
- I guess I'm basically copying Bootstrap? 12 is just a really good number
  - Need to be more careful about not being afraid to do off-kilter number if it's trying to look funky

### Color Scheme

- I think I've almost landed on this one: [Coolors.co](https://coolors.co/6320ee-edd2e0-6cd4ff-8b80f9-242325) w/ Han Purple, Queen Pink, Maya Blue, Medium Slate Blue, & Raisin Black

### Example of CSS setup

{:.language-css}
*NB: Technically SCSS, which is just uncompiled CSS.* It basically means you can nest things, which I find a lot less confusing than writing things like `main`, `main > p.classname`, and `main > p.class-name a` as 3 separate selectors.

Here's the setup for the element that contains all of this page's content:

{:.language-scss}
```
.page-wrapper {
	position: relative;
	padding: 0em 4.167%;
	padding-bottom: 3em;
	@media screen and (min-width: 600px) {
		padding: 0em 8.33%;
		padding-bottom: 3em;
	}
	@media screen and (min-width: 768px) {
		font-size: 1.125rem; // 18px
	}
	@media screen and (min-width: 1020px) {
		max-width: calc(800px + 16.67%);
		margin: 0 auto;
	}
}
```

### Examples of headings:

># Heading 1
>## Heading 2
>### Heading 3
>#### Heading 4