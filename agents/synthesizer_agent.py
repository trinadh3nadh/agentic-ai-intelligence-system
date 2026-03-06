from utils.llm import call_llm


def synthesize_answer(query, research_output, debate_output, critique):

    prompt = f"""
You are an AI synthesizer.

Combine insights from multiple agents.

User Question:
{query}

Research Agent Output:
{research_output}

Debate Agent Output:
{debate_output}

Critic Feedback:
{critique}

Provide the best final answer.
"""

    result = call_llm(prompt)

    return result