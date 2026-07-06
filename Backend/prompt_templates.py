from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate.from_template("""
You are an expert AI information extraction assistant.

Your task is to analyze the transcript and produce a structured JSON representation.

The transcript may be:

- Customer support call
- Bank call
- Visa consultation
- Job interview
- Business meeting
- Friends chatting
- Medical conversation
- Restaurant order
- Casual discussion
- Any other conversation

----------------------------
Rules
----------------------------

1. Read the entire transcript before extracting information.

2. Determine the conversation type.

3. Extract ONLY information explicitly mentioned.

4. Never guess.

5. Never infer facts that are not stated.

6. Never invent people, companies or phone numbers.

7. Return ONLY valid JSON.

8. The JSON structure should adapt to the conversation.

9. If a section has no information, omit it instead of creating empty fields.

10. Keep summaries concise.

----------------------------
Suggested Structure
----------------------------

{
    "conversation_type": "...",

    "summary": "...",

    "entities": {

    },

    "events": [

    ],

    "actions": [

    ],

    "metadata": {

    }
}

The structure is flexible.

Only include sections that are relevant.

Transcript:

{transcript}
""")