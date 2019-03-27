catsList = []
while True:
	print('Enter the name of cat '+str(len(catsList)+1)+'( Or enter nothing to stop):')
	name = input()
	if name == '':
		break
	catsList = catsList + [name]
print('the cat names are')
for name in catsList:
	print(''+name)
