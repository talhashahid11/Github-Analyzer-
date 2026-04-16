# 🚀 GitHub Analyzer AI

An AI-powered GitHub profile analyzer that evaluates developers, provides deep insights, and compares multiple profiles using advanced LLMs.

---

## 🌟 Features

### 🔍 Profile Analysis

* Analyze any GitHub user in detail
* Extract skills, tech stack, and experience level
* Identify strengths and weaknesses
* Get AI-powered recommendations
* Overall developer scoring

### 📊 Advanced Insights

* Total stars count
* Top programming languages
* Repository-level analysis

### ⚔️ Profile Comparison

* Compare 2–3 GitHub users
* AI-based hiring recommendation
* Developer ranking & evaluation

---

## 🧠 Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **AI Model:** OpenRouter (GPT-3.5 Turbo)
* **Libraries:** LangChain, Requests, Python-dotenv

---

## 📁 Project Structure

```
github-analyzer/
│
├── main.py        # Core AI logic
├── api.py         # FastAPI backend
├── frontend.py    # Streamlit UI
├── .env           # API keys
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/github-analyzer.git
cd github-analyzer
```

---

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn streamlit langchain langchain-openai requests python-dotenv
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
OPENROUTER_API_KEY=your_openrouter_key
```

---

### 4️⃣ Run Backend

```bash
uvicorn api:app --reload

```

### 5️⃣ Run Frontend

```bash
streamlit run frontend.py
---

## 🎯 Example Use Cases

* Evaluate developer profiles
* Compare candidates for hiring
* Analyze GitHub activity
* Portfolio showcase project

---

## 🚀 Future Improvements

* 📊 Charts & visual analytics
* 👤 GitHub avatar integration
* 📈 Contribution graph analysis
* 🌐 Deploy as SaaS application

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 💡 Author

**Your Name**
GitHub: https://github.com/your-username

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
