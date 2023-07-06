import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "1102f19cfbb21408a7309adf2ab41c63"
account_sid = "AC28e10ee9c43f8e1905e34d944430affd"
auth_token = "6fd134e05cef1af00f9bfcb05eece822"

weather_params = {
    "lat": 26.462891,
    "lon": 80.323357,
    "appid": api_key,
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]
if int(condition_code) < 700:
    will_rain = True

if will_rain is False:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                body="It's gonna rain today. Remember to bring an umbrella ☂️☂️☂️",
                from_="+14344236766",
                to="+919140593106")
    print(message.status)