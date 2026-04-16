from chains.llm import get_llm
from prompts.match_prompt import match_prompt

llm = get_llm()

matching_chain = match_prompt | llm