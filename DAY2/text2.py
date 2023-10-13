import re

import content

pattern=re.compile("\d{10}")

print(pattern.findall(content.text))