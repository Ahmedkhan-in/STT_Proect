from langchain_core.prompts import PromptTemplate

from prompts.instructions import SYSTEM_INSTRUCTIONS

prompt = PromptTemplate.from_template(
"""
{instructions}

Example Output

{example}

Transcript

{transcript}
"""
)