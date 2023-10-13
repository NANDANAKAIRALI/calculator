#Create a regex pattern to remove all HTML tags from a string
#<p>This is a <b>sample</b> HTML <i>string</i>.</p>

import re

html_string =input("Enter the string")
clean_string = re.sub(r'<[^>]*>', '', html_string)

print(clean_string)