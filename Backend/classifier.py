from llm import llm

from parser import parser

from prompt_templates import extract_prompt

chain = extract_prompt | llm | parser


def classify(transcript):

    return chain.invoke(
        {
            "transcript": transcript
        }
    )