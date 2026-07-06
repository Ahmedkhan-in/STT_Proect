import json

EXAMPLE_OUTPUT = {
    "conversation_type": "Job Interview",

    "summary": "Candidate introduced himself and discussed his background.",

    "entities": {
        "people": [
            {
                "name": "Ahmed"
            }
        ],

        "organizations": [
            "OpenAI"
        ],

        "skills": [
            "Python",
            "Machine Learning"
        ]
    },

    "events": [
        {
            "event": "Completed Bachelor's Degree"
        }
    ],

    "actions": [
        "Apply for internship"
    ],

    "metadata": {
        "language": "English"
    }
}


def get_example():

    return json.dumps(
        EXAMPLE_OUTPUT,
        indent=4
    )