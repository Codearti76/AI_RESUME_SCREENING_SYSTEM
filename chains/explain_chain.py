from chains.llm import get_llm
from prompts.explain_prompt import explain_prompt

llm = get_llm()

explanation_chain = explain_prompt | llm