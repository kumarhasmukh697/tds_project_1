# 🚀 LLM-Based Code Deployment Project  

### 📘 Overview  
This project is part of the **IITM BS Degree in Data Science (TDS Project)**.  
It implements an automated Flask-based system that:  

1. Accepts a JSON request via an API.  
2. Uses an **LLM (AI Pipe)** to generate a web app based on the given *brief*.  
3. Automatically creates a **GitHub repository**, pushes the generated code,  
   and deploys it using **GitHub Pages**.  
4. Returns a JSON response containing repo and deployment details.  

---

## 🧩 Features  

✅ Flask-based API endpoint (`/api-endpoint`)  
✅ Integration with **AI Pipe (OpenAI-compatible free LLM)**  
✅ Automatic GitHub repo creation & deployment  
✅ GitHub Pages hosting  
✅ JSON-based communication for evaluation rounds  

---

## 🗂️ Project Structure  

llm_code_deployment/
│
├── app.py # Flask entry point (main API)
├── config.json # Secrets and tokens (ignored in Git)
├── requirements.txt # Python dependencies
├── Procfile # Render deployment config
│
├── generator/
│ └── llm_generator.py # Calls AI Pipe to generate code
│
├── github_tools/
│ └── github_automation.py # Handles repo creation & commits
│
├── utils/
│ └── helper.py # Helper functions
│
└── generated_apps/ # Stores AI-generated apps
└── test-task/
├── index.html
├── style.css
└── script.js



---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/<your_username>/llm-code-deployment.git
cd llm-code-deployment

python -m venv venv
venv\Scripts\activate        # (Windows)
# OR
source venv/bin/activate     # (Mac / Linux)


pip install -r requirements.txt


{
  "secret": "test123",
  "github_token": "ghp_yourGitHubTokenHere",
  "github_username": "your_github_username",
  "openai_api_key": "your_AI_Pipe_token_here"
}


python app.py


curl http://127.0.0.1:5000/api-endpoint \
-H "Content-Type: application/json" \
-d "{\"email\":\"22f2001125@ds.study.iitm.ac.in\",\"secret\":\"test123\",\"task\":\"test-task\",\"round\":1,\"nonce\":\"abc123\",\"brief\":\"Create a simple Hello World webpage\",\"evaluation_url\":\"https://example.com/notify\"}"



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

Connect your GitHub repo.

Fill the following details:



| Setting           | Value                             |
| ----------------- | --------------------------------- |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app`                |


Click Deploy 🚀

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
| Step | Description                                            |
| ---- | ------------------------------------------------------ |
| 1️⃣  | Evaluator sends a JSON request with task & brief       |
| 2️⃣  | Flask API verifies secret and triggers code generation |
| 3️⃣  | AI Pipe creates HTML/CSS/JS app                        |
| 4️⃣  | Code is pushed to GitHub and published                 |
| 5️⃣  | API returns repo + deployment links                    |


🧾 Example Output
{
  "email": "22f2001125@ds.study.iitm.ac.in",
  "task": "captcha-solver-001",
  "round": 1,
  "nonce": "abc123",
  "repo_url": "https://github.com/kumarhasmukh697/captcha-solver-001",
  "commit_sha": "db18a6602e5e539715a8a158319a24781741177e",
  "pages_url": "https://kumarhasmukh697.github.io/captcha-solver-001/"
}

👨‍💻 Author

Name: Hasmukh Kumar
Email: 22f2001125@ds.study.iitm.ac.in

GitHub: @kumarhasmukh697


✅ This project successfully integrates Flask, AI Pipe (OpenAI-compatible API), and GitHub automation for end-to-end LLM-based web app generation and deployment.


---

### 📌 Instructions:
1. Create a new file named **`README.md`** in your project root (same place as `app.py`).  
2. Paste the above content **exactly as-is**.  
3. Commit and push it:
   ```bash
   git add README.md
   git commit -m "Added project README"
   git push


