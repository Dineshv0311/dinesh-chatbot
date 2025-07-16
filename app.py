from flask import Flask, render_template, request, jsonify, send_file
import requests
import datetime
import os
import sqlite3

app = Flask(__name__)
DB_PATH = "chatlog.db"

# 🔧 Create chats table if not exists
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                user_message TEXT,
                bot_reply TEXT
            )
        """)
        conn.commit()

# 🏠 Home page
@app.route("/")
def home():
    return render_template("index.html")

# 📬 Handle user message
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    print(f"\n🧑 User: {user_input}")

    try:
        # Call local Ollama API
        response = requests.post(
            "https://a988e715d131.ngrok-free.app",
            json={
                "model": "dinesh",
                "prompt": user_input,
                "stream": False
            }
        )
        response.raise_for_status()
        response_json = response.json()
        bot_reply = response_json.get("response", "").strip()
        print(f"🤖 Bot: {bot_reply}")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to .txt file
        with open("chat_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n[{timestamp}]\nUser: {user_input}\nBot: {bot_reply}\n")

        # Save to SQLite DB
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                INSERT INTO chats (timestamp, user_message, bot_reply)
                VALUES (?, ?, ?)
            """, (timestamp, user_input, bot_reply))
            conn.commit()

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("⚠️ Error:", e)
        return jsonify({"reply": "⚠️ Error talking to local AI model."})

# 📄 View plain .txt log
@app.route("/view-log")
def view_log():
    try:
        if not os.path.exists("chat_log.txt"):
            return "<h2>No chat log found.</h2>"
        with open("chat_log.txt", "r", encoding="utf-8") as f:
            content = f.read().replace("\n", "<br>")
        return f"<h2>📝 Chat Log</h2><div style='white-space: pre-wrap; padding: 20px; font-family: monospace;'>{content}</div>"
    except Exception as e:
        return f"<p>Error loading log: {e}</p>"

# ⬇ Download .txt file
@app.route("/download-log")
def download_log():
    try:
        if not os.path.exists("chat_log.txt"):
            return "Log file not found", 404
        return send_file("chat_log.txt", as_attachment=True)
    except Exception as e:
        return f"Error downloading log: {e}", 500

# 🗃 View chat history from DB
@app.route("/view-db")
def view_db():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            rows = conn.execute("SELECT timestamp, user_message, bot_reply FROM chats ORDER BY id DESC").fetchall()

        if not rows:
            return "<h2>No chats saved yet.</h2>"

        html = "<h2>📚 Chat History (from Database)</h2><div style='font-family: monospace; padding: 20px;'>"
        for timestamp, user, bot in rows:
            html += f"<strong>[{timestamp}]</strong><br>"
            html += f"<span style='color: blue;'>You:</span> {user}<br>"
            html += f"<span style='color: green;'>Bot:</span> {bot}<br><br>"
        html += "</div>"
        return html

    except Exception as e:
        return f"<p>Error reading database: {e}</p>"

# 🚀 Run the server

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Flask server running at http://0.0.0.0:{port}")
    app.run(debug=True, host="0.0.0.0", port=port)

