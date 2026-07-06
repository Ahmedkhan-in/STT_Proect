from langchain_core.output_parsers import JsonOutputParser

from schemas.conversation_schema import ConversationSchema

parser = JsonOutputParser(
    pydantic_object=ConversationSchema
)