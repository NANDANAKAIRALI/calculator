#Write a regex pattern to find all URLs in a text.
#"Here are some example URLs: http://example.com, https://www.example.org, ftp://ftp.example.net"
import re

text =input("Enter the text")
pattern =r'\b(?:https?|ftp):\/\/\S+'
#print(pattern)
urls =re.findall(pattern, text)

print(urls)

'''import re

text = "Here are some example URLs: http://example.com, https://www.example.org, ftp://ftp.example.net"
pattern = r'\b(?:https?|ftp):\/\/\S+'
urls = re.findall(pattern, text)

print(urls)'''


