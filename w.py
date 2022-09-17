import requests


try :
	wa = "https://ipinfo.io"
	res = requests.get(wa)
	data = res.json()
	city = data["city"]
	state = data["region"]
	
	loc = data["loc"]

	


	a1 = "https://api.openweathermap.org/data/2.5/weather"
	a2 = "?q=" + city
	a3 = "&appid=" + "696f758d0711d9b25f219e59ea85da38"
	a4 = "&units=" + "metric"
	wa = a1 + a2 +a3 + a4
	res = requests.get(wa)
   #	print(res)
	data = res.json()
	# print(data)

	temp = data["main"]["temp"]
	

except Exception as e:
	print("issue ",e)