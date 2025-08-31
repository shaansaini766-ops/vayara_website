import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize Google AI client only when needed
def get_ai_client():
    try:
        import google.generativeai as genai
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            return None
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-pro')
    except Exception as e:
        print(f"AI client error: {e}")
        return None

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
    try:
        data = request.json
        user_input = data.get('question', '').strip()
        
        if not user_input:
            return jsonify({'error': 'No question provided'}), 400
        
        if "vayara" in user_input.lower():
            return jsonify({'response': 'Haan, main Vayara hoon, aapki smart assistant. Kaise madad kar sakti hoon?'})
        
        # Get AI client
        model = get_ai_client()
        if not model:
            return jsonify({'response': 'AI service temporarily unavailable. Please try again later.'})
        
        response = model.generate_content(user_input)
        clean_response = response.text.replace('*', '')
        return jsonify({'response': clean_response})
        
    except Exception as e:
        print(f"Error in ask_vayara: {e}")
        return jsonify({'response': 'Sorry, I encountered an error. Please try again.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
