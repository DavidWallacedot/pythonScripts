import requests, sys, json
if len(sys.argv)<2:
	print('Usage: quick weather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
weatherData= json.loads(response.text)
w = weatherData['list']
print('Current weatehr in %s:'%(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print("Tommorow")
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print('Day after tommorow')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])ls

