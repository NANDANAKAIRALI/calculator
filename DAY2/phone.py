import re
ph_no=input("ENTER THE PHONE NUMBER")

pattern="\d{3}-\d{3}-\d{3}|\d{10}|\(\d{3}\)-\d{3}-\d{4}|\(\d{3}\)\S-\d{3}-\d{4}"

if re.match(pattern,ph_no):
    print(f"{ph_no} is a valid phone number.")
else:
    print(f"{ph_no} is not a valid phone number.")
