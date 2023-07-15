import requests
import html

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
# s304-1-1-1 get question content which contains html special char
question_content = data["results"][0]["question"]
print(question_content)
# s304-1-1-2 using html.unescape func,convert content to normal
q_text = html.unescape(question_content)
print(q_text)

