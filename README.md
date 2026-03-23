<img width="2133" height="752" alt="heroDesktopBgV2" src="https://github.com/user-attachments/assets/b932bca8-f78c-4d41-a63f-ef58de9fadcc" />


# Track 1 - Build and Deploy AI Agents
## 💰 Financial Risk Classifier Agent

An AI-powered financial analysis agent that evaluates user-provided financial text and classifies risk levels using Google Gemini. The system provides structured insights along with actionable improvement suggestions.

---
## 📌 Problem Statement

- Many individuals struggle to understand their financial health because:
-Financial information is often unstructured
- People don’t know how to assess risk
- Existing tools require manual calculations
  
👉 This leads to:
- Poor financial decisions
- Debt accumulation
- Lack of planning

---

## 🚀 Proposed Solution
We built an AI-powered Financial Risk Classifier Agent that:
- Takes natural language financial input
- Analyzes income, expenses, and liabilities
- Classifies financial risk into:
```
  1. Low
  2. Medium
  3. High
````

This provides:
- Clear reasoning
- Actionable improvements
- Stability planning
  
#### 💡 🟨 WHY (Why this matters)
- Financial literacy is low globally
- Most people think in natural language, not numbers

### 👉 This system acts like a personal financial advisor powered by AI

---

## 🚀 Live Demo

#### 🔗 API Base URL:
https://financial-risk-agent-1059652519537.asia-south1.run.app

<img width="1920" height="932" alt="Root page" src="https://github.com/user-attachments/assets/e651113b-3331-4bd0-9691-97ce63b30e03" />


#### 🔗 Swagger Docs:
https://financial-risk-agent-1059652519537.asia-south1.run.app/docs

<img width="1920" height="1012" alt="Swagger UI" src="https://github.com/user-attachments/assets/5118f504-3f2c-46ea-87d4-ec62d672795e" />


#### 🔗 UI (Optional):
https://financial-risk-agent-1059652519537.asia-south1.run.app/ui

<img width="1615" height="825" alt="UI" src="https://github.com/user-attachments/assets/b424456a-a42f-42cd-a738-a0851d7f2daa" />

---

## 🎯 Features
- 🧠 Financial risk classification (Low / Medium / High)
- 📊 Structured JSON responses
- ✅ Actionable improvement suggestions
- 📈 Stability planning guidance
- ⚡ FastAPI backend with Cloud Run deployment
- 🤖 Powered by Google Gemini
- 🧩 ADK agent structure included

---

## 🗝 API Endpoint
### POST /analyze
Analyze financial text and return risk insights.

## 📥 Request Example
```
{
  "text": "I earn 40k per month but have multiple debts and high expenses"
}
```

## 📤 Response Example
```
{
  "risk_level": "High",
  "reason": "Expenses and liabilities are high relative to income",
  "summary": "User has limited financial buffer",
  "improvements": [
    "Reduce unnecessary expenses",
    "Avoid taking additional loans"
  ],
  "stability_plan": [
    "Track monthly spending",
    "Build an emergency fund",
    "Increase income sources if possible"
  ]
}
```
---
## 🧱 Project Structure
```
financial-risk-agent/
│
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── agent.py       # Gemini + ADK logic
│   ├── schemas.py     # Request/Response models
│   ├── index.html     # Optional UI
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Tech Stack
- Python
- FastAPI
- Google Gemini API
- Google ADK (Agent Development Kit)
- Cloud Run
- Docker


## 🛠️ Setup Instructions
### 1. Clone the repo
```
git clone https://github.com/your-username/financial-risk-agent.git
cd financial-risk-agent
```

### 2. Create virtual environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Add environment variable
Create `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run locally
```
uvicorn app.main:app --reload
```
#### Open:
`http://127.0.0.1:8000/docs`

---

## ☁️ Deployment (Cloud Run)
```
gcloud run deploy financial-risk-agent \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=your_api_key_here
```

---

## 🧠 How It Works
- User sends financial text input
- FastAPI receives request
- Gemini model analyzes financial signals
- Risk classification is generated
- Structured JSON response is returned
