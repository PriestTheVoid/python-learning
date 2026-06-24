import requests

# Адрес твоего сервера, который ты прописал в батнике
URL = "http://127.0.0.1:8000/v1/chat/completions"

# Настройки запроса (тело в формате JSON)
payload = {
    "model": "gemma-4", # Имя модели (для llama.cpp тут можно писать что угодно)
    "messages": [
        {"role": "system", "content": "Ты веселый ИИ-ассистент витубера."},
        {"role": "user", "content": "Привет! Как меня слышно?"}
    ],
    "temperature": 0.7 # Степень креативности модели (от 0 до 1)
}

print("Отправляю запрос к Riso...")

# Посылаем POST-запрос на локалхост
response = requests.post(URL, json=payload)

# Проверяем, что сервер ответил успешно (код 200)
if response.status_code == 200:
    data = response.json()
    # Вытаскиваем чистый текст ответа из сложной структуры JSON
    ai_text = data['choices'][0]['message']['content']
    print(f"\nОтвет ИИ:\n{ai_text}")
else:
    print(f"Ошибка! Сервер вернул код: {response.status_code}")
    print(response.text)