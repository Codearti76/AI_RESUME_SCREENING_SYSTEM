from chains.llm import get_llm
from prompts.score_prompt import score_prompt

llm = get_llm()

scoring_chain = score_prompt | llm