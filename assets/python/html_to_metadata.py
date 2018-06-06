# filenames-to-html.py
# match images w/ project titles

################### FUNCTIONS: #############

# write HTML to string, strip excess whitespace
def textToString(file):
	with open(file, 'rt', encoding='utf-8') as myfile:
		html = myfile.read()
		string = html.strip().replace('\n', '').replace('\t', '')
		return string

# using regex to search and grab
def regexTextSearch(html, pattern):
	import re

	matches = re.findall(pattern, html, re.DOTALL)
	return matches

# use only <li> that contain <img>
def filterByContent(matches):
	ul = [m for m in matches if 'img' in m]
	return ul

# take each <li> -> return <img> src attribute
def grabImageSource(ul):
	import re

	sources = []
	for li in ul:
		result = re.findall(r'src=".*?"', li)
		sources.append(result[0])
	return sources

# split at all '/', take last section, remove endquote -> filename.ext
def srcToFileName(src_list):
	filenames = []
	for s in src_list:
		filename = s.split('/')[-1].replace('"', '')
		filenames.append(filename)
	return filenames

# take each <li> -> return title of project
def grabProjectTitles(ul):
	import re

	titles = []
	for li in ul:
		result = re.findall(r'<h2>.*?<', li)
		title = result[0].split('>')[1].replace('<', '')
		titles.append(title)
	return titles

# take each <li> -> return title of project
def grabProjectSlugs(ul):
	import re

	slugs = []
	for li in ul:
		result = re.findall(r'href=".*?"', li)
		slug = result[0].split('/')[-2]
		slugs.append(slug)
	return slugs

################## CALLS: ##################

# take HTML file -> strip excess whitespace -> return string
html = textToString('research.html')

# match string s where s == '<li<val></li>'
pattern = r'<li>.*?</li>'

# list of all <li> elements in file
matches = regexTextSearch(html, pattern)

# list of all <li> w/ images in file
ul = filterByContent(matches)

# list of 'src' attribute in each <li>
src_list = grabImageSource(ul)

# 'filename.ext' per <img> in <li>
filenames = srcToFileName(src_list)
# print(filenames)

# 'Title of Project' per <h2> in <li>
titles = grabProjectTitles(ul)

# 'project-slug' per 'href' in <li> <a>
slugs = grabProjectSlugs(ul)

'''
desired format:
{slug}.md ->

layout: research
slug: {slug}
title: {title}
preview-img: {filename}
'''

# ('title: val', 'filename: val', 'slug: val') per project
tuples = [(title, file, slug) for 
			title, file, slug in zip(titles, filenames, slugs)]
tuples.sort()

def tuplesToYAML(tuples):
	yamls = []
	for (title, file, slug) in tuples:
		yaml = '''---\nlayout: research\nslug: {slug}\ntitle: {title}\npreview-img: {file}\n'''.format(title=title, file=file, slug=slug)
		yamls.append(yaml)
	return yamls

yamls = tuplesToYAML(tuples)

# for yaml in yamls:
#	print(yaml)