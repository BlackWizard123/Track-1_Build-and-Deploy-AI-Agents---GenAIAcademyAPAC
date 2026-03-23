from fastapi import FastAPI
from app.agent import analyze_financial_risk
from app.schemas import RiskRequest, RiskResponse

app = FastAPI(
    title="Financial Risk Classifier API",
    description="Analyzes financial text and classifies risk level using Gemini",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Financial Risk Classifier API is running"}


@app.post("/analyze", response_model=RiskResponse)
def analyze(request: RiskRequest):
    result = analyze_financial_risk(request.text)
    return result