from flask import Flask, request, jsonify
from triage import classify_issue, generate_reply
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    category, priority = classify_issue(user_message)

    response = {
        "reply": "Issue received successfully",
        "category": category,
        "priority": priority
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

