# filenames-to-html.py
# match images w/ project titles

# FUNCTIONS:

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

# create or open file & write to it
def writeToFile(file, list):
	with open(file, 'wt') as myfile:
		for l in list:
			myfile.write(l + '\n')

# CALLS:

html = textToString('research.html')
# print(html_string[1000:2000])

# match string s where s == '<li<val></li>'
pattern = r'<li>.*?</li>'

# list of all 'class="<val>"' in file
matches = regexTextSearch(html, pattern)
print(matches)
