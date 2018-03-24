# filenames-to-html.py
# match images w/ project titles

# FUNCTIONS:

# using regex to search and grab
def regexTextSearch(file, pattern):
	import re

	with open(file, 'rt') as myfile:
		matches = re.findall(pattern, myfile.read())
		return matches

# CALLS:

# match string s where s == 'class="<val>"'
pattern = r'class=".*?"'

# list of all 'class="<val>"' in file
matches = regexTextSearch('research.html', pattern)

print(matches)