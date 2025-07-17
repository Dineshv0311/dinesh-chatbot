# 🧠 Dinesh AI Chatbot — Powered by LLaMA 3 via Ollama

An open-source, locally hosted chatbot built using Python, Flask, and the powerful LLaMA 3 model via Ollama. Designed with a clean and responsive web interface, this chatbot runs 100% on your own system — no internet, no API keys, no data leaks.

## 🚀 Features

- 🔒 100% local inference using Ollama + LLaMA 3.2
- 🧰 Backend built with lightweight Flask framework
- 🎨 Clean and modern UI with HTML, CSS (custom styled)
- ⚡ Real-time interaction with an LLM (no API calls)
- 🌐 Expose to the web easily via ngrok
- 🧠 Model can be customized (this repo uses a renamed llama3 model `dinesh`)
- 📝 Modular codebase for easy extension

## 📸 Live Demo

Coming soon (can be hosted via [Render](( https://60279faee806.ngrok-free.app)) or shared over [ngrok](https://ngrok.com/))  
→ Example: `https://02b4a418754.ngrok-free.app`

## 🛠️ Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Ollama](https://ollama.com/) (for running LLaMA locally)
- HTML + CSS (customized)
- [ngrok](https://ngrok.com/) (optional for public access)

## 📂 Project Structure

llm-ui/
├── app.py # Flask backend
├── requirements.txt # Dependencies
├── .render.yaml # For deployment on Render
├── static/
│ └── style.css # UI styles
├── templates/
│ └── index.html # Main chat UI
├── chatlog.db # (Optional) SQLite log
├── chat_log.txt # (Optional) Log file
└── ngrok.exe # (Optional) ngrok tunnel tool

bash
Copy
Edit

## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Dineshv0311/llm-ui.git
cd llm-ui
2. Install Python dependencies
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
3. Run the Ollama model
Make sure you have Ollama installed and the model pulled:

bash
Copy
Edit
ollama run dinesh
If you haven’t pulled it yet:
ollama pull llama3

4. Start the Flask App
bash
Copy
Edit
python app.py
Open browser → http://localhost:5000

5. (Optional) Share Online via ngrok
bash
Copy
Edit
ngrok http 5000
Copy the URL (e.g., https://abc123.ngrok-free.app) and share it with others.

🌐 Deployment on Render (Optional)
This repo includes .render.yaml for 1-click deployment on Render. You can host the Flask app online and connect it to your local Ollama model via ngrok.

📦 Built By
Dinesh V — GitHub | LinkedIn
Customized and developed as a personal AI assistant using open LLMs

📄 License
MIT License — free to use and modify.
