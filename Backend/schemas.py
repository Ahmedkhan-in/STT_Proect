from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class ConversationSchema(BaseModel):

    name: Optional[str] = None

    phone_number: Optional[str] = None

    email: Optional[str] = None

    address: Optional[str] = None

    company: Optional[str] = None

    organization: Optional[str] = None

    participants: Optional[List[str]] = None

    topic: Optional[str] = None

    intent: Optional[str] = None

    summary: str

    additional_information: Optional[Dict[str, Any]] = None