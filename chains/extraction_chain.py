from chains.llm import get_llm
from prompts.extract_prompt import extract_prompt

llm = get_llm()

extraction_chain = extract_prompt | llm