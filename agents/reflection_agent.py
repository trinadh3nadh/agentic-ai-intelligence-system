from utils.llm import call_llm

def improve_answer(query, answer, critique):

    prompt = f"""
Improve the answer using the critique.

Question:
{query}

Original Answer:
{answer}

Critique:
{critique}

Provide a better answer.
"""

    improved = call_llm(prompt)

    return improved