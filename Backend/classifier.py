from parser import parser

from llm import llm

from prompts.extraction_prompt import prompt

chain = prompt | llm | parser


def classify(transcript):

    return chain.invoke(
        {
            "transcript": transcript
        }
    )