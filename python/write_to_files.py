# write-to-file.py
# create or open file & write to it

import html_to_metadata as html

yamls = html.yamls
for yaml in yamls:
	print(yaml)

def writeToFile(file, list):
	with open(file, 'at') as myfile:
		for l in list:
			myfile.write(l + '\n')

el = ['one', 'two', 'three']
files = ['test1', 'test2', 'test3']

'''def testFile(files):
	for file in files:
		with open(file + '.md', 'wt') as myfile:
			myfile.write('will this get erased?\n')
'''
# testFile(files)

# create & write, or append if exists
# files = list of filenames
# add = list of strings to append
def addToFiles(files, add):
	for file, a in zip(files, add):
		with open(file + '.md', 'at') as myfile:
			myfile.write(a)

# addToFiles(files, el)