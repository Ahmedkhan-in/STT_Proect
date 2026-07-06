from typing import Any
from typing import Dict
from typing import List

from pydantic import BaseModel
from pydantic import Field


class ConversationSchema(BaseModel):

    conversation_type: str = Field(
        description="Type of conversation"
    )

    summary: str = Field(
        description="Short summary"
    )

    entities: Dict[str, Any] = Field(
        default_factory=dict,
        description="Dynamic extracted entities"
    )

    events: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    actions: List[str] = Field(
        default_factory=list
    )

    metadata: Dict[str, Any] = Field(
        default_factory=dict
    )