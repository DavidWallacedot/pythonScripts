import sys, webbrowser,pyperclip
if len(sys.argv)>1:
	address = ' '.join(sys.argv[1:])
else:
	address = clipboard.paste()

webbrowser.open('https://www.google.com/maps/place/'+ address)
