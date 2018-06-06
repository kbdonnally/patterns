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

# create & write, or append if exists
# files = list of filenames
# add = list of strings to append
def addToFiles(files, add):
	for file, a in zip(files, add):
		with open(file + '.md', 'at') as myfile:
			myfile.write(a)