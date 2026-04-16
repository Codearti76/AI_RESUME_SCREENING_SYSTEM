from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate.from_template("""
You are an AI evaluator.

Based on match percentage and experience, assign a score (0–100).

Rules:
- Strong: 80–100
- Medium: 50–79
- Weak: below 50

Match Data:
{match_data}

Return ONLY JSON:
{{
  "score": ""
}}
""")