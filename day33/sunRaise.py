import requests
from datetime import datetime

MY_LAT = 51.50
MY_LONG = -0.1277

#s299-1-1-1 define the parameters for API
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

#s299-1-1-2 call API with parameter
response = requests.get(url="https://api.sunrise-sunset.org/json",
                        params=parameters)

#s299-1-1-3 parse the response
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
