array = []
with open("fallout.txt") as my_file:
	for line in my_file:
		if(line[0]=='x'):
			break
		else:
			array.append(line)
			print(line)

print("The number of items entered is : 	")
print(len(array))
#print("enter the index for the test password: ")

index = input("enter the index for the test password")
print (index)
numberOfCharMatches = input("enter the number of exact character matches:   ")
