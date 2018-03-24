# helpers.py
# reusable functions for web dev

# using regex to search and grab
def regexTextSearch(file, pattern):
	import re

	with open(file, 'rt') as myfile:
		matches = re.findall(pattern, myfile.read())
		return matches

# example pattern:
# match string s where s == 'class="<val>"'
pattern = r'class=".*?"'