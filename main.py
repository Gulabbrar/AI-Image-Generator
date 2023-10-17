from flask import Flask, jsonify, request, render_template
import openai
from config import key

app = Flask(__name__)

openai.api_key = key


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/generateimages/<prompt>', methods=['GET', 'POST'])
def generate(prompt):
  if request.method == 'POST':
    response = openai.Image.create(prompt=prompt, n=3, size="256x256")
    image_urls = [img['url'] for img in response['data']]
    return jsonify(image_urls)
  else:
    # Handle GET requests if needed
    return "GET requests are allowed here."


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
