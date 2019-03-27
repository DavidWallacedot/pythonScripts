import shelve, pyperclip, sys

#mcb.py - saves and loads pieces of text to the clipboard
#usage: py.exe mcb.py save <keyword> - saves clipboard to keyword
# 	py.exe mcb.py list - loads all keywords to clipboard
#	py.exe mcb.py <keyword> -loads keyword to clipboard
mcbShelf = shelve.open('mcb')
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
	print('clipboard loaded to keyword')
elif len(sys.argv) == 2:
	if sys.argv[1].lower() =='list':	
		pyperclip.copy(str(list(mcbShelf.keys())))
		print('list loaded to clipboard')		
		print('list of keys')
		print(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		print('value loaded to clipboard')
mcbShelf.close()
