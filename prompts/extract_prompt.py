from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate.from_template("""
You are an AI resume parser.

Extract:
- Skills
- Tools
- Experience (in years)

Rules:
- Do NOT assume anything
- Only extract explicitly mentioned data
- Return ONLY valid JSON

Format:
{{
  "skills": [],
  "tools": [],
  "experience": ""
}}

Resume:
{resume}
""")