import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Use environment variable for API key in production
api_key = os.environ.get("GOOGLE_API_KEY", "AIzaSyCsNZtfWz4jIvbNPjxFSYubhaa2jI7y5ZU")
os.environ["GOOGLE_API_KEY"] = api_key
client = genai.Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ask', methods=['POST'])
def ask_vayara():
    data = request.json
    user_input = data.get('question', '').strip()
    
    if not user_input:
        return jsonify({'error': 'No question provided'}), 400
    
    if "vayara" in user_input.lower():
        return jsonify({'response': 'Haan, main Vayara hoon, aapki smart assistant. Kaise madad kar sakti hoon?'})
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
        )
        clean_response = response.text.replace('*', '')
        return jsonify({'response': clean_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
