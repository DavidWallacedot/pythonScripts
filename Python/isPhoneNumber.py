import re
def isPhoneNumber():
	
	regexOb= re.compile(r'/d{3}-/d{3}-/d{4}')
	mo = regexOb.search('Hey my number is 615-542-9449, Hey my number is 901-896-9073')
	print("Phone number found:"+ mo.expand())
	"""if len(text) !=12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True"""
"""def takeInMessage(message):
	for i in range(len(message)):
		phoneNumber= message[i:i+12]
		if isPhoneNumber(phoneNumber):
			print('Phone number found '+phoneNumber)
	
"""
isPhoneNumber()
