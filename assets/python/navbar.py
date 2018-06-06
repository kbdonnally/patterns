# navbar.py

divtemplate = '''<li class="nav-list__{cname}"><a href="{{ page.url | relative_url }}">{page}</a></li>'''

pages = ['Home', 'About', 'FAQ', 'Research', 'Events', 'Makerspace', 'Student Opportunities', 'Blog', 'People']

pageclasses = [p.lower().replace(' ', '-') for p in pages]

for p, c in zip(pages, pageclasses):
	div = divtemplate.format(cname=c, page=p)
	print(div)