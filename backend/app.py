from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    response = {
        "reply": "Backend server is working",
        "user_input": user_message
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
