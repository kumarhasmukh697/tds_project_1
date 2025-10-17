🚀 LLM-Based Code Deployment Project
📘 Overview

This project is built as part of the IITM BS Degree in Data Science coursework (TDS Project).
It implements an automated system that:

Accepts a JSON request through a Flask API.

Uses an LLM (AI Pipe) to generate a simple web app based on the given brief.

Automatically creates a new GitHub repository, pushes the generated code,
and publishes it using GitHub Pages.

Returns a JSON response containing repo details and deployment URLs.

🧩 Features

✅ Flask-based API endpoint (/api-endpoint)
✅ Integration with AI Pipe (OpenAI-compatible free LLM)
✅ Automatic GitHub repo creation & code push
✅ GitHub Pages deployment
✅ JSON-based communication for evaluation rounds

🗂️ Project Structure
llm_code_deployment/
│
├── app.py                   # Flask entry point (main API)
├── config.json               # Secrets and tokens (ignored in Git)
├── requirements.txt          # Python dependencies
├── Procfile                  # Render deployment config
│
├── generator/
│   └── llm_generator.py      # Calls AI Pipe to generate code
│
├── github_tools/
│   └── github_automation.py  # Handles repo creation & commits
│
├── utils/
│   └── helper.py             # Helper functions
│
└── generated_apps/           # Stores AI-generated apps
    └── test-task/
        ├── index.html
        ├── style.css
        └── script.js

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your_username>/llm-code-deployment.git
cd llm-code-deployment

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate        # (Windows)
# OR
source venv/bin/activate     # (Mac / Linux)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure config.json
{
  "secret": "test123",
  "github_token": "ghp_yourGitHubTokenHere",
  "github_username": "your_github_username",
  "openai_api_key": "your_AI_Pipe_token_here"
}


⚠️ Add config.json to .gitignore before pushing to GitHub.

▶️ Run the App Locally
python app.py


Access it at:
👉 http://127.0.0.1:5000/

🧪 Test the API Endpoint

Example request:

curl http://127.0.0.1:5000/api-endpoint \
-H "Content-Type: application/json" \
-d "{\"email\":\"22f2001125@ds.study.iitm.ac.in\",\"secret\":\"test123\",\"task\":\"test-task\",\"round\":1,\"nonce\":\"abc123\",\"brief\":\"Create a simple Hello World webpage\",\"evaluation_url\":\"https://example.com/notify\"}"


Expected response:

{
  "email": "22f2001125@ds.study.iitm.ac.in",
  "task": "test-task",
  "round": 1,
  "nonce": "abc123",
  "repo_url": "https://github.com/<username>/test-task",
  "commit_sha": "abc12345",
  "pages_url": "https://<username>.github.io/test-task/"
}

🌐 Deploy on Render (Free Hosting)

Push this project to your GitHub.

Go to https://render.com
 → New Web Service.

Connect your repo.

Fill in:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Click Deploy.

Your public API URL will look like:

https://llm-code-deployment.onrender.com/api-endpoint

🔐 Environment & Security

Secrets (tokens, keys) stored in config.json → not uploaded to GitHub.

.gitignore should include:

.env
config.json
__pycache__/
*.pyc

🧠 Example Workflow
Step	Description
1️⃣	Evaluator sends a JSON request with task & brief
2️⃣	Flask API verifies secret and triggers generation
3️⃣	AI Pipe creates HTML/CSS/JS app
4️⃣	Code is pushed to GitHub and published
5️⃣	API returns repo + deployment links
🧾 Example Output

👨‍💻 Author

Name: Hasmukh Kumar
Email: 22f2001125@ds.study.iitm.ac.in

GitHub: @kumarhasmukh697

✅ This project successfully integrates AI Pipe LLM, Flask, and GitHub automation for end-to-end web-app generation and deployment.