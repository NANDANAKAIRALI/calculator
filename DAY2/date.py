import re

date = input("ENTER THE DATE")
pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}'

if re.match(pattern,date):
    print(f"{date} is a valid date.")
else:
    print(f"{date} is not a valid date.")