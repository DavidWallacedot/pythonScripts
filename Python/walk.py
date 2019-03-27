import os
for foldername, subfolders, filenames in os.walk('/home/david/bin/ericson'):
	print('The current folder is '+foldername)
	for subfolder in subfolders:
		print('Sub folder of '+foldername+':'+subfolder)
	for filename in filenames:
		print('file inside'+foldername+':'+filename)
	print(' ')
