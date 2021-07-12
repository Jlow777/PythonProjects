import requests
from twilio.rest import Client
import os
# AMd#65153Corgi
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACbc7d848bba5ffa008ed8d6cdc9a676cb"
auth_token = "598d264af912efdce27aa2962534847e"
LATITUDE = 39.952583
LONGITUDE = -75.165222

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body="It's going to rain today :( bring an ☂️",
        from_="+14044767669",
        to="+14806886386")
    print(message.status)
