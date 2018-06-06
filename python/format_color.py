# format_color.py

# HSL copied from google
# -> CSS-friendly color
def formatColor(color):
	return color.replace('hsl', 'hsla').replace('°', '').replace(')', ', 1)\n')

# input here:
color = formatColor("hsl(345°, 6%, 13%)")
print(color)