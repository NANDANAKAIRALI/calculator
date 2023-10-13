import re
text=input("ENTER THE EMAIL ID")
pattern=r"\w*@(?!.*(?:yahoo|hotmail))\w*\.com|\w*@(?!.*(?:yahoo|hotmail))\w*\.in|\w*@(?!.*(?:yahoo|hotmail))\w*\.org"

if(re.match(pattern,text)):
    print(f"{text} is a valid email address.")
else:
    print(f"{text} is not a valid email address.")

