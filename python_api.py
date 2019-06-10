import requests
import json

city_name="Tokyo"
API_KEY = "0a5357d6b04726d418aad4cca2202999"
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ja&appid={key}"

url = api.format(city = city_name, key = API_KEY)
print(url)
response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)
print(jsonText)
