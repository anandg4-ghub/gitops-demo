from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "gitops-demo",
        "version": os.getenv("APP_VERSION", "2.0.0"),
        "message": "Hello from the GitOps pipeline! 🚀",
        "environment": "production",
        "team": "SCP Platform"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
