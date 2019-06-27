import requests
import json

#city_name="Tokyo"
API_KEY = "0a5357d6b04726d418aad4cca2202999"
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ja&appid={key}"


#print(url)
cities=["Tokyo,JP","London,UK"]



#jsonText = json.dumps(data, indent=4)#json.dumpでjson型に変換
#print(data)
#print(jsonText)


for city_name in cities:
    url = api.format(city = city_name, key = API_KEY)
    response = requests.get(url)
    data = json.loads(response.text)
    print("+ 都市=",data["name"])
    print("| 天気=", data["weather"])
    print(" ")
