# Vayara AI Website

An intelligent AI assistant website built with Flask and integrated with Google's Gemini AI.

## Features

- 🏠 Welcome page with branding
- 🏡 Home page with inspirational quote
- 💬 Interactive chat interface with real AI responses
- ℹ️ About page with features
- 🤖 AI-powered responses using Google Gemini
- 📱 Responsive design
- 🚀 Production-ready with WSGI server

## Quick Deploy

### Heroku
1. Fork this repository
2. Connect to Heroku
3. Set environment variable: `GOOGLE_API_KEY=your_api_key`
4. Deploy

### Railway
1. Fork this repository
2. Connect to Railway
3. Set environment variable: `GOOGLE_API_KEY=your_api_key`
4. Deploy

### Render
1. Fork this repository
2. Connect to Render
3. Set environment variable: `GOOGLE_API_KEY=your_api_key`
4. Deploy

## Local Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd VayaraAI-Website
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set environment variable:
```bash
export GOOGLE_API_KEY=your_google_api_key_here
```

5. Run the application:
```bash
python app.py
```

6. Open http://localhost:5000 in your browser

## Project Structure

```
VayaraAI-Website/
├── app.py              # Flask application
├── wsgi.py             # WSGI entry point
├── requirements.txt    # Python dependencies
├── Procfile           # Process file for deployment
├── runtime.txt        # Python version
├── .env.example       # Environment variables example
├── templates/         # HTML templates
│   ├── index.html    # Welcome page
│   ├── home.html     # Home page
│   ├── chat.html     # Chat interface
│   └── about.html    # About page
└── static/           # Static assets
    ├── style.css     # Styles
    ├── script.js     # JavaScript
    └── logo.png      # Logo image
```

## Environment Variables

- `GOOGLE_API_KEY`: Your Google Gemini API key (required)
- `PORT`: Port number (optional, defaults to 5000)

## License

MIT License
