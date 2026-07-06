from langchain_core.prompts import PromptTemplate

from parser import parser

prompt = PromptTemplate(
    template="""
You are an expert AI information extraction assistant.

Analyze the transcript carefully.

Return ONLY valid JSON.

Rules:

1. Understand the entire conversation first.

2. Determine the conversation type.

3. Extract ONLY explicitly mentioned information.

4. Never guess.

5. Never infer.

6. Never invent missing information.

7. Keep the summary short.

8. Use this fixed top-level structure:

- conversation_type
- summary
- entities
- events
- actions
- metadata

9. The "entities" object is completely dynamic.

Examples:

Bank conversation

entities:
{{
    "people":[
        {{
            "name":"Ahmed"
        }}
    ],

    "phone_numbers":[
        "03001234567"
    ],

    "cards":[
        "Debit Card"
    ]
}}

Job interview

entities:
{{
    "people":[
        {{
            "name":"Ali"
        }}
    ],

    "skills":[
        "Python",
        "Machine Learning"
    ],

    "education":[
        "BS Artificial Intelligence"
    ]
}}

Friends conversation

entities:
{{
    "people":[
        "Ali",
        "Ahmed"
    ],

    "movie":[
        "Superman"
    ]
}}

Restaurant

entities:
{{
    "food_items":[
        "Burger",
        "Pizza"
    ]
}}

{format_instructions}

Transcript:

{transcript}
""",
    input_variables=["transcript"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)