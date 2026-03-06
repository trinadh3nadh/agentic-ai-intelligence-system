from agents.research_agent import research_agent
from agents.debate_agent import debate_agent


def execute_tool(step, query):

    if not query or len(query.strip()) == 0:
        return "Invalid query provided."

    step = step.lower()

    try:

        if "research" in step or "search" in step:

            answer, _ = research_agent(query)

            return answer

        elif "debate" in step:

            a, b, c = debate_agent(query)

            return c

        else:

            return "No tool matched for this step."

    except Exception as e:

        return f"Tool execution error: {str(e)}"