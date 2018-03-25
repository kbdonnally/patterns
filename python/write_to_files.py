# write-to-file.py
# create or open file & write to it

import os
import html_to_metadata as html

yamls = html.yamls


# create & write, or append if exists
# files = list of filenames
# add = list of strings to append
def addToFiles(files, add):
	for file, a in zip(files, add):
		with open(file + '.md', 'at') as myfile:
			myfile.write(a)

# addToFiles(files, el)
projects = os.listdir('_research')
print(projects)