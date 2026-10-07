import requests


url = "http://127.0.0.1:8000/api/v1/chat"

payload = {
    "messages": [
        {
            "role": "system",
            "content": "你是一个专业 AI 助手"
        },
        {
            "role": "user",
            "content": "什么是 AI Agent？"
        }
    ],
    "model": "deepseek-chat",
    "temperature": 0.7,
    "stream": False,
    "session_id": "c_10001",
    "user_id": "u_10001",
    "metadata": {
        "client": "python-requests"
    }
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())