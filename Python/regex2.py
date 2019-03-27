import re
regex = r"\d\d\d-\d\d\d-\d\d\d\d"
match = re.search(regex, "901-896-9034")
print(match.group(0))
