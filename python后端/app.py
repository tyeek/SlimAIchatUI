from flask import Flask, request, Response
from openai import OpenAI
import os

app = Flask(__name__)

# 设置 OpenAI API 密钥
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-4b165e2c3a74299*****************"
)


@app.route('/', methods=['GET'])
def index():
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "未找到 index.html 文件", 404


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')

    def generate():
        try:
            response = client.chat.completions.create(
                model="moonshotai/moonlight-16b-a3b-instruct:free",
                messages=[{"role": "user", "content": message}],
                stream=True
            )
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    yield content
        except Exception as e:
            print(f"Error: {e}")

    return Response(generate(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True)
    