# ==============================
# LOAD ENV VARIABLES
# ==============================
from dotenv import load_dotenv
import os
import sys
sys.path.append("./chains")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

print("DEBUG: GROQ KEY =", os.getenv("GROQ_API_KEY"))  # ✅ debug

# ==============================
# IMPORT CHAINS
# ==============================
from chains.llm import get_llm
from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explain_chain import explain_chain

# ==============================
# SAMPLE DATA
# ==============================

job_description = """
We are looking for a Data Scientist with:
- Strong Python skills
- Experience with Machine Learning
- Knowledge of Pandas, NumPy, Scikit-learn
- Experience with SQL
- Good problem-solving skills
"""

resume_strong = """
John Doe
Skills: Python, Machine Learning, Pandas, NumPy, Scikit-learn, SQL
Experience: 3 years as Data Scientist
"""

resume_average = """
Jane Smith
Skills: Python, Pandas, Excel
Experience: 1 year as Data Analyst
"""

resume_weak = """
Bob Brown
Skills: MS Word, Communication
Experience: Fresher
"""

# ==============================
# PIPELINE FUNCTION
# ==============================

def run_pipeline(resume, name):
    print(f"\n\n===== {name} =====")

    # Step 1: Extraction
    extracted = extraction_chain.invoke({
        "resume": resume
    })
    print("\n[EXTRACTED]")
    print(extracted)

    # Step 2: Matching
    matched = matching_chain.invoke({
        "resume_data": extracted,
        "job_description": job_description
    })
    print("\n[MATCHED]")
    print(matched)

    # Step 3: Scoring
    score = scoring_chain.invoke({
        "match_result": matched
    })
    print("\n[SCORE]")
    print(score)

    # Step 4: Explanation
    explanation = explain_chain.invoke({
        "score": score,
        "match_result": matched
    })
    print("\n[EXPLANATION]")
    print(explanation)


# ==============================
# MAIN EXECUTION
# ==============================

if __name__ == "__main__":
    llm = get_llm()  # ✅ triggers API usage

    run_pipeline(resume_strong, "STRONG CANDIDATE")
    run_pipeline(resume_average, "AVERAGE CANDIDATE")
    run_pipeline(resume_weak, "WEAK CANDIDATE")