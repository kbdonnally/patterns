# write-to-file.py
# create or open files & write fancy things to them

import os, re
import html_to_metadata as html

# FUNCTIONS:

# create & write, or append if exists
# files = list of filenames
# add = list of strings to append
def addToFiles(files, add):
	for file, a in zip(files, add):
		with open(file + '.md', 'at') as myfile:
			myfile.write(a)

# list of files -> file content as strings
def grabFileText(files):
	text = []
	for file in files:
		with open(file, 'rt', encoding='utf-8') as myfile:
			md = myfile.read()
			text.append(md)
	return(text)

# remove content before 'research-category'
def filterFrontMatter(texts):
	filtered = []
	for text in texts:
		match = re.search(r'research-category.*', text, re.DOTALL)
		result = match.group(0)
		filtered.append(result)
	return filtered

# write modified content to new dir w/ same filenames
def writeToNewFile(filtered, filenames):
	for text, filename in zip(filtered, filenames):
		with open('_research-new/' + filename, 'at', encoding='utf-8') as myfile:
			myfile.write(text)

# CALLS:

# list of filenames like 'projectname.md'
project_names = os.listdir('_research')
project_names.sort()

# prepend names w/ directory
filepaths = ['_research/' + project for project in project_names]

# use filepaths to extract text content of each file
texts = grabFileText(filepaths)

# filter text content -> start at 'research-category:'
filtered = filterFrontMatter(texts)

# YAML to prepend files with, 1 per .md file
yamls = html.yamls

# RESULT:

# 1. write YAML from html_to_metadata to '_research-new/projectname.md'
# writeToNewFile(yamls, project_names)

# 2. write rest of project file to same location
# writeToNewFile(filtered, project_names)