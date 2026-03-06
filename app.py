import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gc
import time
from agents.research_agent import research_agent
from agents.debate_agent import debate_agent
from agents.data_analyst_agent import analyze_dataset
from agents.kg_agent import extract_entities, build_graph, visualize_graph
from agents.planner_agent import create_plan
from agents.tool_executor import execute_tool
from agents.critic_agent import critique_answer
from agents.reflection_agent import improve_answer
from agents.synthesizer_agent import synthesize_answer

from utils.report_generator import generate_report
from utils.agent_timeline import show_agent_timeline

st.set_page_config(page_title="Agentic AI Intelligence System", layout="wide")

st.title("🤖 Agentic AI Intelligence System")
st.caption("Built by Trinadh Kolluboyina")

mode = st.sidebar.selectbox(
"Select AI Agent",
[
"Research Agent",
"Debate Agent",
"Data Analyst Agent",
"Knowledge Graph Agent",
"Autonomous Agent",
"Collaborative AI Agents"
]
)

agent_notes = {
"Research Agent":"Finds trusted information online and summarizes it.",
"Debate Agent":"Presents two viewpoints and produces a balanced answer.",
"Data Analyst Agent":"Analyzes datasets and generates insights.",
"Knowledge Graph Agent":"Extracts entities and visualizes relationships.",
"Autonomous Agent":"Plans and improves answers automatically.",
"Collaborative AI Agents":"Multiple agents collaborate to solve tasks."
}

st.sidebar.info(agent_notes[mode])

if "run_id" not in st.session_state:
    st.session_state.run_id = 0

query = None
uploaded_files = None
text_input = None

if mode in [
"Research Agent",
"Debate Agent",
"Autonomous Agent",
"Collaborative AI Agents"
]:

    query = st.text_input("Enter your query", key=f"query_{st.session_state.run_id}")

elif mode == "Data Analyst Agent":

    uploaded_files = st.file_uploader(
    "Upload datasets (max 5 files)",
    type=["csv","tsv","xlsx"],
    accept_multiple_files=True
    )

elif mode == "Knowledge Graph Agent":

    text_input = st.text_area("Enter text for graph generation", height=150)

submit = st.button("Run Agent")

final_answer = None

if submit and mode == "Research Agent" and query:

    with st.spinner("Researching..."):

        answer, results = research_agent(query)

    for r in results:

        st.markdown(f"**{r['title']}**")
        st.caption(r["link"])
        st.write(r["snippet"])
        st.markdown("---")

    st.success(answer)

    final_answer = answer

elif submit and mode == "Debate Agent" and query:

    with st.spinner("Running debate..."):

        a,b,c = debate_agent(query)

    col1,col2 = st.columns(2)

    col1.write(a)
    col2.write(b)

    st.success(c)

    final_answer = c

elif submit and mode == "Data Analyst Agent":

    if uploaded_files:

        for file in uploaded_files[:5]:

            df, insights = analyze_dataset(file)

            st.dataframe(df.head())
            st.dataframe(df.describe())

            st.success(insights)

            charts = []

            numeric_cols = df.select_dtypes(include=['int64','float64']).columns

            for col in numeric_cols[:4]:

                fig,ax = plt.subplots(figsize=(4,3))
                sns.histplot(df[col].dropna(),kde=True,ax=ax)
                charts.append(fig)

            for i in range(0,len(charts),3):

                cols = st.columns(3)

                for j in range(len(charts[i:i+3])):

                    cols[j].pyplot(charts[i+j])

            del df
            gc.collect()

elif submit and mode == "Knowledge Graph Agent" and text_input:

    triples = extract_entities(text_input)

    G = build_graph(triples)

    graph_path = visualize_graph(G)

    with open(graph_path,"r") as f:
        html = f.read()

    st.components.v1.html(html,height=550)

elif submit and mode == "Autonomous Agent" and query:

    with st.spinner("Agent thinking..."):

        plan = create_plan(query)

        show_agent_timeline(["Planning task","Executing tools","Critiquing","Improving answer"])

        result = execute_tool(plan,query)

        critique = critique_answer(query,result)

        improved = improve_answer(query,result,critique)

    st.success(improved)

    final_answer = improved

elif submit and mode == "Collaborative AI Agents" and query:

    with st.spinner("Agents collaborating..."):

        show_agent_timeline([
        "Research Agent",
        "Debate Agent",
        "Critic Agent",
        "Synthesizer Agent"
        ])

        research_output,_ = research_agent(query)

        a,b,debate_output = debate_agent(query)

        critique = critique_answer(query,research_output)

        final_answer = synthesize_answer(
        query,
        research_output,
        debate_output,
        critique
        )

    st.success(final_answer)

if final_answer:

    report_file = generate_report(query,final_answer)

    with open(report_file,"rb") as f:

        st.download_button(
        label="Download AI Report",
        data=f,
        file_name="ai_report.pdf",
        mime="application/pdf"
        )

    st.session_state.run_id += 1

if "last_run" not in st.session_state:
    st.session_state.last_run = 0

if time.time() - st.session_state.last_run < 2:
    st.warning("Please wait before sending another request.")
    st.stop()

st.session_state.last_run = time.time()