import re
text="""Elon musk's phone number is 9991116666,
call him if you have any questions on dodgecoin.
Tesla's revenue is 40 billion.
Tesla's CFO number (999)-333-7777 999-333-777"""

"""pattern="\d{10}"

print(re.findall(pattern,text))"""

pattern=re.compile("Elon")
print(pattern.match("the Elon musk"))
#match is used to find the first element of the selected text
