import streamlit as st
import requests
import time


def call_llm(prompt, retries=3):

    api_key = st.secrets["GROQ_API_KEY"]

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 700
    }

    for attempt in range(retries):

        try:

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=60
            )

            result = response.json()

            # success
            if "choices" in result:
                return result["choices"][0]["message"]["content"]

            # rate limit
            if "error" in result and "rate limit" in result["error"]["message"].lower():

                wait_time = 2 + attempt
                time.sleep(wait_time)
                continue

            # other error
            if "error" in result:
                return f"LLM API Error: {result['error']['message']}"

            return "Unexpected LLM response."

        except Exception as e:

            time.sleep(2)
            if attempt == retries - 1:
                return f"LLM request failed: {str(e)}"

    return "LLM request failed after retries."