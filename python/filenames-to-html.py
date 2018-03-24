# filenames-to-html.py
# match images w/ project titles

################### FUNCTIONS: #############

# write HTML to string, strip all whitespace
def textToString(file):
	with open(file, 'rt') as myfile:
		html = myfile.read()
		string = html.strip().replace('\n', '').replace(' ', '')
		return string

# using regex to search and grab
def regexTextSearch(html, pattern):
	import re

	matches = re.findall(pattern, html)
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

# take each <li> -> return title of project
def grabProjectTitles(ul):
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

################## CALLS: ##################

# take HTML file -> output as string w/ no whitespace
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
print(filenames)