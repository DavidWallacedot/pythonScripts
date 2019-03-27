birthdays = {'David':'Feb15','Faith':'Jan23'}
while True:
	print('Input the name person or blank to quit')
	name = ''	
	name = input()
	if name =='':
		break
	if name in birthdays:
		print('the birthday for '+name+' is '+birthdays[name])
	else:
		print('That peron does not exist in our DB')
		print('Please input the bd of the person')
		birthdays [name]= input()
	
