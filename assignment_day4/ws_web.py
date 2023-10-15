from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Your User Agent',
    'Custom-Header': 'Custom Value'}

response=requests.get("https://news.ycombinator.com/",headers)
contents=response.text
soup=BeautifulSoup(contents,"html.parser")

headings= soup.find_all(class_='athing')
headings_text = [heading.text for heading in headings]
print(headings_text)
'''for heading in headings:
    headings_text = [heading.text]'''



score= soup.find_all(class_='score')
score_text = [s.text for s in score]
print(score_text)

site= soup.find_all(class_='sitebit comhead')
site_text = [x.text for x in site]
print(site_text)