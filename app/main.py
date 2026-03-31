from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.agent import analyze_financial_risk
from app.agent import analyze_with_adk
from app.schemas import RiskRequest, RiskResponse

app = FastAPI(
    title="Financial Risk Classifier API",
    description="Analyzes financial text and classifies risk level using Gemini",
    version="1.0.0"
)


@app.get("/", response_class=HTMLResponse)
def root():
    with open("app/landing.html", "r") as file:
        return file.read()
    # return """
    # <html>
    #     <head>
    #         <title>Financial Risk Classifier</title>
    #         <style>
    #             body {
    #                 font-family: Arial;
    #                 background: #0f172a;
    #                 color: white;
    #                 display: flex;
    #                 justify-content: center;
    #                 align-items: center;
    #                 height: 100vh;
    #                 text-align: center;
    #             }
    #             .container {
    #                 background: #1e293b;
    #                 padding: 30px;
    #                 border-radius: 12px;
    #             }
    #             a {
    #                 display: block;
    #                 margin: 10px;
    #                 padding: 10px;
    #                 background: #38bdf8;
    #                 color: black;
    #                 text-decoration: none;
    #                 border-radius: 6px;
    #             }
    #             a:hover {
    #                 background: #0ea5e9;
    #             }
    #         </style>
    #     </head>
    #     <body>
    #         <div class="container">
    #             <h1>💰 Financial Risk Classifier</h1>
    #             <p>AI-powered financial risk analysis using Gemini</p>

    #             <a href="/docs">📘 API Docs (Swagger)</a>
    #             <a href="/ui">💬 Try Chat Interface</a>
    #             <a href="/analyze">⚙️ API Endpoint</a>
    #         </div>
    #     </body>
    # </html>
    # """


@app.get("/ui", response_class=HTMLResponse)
def serve_ui():
    with open("app/index.html", "r") as file:
        return file.read()


@app.post("/analyze", response_model=RiskResponse)
def analyze(request: RiskRequest):
    result = analyze_financial_risk(request.text)
    # result = analyze_with_adk(request.text)
    return result