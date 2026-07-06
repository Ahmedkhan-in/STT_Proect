from langchain_core.output_parsers import JsonOutputParser

from schemas import ConversationSchema

parser = JsonOutputParser(
    pydantic_object=ConversationSchema
)