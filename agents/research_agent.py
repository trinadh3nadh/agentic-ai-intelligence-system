from tools.web_search import search_web
from utils.llm import call_llm


def research_agent(query):

    search_results = search_web(query)

    context = ""

    for r in search_results:
        context += f"{r['title']}\n{r['snippet']}\n\n"

    prompt = f"""
You are a research assistant.

Using the information below, answer the question clearly.

Question:
{query}

Information:
{context}

Provide a structured summary.
"""

    answer = call_llm(prompt)

    return answer, search_results