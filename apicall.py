import json
import requests
import openai
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTg1ODFkMjQtYmJhOC00MDZiLTgyNjYtMjMwZmNkNjM4YTBkIiwidHlwZSI6ImFwaV90b2tlbiJ9.nQT0Pbpc8zm5HfFV8bHPqDWW8keO2XBpaMPhHqYb3XA"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Badri"
}

#response = requests.post(url, json=payload, headers=headers)

#result = json.loads(response.text)
#print(result['openai']['generated_text'])

def talktoai(query):
    payload["text"]=query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    speak(result['openai']['generated_text'])


