# edit_research_category.py
# turn from 1-item array to string for easier templating

import os, re
import write_to_files as write

project_paths = os.listdir("../_research")
print(project_paths)
def editCategories(files):
	for file in files:
		with open("../_research/" + file, 'r+', encoding='utf-8') as myfile:
			for i, line in enumerate(myfile):
				if 'research-category' in line:
					print(i)

editCategories(project_paths)

# lol nvm just did it by hand - not deleting this b/c could be useful starting point for something