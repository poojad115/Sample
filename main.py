import requests, datetime
api_key = "9b5b31aa38f43c9261237d1d937ec234"
api_url = "http://api.openweathermap.org/data/2.5/weather"
city_name = input("Enter city name : ")
url = api_url + "?q=" + city_name + "&appid=" + api_key
current_datetime = datetime.datetime.now()
day = current_datetime.day
response = requests.get(url)
weather_Details = response.json()

if day > 1:
    for index in range(2, day):
        if (day % index) == 0:

            weather_Details = "Date is not prime so no date"
            print(weather_Details)
            break
        else:
            print(weather_Details)
            break
else:
    weather_Details = "Date is not prime so no date"
    print(weather_Details)
