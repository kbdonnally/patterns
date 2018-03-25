# print_divs.py

div = '''<div class="collection__item">\n\t<div class="collect-item__img">Image goes here</div>\n\t<div class="collect-item__title">Title of Item {0}</div>\n</div>'''

def printDivs(div, num):
	for n in range(num):
		print(div.format(n + 1))

printDivs(div, 20)