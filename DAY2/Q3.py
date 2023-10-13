#Write a regex pattern to extract the domain
#(e.g., "example.com") from a URL like "https://www.example.com/page&quot;.

import re

url=input("Enter the url eg:https://www.example.com/page&quot;")
pattern = r"https?://(www\.)?([a-zA-Z0-9.-]+)"
domain = re.search(pattern, url).group(2)

print(domain)