import streamlit as st
from tavily import TavilyClient


@st.cache_data(ttl=600)
def search_web(query, max_results=5):

    if not query or len(query.strip()) == 0:
        return []

    try:

        client = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])

        response = client.search(
            query=query,
            max_results=max_results
        )

        results = []

        for r in response.get("results", []):

            results.append({
                "title": r.get("title", ""),
                "link": r.get("url", ""),
                "snippet": r.get("content", "")
            })

        return results

    except Exception:

        return [{
            "title": "Search temporarily unavailable",
            "link": "",
            "snippet": "The search API could not be reached."
        }]