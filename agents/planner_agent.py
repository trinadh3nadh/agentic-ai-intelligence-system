from utils.llm import call_llm

def create_plan(user_query):

    prompt = f"""
You are an AI planner.

Break the task into steps.

Available tools:
- web_search
- debate
- data_analysis
- knowledge_graph

User query:
{user_query}

Return steps.
"""

    plan = call_llm(prompt)

    return plan