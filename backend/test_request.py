import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "What is health insurance?"}
response = requests.post(url, json=data)

print("Response:", response.json())
