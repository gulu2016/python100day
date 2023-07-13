import requests

# s296-1-1-1 send a request to endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# s296-1-1-2 get the response
print(response)

# s297-1-1-1 raise the error if the statue is not 200
response.raise_for_status()

# s297-1-1-2 get response data, it's in dict format
data = response.json()

# s297-1-1-3 get longtitude and latitude
longtitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longtitude,latitude)

print(iss_position)