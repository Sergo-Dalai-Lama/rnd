# my_random.py
import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

if __name__ == "__main__":
    print("⚡ Запуск сервера...")  # Это должно появиться в консоли
    app.run(host='0.0.0.0', port=5000, debug=True)
    print("🚀 Сервер работает")  # Если это не видно - app.run() не сработал

def generate_number():
    return random.randint(1, 100)

@app.route('/api/random', methods=['GET'])
def get_random():
    number = generate_number()
    with open("rnd.txt", "w") as f:
        f.write(f"{number}")
    return jsonify({"number": number})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)