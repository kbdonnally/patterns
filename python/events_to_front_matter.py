# events_to_front_matter.py
# heavily using methods from html_to_metadata.py

import html_to_metadata as html
import re, os

# HTML of events as plaintext
event_html = html.textToString('../pages/events.html')

# find all table row elements
regex = r'<tr>.*?</tr>'
trs = html.regexTextSearch(event_html, regex)

# remove first one, which does setup for old HTML
trs.pop(0)

# split_list = [tr.split('</td>') for tr in trs]
regex2 = r'<td>.*?</td>'

tds = []
for tr in trs:
	data = html.regexTextSearch(tr, regex2)
	tds.append(data)

# list of '<td> date info </td>''
whens = []

# list of '<td> title/place info </tr>'
whats = []
for when, what in tds:
	whens.append(when)
	whats.append(what)

# list of 'date info', 'place/title'
datetime = [w.split('<br/>') for w in whens]

# list of 'title', 'place info'
whatwhere = [w.split('<br/>') for w in whats]

# add place to Metagaming event
whatwhere[7].append('TBD')

slugs = [w[0].split('events/')[1].split('/')[0] for w in whatwhere]
print(slugs)

# RESULTS:

# list of dates
dates = [d[0].replace('<td>', '').strip() for d in datetime]

# list of times
times = [d[1].replace('</td>', '').strip() for d in datetime]

# slugs = [re.findall(r'href=".?*"', w[0], re.DOTALL) for w in whatwhere]

# list of titles
titles = [w[0].split('">')[1].replace('</td>', '').replace('</a>', '').strip() for w in whatwhere]

titles_with_quotes = ['"' + t + '"' for t in titles if ':' in t]
print(titles_with_quotes)
# list of locations
places = [w[1].split('</i>')[0].replace('<i>', '').strip() for w in whatwhere]

# assign categories by inference - don't exist irl
categories = [['office hours']] * 12
categories[0] = ['info sessions']
categories[1] = ['digital humanities', 'visiting speakers']
categories[4] = ['workshops', 'html and css', 'beginners']
categories[7] = ['workshops']
categories[8] = ['workshops', 'makerspace', 'python']
categories[9] = ['digital humanities', 'presentations']
categories[10] = ['digital humanities', 'presentations']
categories[11] = ['makerspace']

# (title, [categories]) for each event - mostly so I can see they match up
titlecats = [(t, c) for t, c in zip(titles, categories)]
# print(titlecats)

fm_template = '''---\nlayout: event\ntitle: {title}\ndate: {date}\ntime: {time}\nplace: {place}\ncategories: {cats}\n---\n'''
# print(frontmatter)

frontmatter = []
for i in range(12):
	fm = fm_template.format(title=titles[i], date=dates[i], time=times[i], place=places[i], cats = categories[i])
	frontmatter.append(fm)

for i, f in enumerate(frontmatter):
	with open('_events/' + slugs[i] + '.md', 'wt', encoding='utf-8') as myfile:
		myfile.write(f)

