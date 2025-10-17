from openai import OpenAI
import os
import json

def generate_app_code(brief, app_dir):
    """
    Uses AI Pipe (OpenAI-compatible) API to generate app code from the brief.
    Saves the generated code inside `app_dir`.
    """

    # Load API key from config.json
    with open("config.json") as f:
        config = json.load(f)
    OPENAI_API_KEY = config["openai_api_key"]

    # 👇 Tell OpenAI library to use AI Pipe’s base URL
    client = OpenAI(
        api_key=OPENAI_API_KEY,
        base_url="https://aipipe.org/openai/v1"
    )

    # Log message (so you can confirm in terminal)
    print("✅ Using AI Pipe API via https://aipipe.org/openai/v1")

    prompt = f"Generate a simple web app in HTML, CSS, and JS that does the following:\n{brief}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # works with AI Pipe
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    app_code = response.choices[0].message.content

    os.makedirs(app_dir, exist_ok=True)
    with open(os.path.join(app_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(app_code)

    print(f"✅ App generated successfully in: {app_dir}")
