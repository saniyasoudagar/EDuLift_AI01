import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guidance", methods=["POST"])
def guidance():
    data = request.json

    prompt = f"""
    You are EduLift AI, a friendly academic and career mentor.

    Student Level: {data['level']}
    Interests: {data['interest']}
    Career Goal: {data['goal']}

    Give:
    1. A simple study plan
    2. Skills to focus on
    3. Career roadmap
    Use easy and motivating language.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {
        "role": "system",
        "content": "You are a highly experienced academic counselor and career mentor who gives deep, structured, and practical guidance."
    },
    {
        "role": "user",
        "content": prompt
    }
]
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    print("🚀 EduLift AI server running...")
    app.run(host="0.0.0.0", port=10000)

prompt = f"""
You are EduLift AI — a senior academic advisor and career strategist.

Your role:
- Guide students like a mentor, not a chatbot
- Give deep, structured, realistic guidance
- Think long-term (5–10 years impact)

Student Profile:
Education Level: {data['level']}
Interests: {data['interest']}
Career Goal: {data['goal']}

Now provide guidance in this EXACT structure:

1️⃣ Student Understanding
- Briefly explain the student's current situation
- Mention strengths and gaps

2️⃣ Personalized Study Strategy
- What subjects to focus on
- Daily and weekly study plan
- Learning methods (projects, practice, theory)

3️⃣ Skill Development Roadmap
- Technical skills
- Soft skills
- Tools or technologies to learn

4️⃣ Career Path Guidance
- Entry-level roles
- Mid-level growth
- Long-term career vision

5️⃣ Common Mistakes to Avoid
- Academic mistakes
- Career mistakes

6️⃣ Motivation & Reality Check
- Honest advice
- Encouraging but realistic tone

Rules:
- Use simple English
- Be clear and confident
- No emojis
- No over-promising
"""
