# events_to_front_matter.py
# heavily using methods from html_to_metadata.py

import html_to_metadata as html
import re, os

eventtable = html.textToString('../pages/events.html')

print(eventtable)