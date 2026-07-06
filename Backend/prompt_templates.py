from langchain_core.prompts import PromptTemplate

from parser import parser

extract_prompt = PromptTemplate(
    template="""
You are an expert AI assistant.

Analyze the transcript.

Extract every important piece of information.

Rules:

- Return ONLY valid JSON.
- Do not explain anything.
- If information is missing, leave it null.
- Put unknown fields inside additional_information.

Transcript:

{transcript}

{format_instructions}
""",
    input_variables=["transcript"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)