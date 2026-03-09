# 🤖 AI Resume Hiring Intelligence System

An advanced **AI-powered resume screening and hiring intelligence
platform** built with:

-   **LangGraph multi-agent workflow**
-   **RAG (Retrieval Augmented Generation)**
-   **Groq LLM**
-   **FAISS vector database**
-   **Streamlit interactive dashboard**
-   **Real-time job recommendations**
-   **Skill analytics & candidate leaderboard**

This project demonstrates how modern AI systems can automate **resume
analysis, candidate ranking, and job matching**.

------------------------------------------------------------------------

## 🌐 Live Demo

🚀 Try the deployed application here:

👉 https://ai-resume-hiring-system.streamlit.app 

------------------------------------------------------------------------

# 🚀 Features

### 📄 Resume Ingestion

-   Upload resumes (PDF)
-   Automatic parsing and chunking
-   Embeddings generated using `sentence-transformers`
-   Stored in **FAISS vector database**
-   Supports **dynamic merging of new resumes**

### 🧠 Multi-Agent AI System

Implemented using **LangGraph**:

1.  Planner Agent
2.  Resume Analyzer Agent
3.  Evaluator Agent
4.  Resume Optimizer Agent
5.  Job Recommendation Agent

Agents collaborate to generate intelligent hiring insights.

------------------------------------------------------------------------

# 📊 Dashboard Features

### Metrics

-   Total candidates
-   Resume chunks indexed
-   AI agents active

### Resume Analysis

-   AI-powered resume insights
-   ATS score gauge
-   Skill radar visualization

### Candidate Leaderboard

-   Shows all uploaded candidates
-   Ranking visualization

### Skill Analytics

-   Extracts common skills across resumes
-   Visual skill frequency charts

### Resume Optimization

-   AI rewrites resume tailored to job description

### Real-time Job Recommendations

-   Fetches **live remote jobs**
-   Matches jobs using **semantic similarity**

------------------------------------------------------------------------

# 🏗 Project Architecture

    User Upload Resume
            ↓
    PDF Parser
            ↓
    Text Chunking
            ↓
    Embedding Model
            ↓
    FAISS Vector Database
            ↓
    LangGraph Multi-Agent Pipeline
            ↓
    Resume Analysis + Optimization
            ↓
    Dashboard + Job Recommendations

------------------------------------------------------------------------

# 📂 Project Structure

    smart_resume_ai/

    app.py

    agents/
        planner_agent.py
        analyzer_agent.py
        evaluator_agent.py
        optimizer_agent.py
        recommender_agent.py

    graph/
        workflow.py

    rag/
        ingest.py
        retriever.py
        vector_store.py

    parsers/
        pdf_parser.py

    jobs/
        job_api.py
        job_matcher.py

    utils/
        embeddings.py
        llm.py

    vector_db/

    requirements.txt
    README.md

------------------------------------------------------------------------

# ⚙ Installation

## 1️⃣ Clone Repository

``` bash
git clone https://github.com/yourusername/smart-resume-ai.git
cd smart-resume-ai
```

## 2️⃣ Create Virtual Environment

``` bash
python -m venv .venv
```

Activate environment:

Windows

``` bash
.venv\Scripts\activate
```

Mac/Linux

``` bash
source .venv/bin/activate
```

------------------------------------------------------------------------

## 3️⃣ Install Dependencies

``` bash
uv add -r requirements.txt
```

------------------------------------------------------------------------

# 🔑 Environment Variables

Create an environment variable for your Groq API key.

Windows:

``` bash
setx GROQ_API_KEY "your_api_key_here"
```

Mac/Linux:

``` bash
export GROQ_API_KEY="your_api_key_here"
```

------------------------------------------------------------------------

# ▶ Running the Application

``` bash
streamlit run app.py
```

Open browser:

    http://localhost:8501

------------------------------------------------------------------------

# 🧪 How to Use

1️⃣ Upload resume PDF

2️⃣ Resume embeddings are stored in FAISS

3️⃣ Enter job description

4️⃣ Click **Run Hiring Analysis**

The system will generate:

-   Resume analysis
-   Skill insights
-   Optimized resume
-   Live job matches

------------------------------------------------------------------------

# 🧠 Technologies Used

  Technology              Purpose
  ----------------------- ---------------------------
  Streamlit               Dashboard UI
  LangGraph               Multi-agent orchestration
  Groq                    LLM inference
  FAISS                   Vector search
  Sentence Transformers   Embeddings
  Plotly                  Data visualization
  Scikit-learn            Job similarity matching

------------------------------------------------------------------------

# 📈 Future Improvements

Possible upgrades:

-   Candidate semantic search
-   Resume → job match scoring
-   AI interview question generator
-   Skill knowledge graph
-   Recruiter dashboard

------------------------------------------------------------------------

# 📜 License

MIT License

------------------------------------------------------------------------

# 👨‍💻 Author

**Vishwatej Khot**

AI / Data Science Projects
