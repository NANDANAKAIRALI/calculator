import re

post=input("ENTER THE SOCIAL MEDIA POST...")
pattern = r'#\w+'
print("THE HASHTAGS ARE ",end="")
print(re.findall(pattern, post))
