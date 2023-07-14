import requests

parameters = {
    "amount":10,
    "type":"boolean"
}

# s303-1-1-1 send request to endpoint and get questions
response = requests.get("https://opentdb.com/api.php",
                        params=parameters)
response.raise_for_status()

# s303-1-1-2 parse the response and get question context
data = response.json()
print(data["results"])

