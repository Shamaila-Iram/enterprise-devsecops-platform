from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user")
def user():
    return jsonify({
        "id": 101,
        "name": "DevSecOps User",
        "role": "engineer"
    })

@app.route("/health")
def health():
    return jsonify({"status": "user-service-ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)