from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate.from_template("""
You are an AI recruiter.

Compare the extracted resume data with job description.

Return:
- matched_skills
- missing_skills
- match_percentage

Rules:
- Only use provided data
- Do NOT assume skills

Resume Data:
{resume_data}

Job Description:
{job_desc}

Return ONLY JSON:
{{
  "matched_skills": [],
  "missing_skills": [],
  "match_percentage": ""
}}
""")