import re
text=input("ENTER THE TEXT")
pattern="\d+"

print("THE NUMBERS ARE ",end="")
print(re.findall(pattern,text))

