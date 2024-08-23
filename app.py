import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import openai

# Load environment variables from .env
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    # Use GPT model to summarize the input text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following book: {text}"}
        ],
        max_tokens=300
    )
    return response.choices[0].message['content']

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        book_text = request.form['book_text']
        summary = summarize_text(book_text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)