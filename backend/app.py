import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from triage import classify_issue, generate_reply
app = Flask(__name__)
CORS(app)
def init_db():
    conn = sqlite3.connect("tickets.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            issue TEXT,
            category TEXT,
            priority TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_ticket(issue, category, priority):
    conn = sqlite3.connect("tickets.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tickets(issue, category, priority) VALUES (?, ?, ?)",
        (issue, category, priority)
    )
    conn.commit()
    conn.close()


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    category, priority = classify_issue(user_message)
    reply = generate_reply(category)
    if priority == "High":
        create_ticket(user_message, category, priority)
        reply += "This looks like something that needs extra attention. I have created a support ticket — our IT team will reach out to you shortly."

    response = {
        "reply": reply
    }

    return jsonify(response)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

