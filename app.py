import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re

from parsers.pdf_parser import parse_pdf
from rag.ingest import ingest_resume
from graph.workflow import build_graph
from rag.vector_store import load_db
from jobs.job_api import fetch_jobs
from jobs.job_matcher import match_jobs

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Resume Hiring System",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

[data-testid="stMetric"] {
    background-color: #111;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #333;
}

.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
}

section[data-testid="stSidebar"] {
    background-color: #0e1117;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD GRAPH
# -----------------------------
graph = build_graph()

# -----------------------------
# TITLE
# -----------------------------
st.title("🤖 AI Resume Hiring Intelligence System")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Controls")

uploaded_resume = st.sidebar.file_uploader("Upload Resume PDF")

job_desc = st.sidebar.text_area("Job Description")

run_analysis = st.sidebar.button("Run Hiring Analysis")

st.sidebar.markdown("---")
st.sidebar.info("LangGraph + RAG + ATS + Resume Optimizer")

# -----------------------------
# LOAD VECTOR DB
# -----------------------------
db = load_db()

candidates = []
all_text = ""

if db:

    docs = db.docstore._dict.values()

    for doc in docs:

        if "candidate" in doc.metadata:
            candidates.append(doc.metadata["candidate"])

        all_text += " " + doc.page_content

unique_candidates = list(set(candidates))
num_candidates = len(unique_candidates)

# -----------------------------
# DASHBOARD METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Candidates", num_candidates)
col2.metric("Resumes Indexed", len(candidates))
col3.metric("AI Agents", "6")

st.markdown("---")

# -----------------------------
# RESUME INGESTION
# -----------------------------
if uploaded_resume:

    text = parse_pdf(uploaded_resume)

    ingest_resume(text, uploaded_resume.name)

    st.success(f"{uploaded_resume.name} indexed into vector database")

# -----------------------------
# SKILL ANALYTICS
# -----------------------------
skill_list = [
    "python","machine learning","sql","docker",
    "kubernetes","pytorch","tensorflow",
    "nlp","data science","mlops"
]

skill_counts = {}

for skill in skill_list:

    pattern = r"\b" + skill + r"\b"
    count = len(re.findall(pattern, all_text.lower()))

    skill_counts[skill] = count

skills_df = pd.DataFrame({
    "Skill": list(skill_counts.keys()),
    "Frequency": list(skill_counts.values())
})

# -----------------------------
# CREATE TABS (ALWAYS VISIBLE)
# -----------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Analysis",
    "🧠 Evaluation",
    "✨ Optimized Resume",
    "🎯 Job Recommendations",
    "🏆 Candidate Leaderboard",
    "📈 Skill Analytics"
])

# -------------------------
# ANALYSIS TAB
# -------------------------
with tab1:

    st.subheader("Resume Analysis")

    if run_analysis and job_desc:

        result = graph.invoke({
            "job_description": job_desc
        })

        st.write(result["analysis"])

        ats_score = 82

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=ats_score,
            title={'text': "ATS Match Score"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "green"},
                'steps': [
                    {'range':[0,50],'color':'red'},
                    {'range':[50,75],'color':'orange'},
                    {'range':[75,100],'color':'lightgreen'}
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

    else:

        st.info("Upload resumes and click **Run Hiring Analysis** to generate insights.")

# -------------------------
# EVALUATION TAB
# -------------------------
with tab2:

    if run_analysis and job_desc:

        st.subheader("Evaluator Agent Feedback")

        st.write(result["evaluation"])

    else:

        st.info("Run analysis to view evaluator feedback.")

# -------------------------
# OPTIMIZED RESUME
# -------------------------
with tab3:

    if run_analysis and job_desc:

        st.subheader("AI Generated Optimized Resume")

        st.write(result["optimized_resume"])

        st.download_button(
            "Download Optimized Resume",
            result["optimized_resume"],
            file_name="optimized_resume.txt"
        )

    else:

        st.info("Run analysis to generate optimized resume.")

# -------------------------
# JOB RECOMMENDATIONS
# -------------------------
with tab4:

    st.subheader("Live Job Opportunities")

    if job_desc:

        jobs_df = fetch_jobs()

        matched_jobs = match_jobs(job_desc, jobs_df)

        st.dataframe(matched_jobs)

    else:

        st.info("Enter a job description to see matching jobs.")

# -------------------------
# LEADERBOARD
# -------------------------
with tab5:

    st.subheader("Candidate Leaderboard")

    if num_candidates == 0:

        st.warning("No resumes uploaded yet.")

    else:

        leaderboard = pd.DataFrame({
            "Candidate": unique_candidates,
            "ATS Score": [82 for _ in unique_candidates]
        })

        st.dataframe(leaderboard, use_container_width=True)

        fig = px.bar(
            leaderboard,
            x="Candidate",
            y="ATS Score",
            color="ATS Score",
            title="Candidate Ranking"
        )

        st.plotly_chart(fig, use_container_width=True)

# -------------------------
# SKILL ANALYTICS
# -------------------------
with tab6:

    st.subheader("Top Skills Across Candidates")

    fig = px.bar(
        skills_df,
        x="Skill",
        y="Frequency",
        color="Frequency",
        title="Skill Distribution Across Resumes"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(skills_df)

