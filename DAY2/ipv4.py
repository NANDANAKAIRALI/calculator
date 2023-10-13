import re
ipv4= input("ENTER THE IPv4 ADDRESS")
pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
if re.match(pattern, ipv4):
    print(f"{ipv4} is a valid IPv4 address.")
else:
    print(f"{ipv4} is not a valid IPv4 address.")
