from flask import Flask, request, jsonify
import os
import json
from generator.llm_generator import generate_app_code
from github_tools.github_automation import create_and_deploy_repo

app = Flask(__name__)

# Load secret and GitHub token


STUDENT_SECRET = os.environ.get("SECRET")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


@app.route('/api-endpoint', methods=['POST'])
def api_endpoint():
    try:
        data = request.get_json()

        # 1️⃣ Verify the secret
        if data.get("secret") != STUDENT_SECRET:
            return jsonify({"error": "Invalid secret"}), 403

        email = data.get("email")
        brief = data.get("brief")
        task = data.get("task")
        round_num = data.get("round")
        evaluation_url = data.get("evaluation_url")
        nonce = data.get("nonce")

        # 2️⃣ Generate code using LLM
        app_dir = f"generated_apps/{task}"
        os.makedirs(app_dir, exist_ok=True)
        generate_app_code(brief, app_dir)

        # 3️⃣ Create GitHub repo & deploy
        repo_url, commit_sha, pages_url = create_and_deploy_repo(task, app_dir)

        # 4️⃣ Respond to evaluation API
        response_payload = {
            "email": email,
            "task": task,
            "round": round_num,
            "nonce": nonce,
            "repo_url": repo_url,
            "commit_sha": commit_sha,
            "pages_url": pages_url
        }

        # Normally you’d send this to evaluation_url using requests.post()
        # But for testing, just return JSON response
        return jsonify(response_payload), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
