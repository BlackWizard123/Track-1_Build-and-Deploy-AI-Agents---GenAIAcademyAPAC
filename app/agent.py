import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv
from google.adk import Agent

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-1.5-flash")
model = genai.GenerativeModel("gemini-2.5-flash")


def extract_json(text: str) -> dict:
    """
    Robust JSON extractor from LLM output
    """
    try:
        # Direct parse
        return json.loads(text)
    except:
        pass

    try:
        # Remove markdown ```json ```
        text = re.sub(r"```json|```", "", text).strip()

        # Extract JSON block
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            json_str = match.group()

            # Fix common trailing comma issue
            json_str = re.sub(r",\s*}", "}", json_str)

            return json.loads(json_str)
    except:
        pass

    raise ValueError("Could not extract valid JSON")

risk_agent = Agent(
    name="financial_risk_agent",
    model="gemini-1.5-flash-latest",
    description="Analyzes financial text and classifies financial risk",
    instruction="""
You are a financial risk analysis assistant.

Your task is to analyze a user's financial situation and classify risk.

### Risk Guidelines:
- HIGH RISK:
  - Expenses close to or greater than income
  - Multiple debts or liabilities
  - No stable income

- MEDIUM RISK:
  - Moderate expenses compared to income
  - Some debt but manageable

- LOW RISK:
  - Stable income
  - Low expenses
  - Minimal or no debt

### Instructions:
- Carefully read the input
- Identify income, expenses, and debt indicators
- Classify into: Low, Medium, or High

### Output Rules:
- Return ONLY valid JSON
- No markdown
- No extra text

### Format:
{
    "risk_level": "Low | Medium | High",
    "reason": "Explanation based on financial signals",
    "summary": "Short summary",

    "improvements": [
        "Actionable suggestion 1",
        "Actionable suggestion 2"
    ],

    "stability_plan": [
        "Step 1",
        "Step 2",
        "Step 3"
    ]
}
"""
)

def analyze_with_adk(text: str) -> dict:
    try:
        response = risk_agent.run(input=text)

        # Sometimes ADK returns object/string → normalize
        if isinstance(response, dict):
            return response

        return extract_json(str(response))

    except Exception as e:
        return {
            "risk_level": "Unknown",
            "reason": f"ADK error: {str(e)}",
            "summary": "Failed to analyze input",
            "improvements": [],
            "stability_plan": []
        }


def analyze_financial_risk(text: str) -> dict:
    prompt = f"""
You are a financial risk analysis assistant.

Your task is to analyze a user's financial situation and classify risk.

### Risk Guidelines:
- HIGH RISK:
  - Expenses close to or greater than income
  - Multiple debts or liabilities
  - No stable income

- MEDIUM RISK:
  - Moderate expenses compared to income
  - Some debt but manageable

- LOW RISK:
  - Stable income
  - Low expenses
  - Minimal or no debt

### Instructions:
- Carefully read the input
- Identify income, expenses, and debt indicators
- Classify into: Low, Medium, or High

### Output Rules:
- Return ONLY valid JSON
- No markdown
- No extra text

### Format:
{{
    "risk_level": "Low | Medium | High",
    "reason": "Explanation based on financial signals",
    "summary": "Short summary",

    "improvements": [
        "Actionable suggestion 1",
        "Actionable suggestion 2"
    ],

    "stability_plan": [
        "Step 1",
        "Step 2",
        "Step 3"
    ]
}}

USER INPUT:
{text}
"""

    try:
        response = model.generate_content(prompt)
        raw_output = response.text.strip()

        result = extract_json(raw_output)

        return result

    except Exception as e:
        return {
            "risk_level": "Unknown",
            "reason": f"Parsing error: {str(e)}",
            "summary": "Could not analyze input properly"
        }