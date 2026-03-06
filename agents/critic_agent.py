from utils.llm import call_llm

def critique_answer(query, answer):

    prompt = f"""
Evaluate the answer.

Question:
{query}

Answer:
{answer}

Score from 1 to 10 and explain weaknesses.
"""

    critique = call_llm(prompt)

    return critique