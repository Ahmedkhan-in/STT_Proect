import json

from llm import llm

from prompts.prompt_templates import prompt

from prompts.instructions import SYSTEM_INSTRUCTIONS

from prompts.examples import get_example

chain = prompt | llm


def classify(transcript):

    response = chain.invoke(
        {
            "instructions": SYSTEM_INSTRUCTIONS,
            "example": get_example(),
            "transcript": transcript,
        }
    )

    content = response.content.strip()

    if content.startswith("```json"):
        content = content.replace("```json", "")
        content = content.replace("```", "").strip()

    return json.loads(content)