from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate.from_template("""
You are an AI recruiter.

Explain why this score was assigned.

Include:
- Strengths
- Weaknesses

Score:
{score}

Match Data:
{match_data}

Return ONLY JSON:
{{
  "explanation": ""
}}
""")