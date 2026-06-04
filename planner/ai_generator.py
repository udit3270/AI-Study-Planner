from groq import Groq
from django.conf import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_schedule(
    subjects,
    study_hours
):

    prompt = f"""
You are an expert study planner.

Create a COMPLETE STUDY ROADMAP.

Subjects:

{subjects}

Available Study Hours Per Day:
{study_hours}

Instructions:

For every subject:

1. Automatically generate beginner-to-advanced topics.
2. Estimate a logical learning sequence.
3. Create a day-wise roadmap.
4. Divide topics according to target days.
5. Mention revision days.
6. Mention project/practice days where applicable.
7. Keep the plan realistic.
8. Mention approximate completion timeline.

Output Format:

=================================================

SUBJECT: <Subject Name>

Topics To Learn:

- Topic 1
- Topic 2
- Topic 3

Estimated Completion:
XX Days

Study Plan:

Day 1:
...

Day 2:
...

Day 3:
...

Revision Day:
...

=================================================

Return only the study roadmap.
Do not add explanations outside the roadmap.
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,

            max_tokens=3000

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI Error: {str(e)}"