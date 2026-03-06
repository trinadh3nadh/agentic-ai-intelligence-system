from utils.llm import call_llm


def debate_agent(topic):

    prompt_a = f"""
You are Expert A.

Argue FOR the following statement:

{topic}
"""

    prompt_b = f"""
You are Expert B.

Argue AGAINST the following statement:

{topic}
"""

    argument_a = call_llm(prompt_a)
    argument_b = call_llm(prompt_b)

    synthesis_prompt = f"""
Two experts debated a topic.

Expert A:
{argument_a}

Expert B:
{argument_b}

Provide a balanced conclusion.
"""

    conclusion = call_llm(synthesis_prompt)

    return argument_a, argument_b, conclusion