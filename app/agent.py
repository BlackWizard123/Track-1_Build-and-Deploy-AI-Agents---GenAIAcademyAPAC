import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

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


def analyze_financial_risk(text: str) -> dict:
    prompt = f"""
You are a financial risk analysis assistant.

Analyze the user's financial situation.

Classify risk:
- Low
- Medium
- High

STRICT INSTRUCTIONS:
- Output ONLY JSON
- No markdown
- No explanation before/after
- Ensure valid JSON format

Example:
{{
    "risk_level": "High",
    "reason": "Expenses are high compared to income",
    "summary": "User has limited financial buffer"
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