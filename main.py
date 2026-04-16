import requests
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# ========================
# GitHub API
# ========================
def get_user_data(username):
    return requests.get(
        f"https://api.github.com/users/{username}",
        headers=headers
    ).json()

def get_repos(username):
    return requests.get(
        f"https://api.github.com/users/{username}/repos?per_page=100",
        headers=headers
    ).json()

# ========================
# Stats Processing
# ========================
def process_repos(repos):
    total_stars = 0
    languages = {}

    for repo in repos:
        total_stars += repo.get("stargazers_count", 0)

        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

    return {
        "total_stars": total_stars,
        "top_languages": top_languages[:5]
    }

# ========================
# LLM Setup
# ========================
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# ========================
# Analyze
# ========================
def analyze_user(username):
    user = get_user_data(username)
    repos = get_repos(username)

    stats = process_repos(repos)

    cleaned = []
    for r in repos[:10]:
        cleaned.append({
            "name": r.get("name"),
            "language": r.get("language"),
            "stars": r.get("stargazers_count")
        })

    prompt = f"""
You are a senior GitHub analyst and tech recruiter.

Analyze this developer professionally.

PROFILE:
Name: {user.get('name')}
Bio: {user.get('bio')}
Followers: {user.get('followers')}
Public Repos: {user.get('public_repos')}

STATS:
Total Stars: {stats['total_stars']}
Top Languages: {stats['top_languages']}

TOP REPOS:
{cleaned}

Return output STRICTLY in this format:

## 👤 Profile Summary
(2-3 lines professional summary)

## 🛠️ Skills
- bullet points

## ⚙️ Tech Stack
- bullet points

## 📊 Experience Level
(Beginner / Intermediate / Advanced + reason)

## 💪 Strengths
- bullet points

## ⚠️ Weaknesses
- bullet points

## 🚀 Recommendations
- bullet points

## 🏆 Overall Score
Give score out of 10 with explanation
"""

    try:
        res = llm.invoke(prompt)

        return {
            "username": username,
            "analysis": res.content,
            "stats": stats
        }

    except Exception as e:
        return {
            "username": username,
            "analysis": str(e),
            "stats": stats
        }

# ========================
# Compare
# ========================
def compare_users(usernames):
    all_data = []

    for u in usernames:
        user = get_user_data(u)
        repos = get_repos(u)
        stats = process_repos(repos)

        all_data.append({
            "username": u,
            "followers": user.get("followers"),
            "repos": user.get("public_repos"),
            "stars": stats["total_stars"],
            "languages": stats["top_languages"]
        })

    prompt = f"""
You are a senior developer recruiter.

Compare these GitHub developers:

{all_data}

Give:

## ⚔️ Comparison Table
## 🏆 Best Developer
## 💼 Hiring Recommendation
## 🧠 Detailed Reasoning
"""

    res = llm.invoke(prompt)

    return res.content
