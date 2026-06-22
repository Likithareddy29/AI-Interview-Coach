from jd_questions import generate_jd_questions
from jd_analyzer import analyze_jd
from report_generator import generate_report
from resume_improver import improve_resume
from jd_resume_improver import improve_resume_for_jd
from answer_evaluator import evaluate_answer
from groq_helper import generate_ai_questions
from question_generator import generate_questions
from ats_score import calculate_ats_score
from skill_extractor import extract_skills
from career_recommender import recommend_career
from readiness_score import calculate_readiness_score

from jd_matcher import (
    calculate_jd_match,
    find_missing_keywords,
    get_matched_skills
)

import streamlit as st
import pdfplumber
import plotly.graph_objects as go

# ==========================================
# GAUGE CHART
# ==========================================

def create_gauge(score, title):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text": title
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "#2563eb"
                },

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "#ef4444"
                    },

                    {
                        "range": [40, 70],
                        "color": "#f59e0b"
                    },

                    {
                        "range": [70, 100],
                        "color": "#10b981"
                    }

                ]
            }
        )
    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        font={
            "color": "white"
        },

        height=300,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    return fig
# ==========================================

# PAGE CONFIG

# ==========================================

st.set_page_config(
page_title="AI Interview Coach",
page_icon="🚀",
layout="wide"
)

# ==========================================

# CUSTOM CSS

# ==========================================

st.markdown("""
<style>

/* ==============================
   MAIN APP
============================== */

.stApp{
    background:#111827;
}

/* ==============================
   SIDEBAR
============================== */

section[data-testid="stSidebar"]{
    background:#0f172a;
    border-right:1px solid #1e293b;
}

/* ==============================
   HEADINGS
============================== */

h1,h2,h3{
    color:white;
}

/* ==============================
   TEXT
============================== */

p{
    color:#cbd5e1;
}

/* ==============================
   BUTTONS
============================== */

.stButton > button{
    width:100%;
    border-radius:12px;
    font-weight:600;
    background:#2563eb;
    color:white;
    border:none;
    transition:0.3s;
}

.stButton > button:hover{
    background:#1d4ed8;
    transform:translateY(-2px);
}

/* ==============================
   METRIC CONTAINERS
============================== */

[data-testid="metric-container"]{
    background:white;
    border-radius:18px;
    padding:20px;
    border:none;
    box-shadow:0px 6px 18px rgba(0,0,0,0.15);
}

/* ==============================
   HOVER EFFECT CARDS
============================== */

.card-hover{
    transition:all 0.3s ease;
}

.card-hover:hover{
    transform:translateY(-6px);
    box-shadow:0px 12px 30px rgba(37,99,235,0.35);
}

/* ==============================
   EXPANDERS
============================== */

.streamlit-expanderHeader{
    color:white !important;
    font-weight:600;
}

/* ==============================
   INPUT BOXES
============================== */

textarea{
    border-radius:12px !important;
}

input{
    border-radius:12px !important;
}

/* ==============================
   SUCCESS BOXES
============================== */

div[data-baseweb="notification"]{
    border-radius:12px;
}

/* ==============================
   PROGRESS BAR
============================== */

.stProgress > div > div > div > div{
    background:#2563eb;
}

/* ==============================
   SCROLLBAR
============================== */

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-track{
    background:#0f172a;
}

::-webkit-scrollbar-thumb{
    background:#2563eb;
    border-radius:20px;
}

::-webkit-scrollbar-thumb:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)
# ==========================================

# SIDEBAR

# ==========================================

st.sidebar.title("🚀 AI Interview Coach")


# ==========================================

# HEADER

# ==========================================

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div style="
background:linear-gradient(
135deg,
#2563eb 0%,
#1d4ed8 40%,
#0f172a 100%
);
padding:35px;
border-radius:24px;
margin-bottom:25px;
box-shadow:0px 15px 40px rgba(37,99,235,0.35);
">

<h1 style="
margin:0;
font-size:52px;
font-weight:700;
color:white;">
🚀 AI Interview Coach
</h1>

<p style="
margin-top:15px;
font-size:18px;
color:#dbeafe;">
Analyze resumes • Optimize ATS Scores • Match Job Descriptions • Generate Interview Questions • Improve Career Readiness
</p>

<div style="
margin-top:20px;
display:flex;
gap:12px;
flex-wrap:wrap;
">

<span style="
background:rgba(255,255,255,0.15);
padding:8px 14px;
border-radius:20px;
color:white;">
📊 ATS Analysis
</span>

<span style="
background:rgba(255,255,255,0.15);
padding:8px 14px;
border-radius:20px;
color:white;">
🛠 Skill Detection
</span>

<span style="
background:rgba(255,255,255,0.15);
padding:8px 14px;
border-radius:20px;
color:white;">
🎯 JD Matching
</span>

<span style="
background:rgba(255,255,255,0.15);
padding:8px 14px;
border-radius:20px;
color:white;">
🤖 Interview Prep
</span>

</div>

</div>
""", unsafe_allow_html=True)



# ==========================================

# FILE UPLOADER

# ==========================================

st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)
text = ""

skills = []
score = 0
readiness = 0
careers = []

jd_match_score = 0
missing_keywords = []
matched_skills = []

job_description = st.sidebar.text_area(
    "📋 Paste Job Description (Optional)",
    height=200
)

if "last_jd" not in st.session_state:
    st.session_state.last_jd = ""

if job_description != st.session_state.last_jd:

    st.session_state.jd_mode = False

    st.session_state.last_jd = job_description

if "jd_mode" not in st.session_state:
    st.session_state.jd_mode = False

if st.sidebar.button("🎯 Evaluate JD"):
    st.session_state.jd_mode = True

if st.sidebar.button("🔄 Reset JD Analysis"):

    st.session_state.jd_mode = False

    st.session_state.last_jd = ""

    st.rerun()
# ==========================================

# ONLY RUN AFTER FILE UPLOAD

# ==========================================

if uploaded_file is not None:

    text = ""

    try:

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text

    except Exception as e:

        st.error(f"PDF Error: {e}")
        st.stop()

    st.success("✅ Resume Uploaded Successfully!")

# ==========================================
# ANALYSIS
# ==========================================

if uploaded_file is not None:

    skills = extract_skills(text)

    # ATS MODE

    ats_score = calculate_ats_score(
        skills
    )

    readiness = calculate_readiness_score(
        ats_score,
        len(skills)
    )

    careers = recommend_career(
        skills
    )

    # JD MODE

    if job_description.strip() and st.session_state.jd_mode:

        jd_match_score = calculate_jd_match(
            text,
            job_description
        )

        matched_skills = get_matched_skills(
            text,
            job_description
        )

        missing_keywords = find_missing_keywords(
            text,
            job_description
        )

        jd_readiness = min(
            int(
                (jd_match_score * 0.8)
                + (len(matched_skills) * 3)
            ),
            100
        )

    else:

        jd_match_score = 0

        jd_readiness = 0

        matched_skills = []

        missing_keywords = []

else:

    skills = []

    ats_score = 0

    readiness = 0

    careers = []

    jd_match_score = 0

    jd_readiness = 0

    matched_skills = []

    missing_keywords = []
# ==========================================
# TABS
# ==========================================

page = st.sidebar.radio(
    "📂 Navigation",
    [
        "📄 Resume Viewer",
        "📊 ATS Analysis",
        "🛠 Skill Detection",
        "🎯 Interview Questions",
        "🤖 Answer Evaluation",
        "🚀 Resume Suggestions",
        "🎯 Career Recommendations",
        "📥 PDF Report"
    ]
)
# ==========================================
# RESUME VIEWER
# ==========================================

if page == "📄 Resume Viewer":

    st.header("📄 Resume Viewer")

    if text:

        with st.expander(
            "View Resume Content",
            expanded=True
        ):

            st.write(text)

    else:

        st.warning(
            "Please upload a resume first."
        )
# ==========================================
# ATS Analysis
# ==========================================

if page == "📊 ATS Analysis":

    if uploaded_file is None:

        st.info(
            "📄 Please upload a resume."
        )

    else:

        st.header("📊 Resume Dashboard")


# ==================================
# JD MODE
# ==================================

        if job_description.strip() and st.session_state.jd_mode:

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(f"""
                <div class="card-hover" style="
                background:rgba(255,255,255,0.08);
                backdrop-filter:blur(12px);
                -webkit-backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.15);
                padding:25px;
                border-radius:20px;
                text-align:center;
                color:white;
                ">
                    <h4>🎯 JD Match Score</h4>
                    <h1>{jd_match_score}</h1>
                </div>
                """, unsafe_allow_html=True)

            with col2:

                st.markdown(f"""
                <div class="card-hover" style="
                background:rgba(255,255,255,0.08);
                backdrop-filter:blur(12px);
                -webkit-backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.15);
                padding:25px;
                border-radius:20px;
                text-align:center;
                color:white;
                ">
                    <h4>🚀 JD Readiness</h4>
                    <h1>{jd_readiness}</h1>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.progress(
                min(jd_readiness, 100)
            )
            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:

                st.plotly_chart(
                    create_gauge(
                        jd_match_score,
                        "JD Match Score"
                    ),
                    use_container_width=True
                )

            with col2:

                st.plotly_chart(
                    create_gauge(
                        jd_readiness,
                        "JD Readiness"
                    ),
                    use_container_width=True
                )
            st.markdown("---")

            st.info(
                f"""
        📌 JD Summary

        JD Match Score: {jd_match_score}/100

        Matched Skills: {len(matched_skills)}

        Missing Skills: {len(missing_keywords)}
        """
            )

            if jd_match_score >= 80:

                st.success(
                    "🟢 Excellent JD Match"
                )

            elif jd_match_score >= 60:

                st.info(
                    "🟡 Good JD Match"
                )

            elif jd_match_score >= 40:

                st.warning(
                    "🟠 Average JD Match"
                )

            else:

                st.error(
                    "🔴 Poor JD Match"
                )

            st.markdown("---")

            st.subheader(
                "📋 JD Recommendations & Improvements"
            )

            try:

                result = analyze_jd(
                    text,
                    job_description
                )

                st.write(
                    result
                )

            except Exception as e:

                st.warning(
                    f"Unable to generate JD recommendations: {e}"
                )

        # ==================================
        # ATS MODE
        # ==================================

        else:

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown(f"""
                <div class="card-hover" style="
                background:rgba(255,255,255,0.08);
                backdrop-filter:blur(12px);
                -webkit-backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.15);
                padding:25px;
                border-radius:20px;
                text-align:center;
                color:white;
                ">
                    <h4>📊 ATS Score</h4>
                    <h1>{ats_score}</h1>
                </div>
                """, unsafe_allow_html=True)

            with col2:

                st.markdown(f"""
                <div class="card-hover" style="
                background:rgba(255,255,255,0.08);
                backdrop-filter:blur(12px);
                -webkit-backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.15);
                padding:25px;
                border-radius:20px;
                text-align:center;
                color:white;
                ">
                    <h4>🛠 Skills Found</h4>
                    <h1>{len(skills)}</h1>
                </div>
                """, unsafe_allow_html=True)
                
            with col3:

                st.markdown(f"""
                <div class="card-hover" style="
                background:rgba(255,255,255,0.08);
                backdrop-filter:blur(12px);
                -webkit-backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.15);
                padding:25px;
                border-radius:20px;
                text-align:center;
                color:white;
                ">
                    <h4>🚀 Readiness</h4>
                    <h1>{readiness}</h1>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                st.progress(
                    min(readiness, 100)
                )
                st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:

                st.plotly_chart(
                    create_gauge(
                        ats_score,
                        "ATS Score"
                    ),
                    use_container_width=True
                )

            with col2:

                st.plotly_chart(
                    create_gauge(
                        readiness,
                        "Readiness"
                    ),
                    use_container_width=True
                )
                st.markdown("---")

                st.info(
                    f"""
                📌 Resume Summary

                Skills Found: {len(skills)}

                ATS Score: {ats_score}/100

                Readiness: {readiness}/100
                """
                )

                if ats_score >= 80:

                    st.success(
                        "🟢 Resume Strength: Strong Candidate"
                    )

                elif ats_score >= 60:

                    st.info(
                        "🟡 Resume Strength: Good Candidate"
                    )

                elif ats_score >= 40:

                    st.warning(
                        "🟠 Resume Strength: Average Candidate"
                    )

                else:

                    st.error(
                        "🔴 Resume Strength: Needs Improvement"
                    )
# ==========================================
# Skill Detection
# ==========================================

if page == "🛠 Skill Detection":

    if uploaded_file is None:

        st.info(
            "📄 Please upload a resume."
        )

    else:

        st.header(
            "🛠 Skill Detection"
        )

        # ==========================================
        # RESUME SKILLS
        # ==========================================

        st.subheader(
            "📄 Resume Skills"
        )

        if skills:

            st.success(
                f"Total Skills Detected: {len(skills)}"
            )

            col1, col2 = st.columns(2)

            for i, skill in enumerate(skills):

                card = f"""
                <div class="card-hover" style="
                background:rgba(255,255,255,0.08);
                backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.15);
                padding:12px;
                border-radius:12px;
                margin-bottom:10px;
                color:white;">
                ✅ {skill.title()}
                </div>
                """

                if i % 2 == 0:

                    col1.markdown(
                        card,
                        unsafe_allow_html=True
                    )

                else:

                    col2.markdown(
                        card,
                        unsafe_allow_html=True
                    )

        else:

            st.warning(
                "No skills detected."
            )

        # ==========================================
        # JD SKILL ANALYSIS
        # ==========================================

        if job_description.strip() and st.session_state.jd_mode:

            st.markdown("---")

            # MATCHED SKILLS

            st.subheader(
                "🎯 Matched JD Skills"
            )

            if matched_skills:

                st.success(
                    f"{len(matched_skills)} skills matched with JD"
                )

                col1, col2 = st.columns(2)

                for i, skill in enumerate(matched_skills):

                    card = f"""
                    <div class="card-hover" style="
                    background:rgba(16,185,129,0.15);
                    border:1px solid rgba(16,185,129,0.4);
                    padding:12px;
                    border-radius:12px;
                    margin-bottom:10px;
                    color:white;">
                    ✅ {skill.title()}
                    </div>
                    """

                    if i % 2 == 0:

                        col1.markdown(
                            card,
                            unsafe_allow_html=True
                        )

                    else:

                        col2.markdown(
                            card,
                            unsafe_allow_html=True
                        )

            else:

                st.warning(
                    "No matched skills found."
                )

            st.markdown("---")

            # MISSING SKILLS

            st.subheader(
                "❌ Missing JD Skills"
            )

            if missing_keywords:

                st.error(
                    f"{len(missing_keywords)} skills missing from resume"
                )

                col1, col2 = st.columns(2)

                for i, skill in enumerate(missing_keywords):

                    card = f"""
                    <div class="card-hover" style="
                    background:rgba(239,68,68,0.15);
                    border:1px solid rgba(239,68,68,0.4);
                    padding:12px;
                    border-radius:12px;
                    margin-bottom:10px;
                    color:white;">
                    ❌ {skill.title()}
                    </div>
                    """

                    if i % 2 == 0:

                        col1.markdown(
                            card,
                            unsafe_allow_html=True
                        )

                    else:

                        col2.markdown(
                            card,
                            unsafe_allow_html=True
                        )

            else:

                st.success(
                    "No missing skills."
                )
    # ==========================================
# INTERVIEW QUESTIONS
# ==========================================

if page == "🎯 Interview Questions":

    if job_description.strip() and st.session_state.jd_mode:

        st.header("🎯 JD-Based Interview Questions")

        if st.button(
            "Generate JD Questions",
            key="jd_questions"
        ):

            try:

                with st.spinner(
                    "Generating JD Questions..."
                ):

                    questions = generate_jd_questions(
                        text,
                        job_description
                    )

                    st.write(
                        questions
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

    else:

        st.header("🤖 AI Generated Questions")

        if st.button(
            "Generate AI Questions",
            key="ai_questions"
        ):

            try:

                with st.spinner(
                    "Generating Questions..."
                ):

                    ai_questions = generate_ai_questions(
                        text
                    )

                    st.write(
                        ai_questions
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )
# ==========================================
# ANSWER EVALUATION
# ==========================================

if page == "🤖 Answer Evaluation":

    st.header("🤖 AI Answer Evaluation")

    question = st.text_input(
        "Interview Question"
    )

    answer = st.text_area(
        "Your Answer"
    )

    if st.button(
        "Evaluate Answer",
        key="evaluate"
    ):

        try:

            with st.spinner(
                "Evaluating..."
            ):

                feedback = evaluate_answer(
                    question,
                    answer
                )

                st.write(
                    feedback
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )
# ==========================================
# RESUME SUGGESTIONS
# ==========================================

if page == "🚀 Resume Suggestions":

    st.header(
        "🚀 Resume Improvement Suggestions"
    )

    if st.button(
        "Analyze Resume",
        key="resume_analysis"
    ):

        try:

            with st.spinner(
                "Analyzing Resume..."
            ):

                if job_description.strip() and st.session_state.jd_mode:

                    suggestions = improve_resume_for_jd(
                        text,
                        job_description
                    )

                else:

                    suggestions = improve_resume(
                        text
                    )

                st.write(
                    suggestions
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )
# ==========================================
# CAREER RECOMMENDATIONS
# ==========================================

if page == "🎯 Career Recommendations":

    if job_description.strip() and st.session_state.jd_mode:

        st.info(
            "Career recommendations are hidden when JD analysis is active."
        )

    else:

        st.header(
            "🎯 Career Recommendations"
        )

        try:

            for career in careers:

                st.markdown(f"""
                <div style="
                background:#1e293b;
                padding:20px;
                border-radius:15px;
                margin-bottom:15px;
                border:1px solid #334155;
                ">

                <h3 style="color:white;margin:0;">
                🎯 {career['role']}
                </h3>

                <p style="color:#cbd5e1;">
                💰 Salary: {career['salary']}
                </p>

                <p style="color:#22c55e;">
                🚀 Readiness: {career['readiness']}
                </p>

                </div>
                """, unsafe_allow_html=True)

        except:

            st.info(
                careers
            )
# ==========================================
# PDF REPORT
# ==========================================

# ==========================================
# PDF REPORT
# ==========================================

if page == "📥 PDF Report":

    st.header("📥 PDF Report")

    if uploaded_file is None:

        st.warning(
            "📄 Please upload a resume first."
        )

    else:

        # JD MODE REPORT

        if job_description.strip() and st.session_state.jd_mode:

            report_content = f"""
JD MATCH REPORT

JD Match Score: {jd_match_score}/100

JD Readiness: {jd_readiness}/100

Matched Skills:
{', '.join(matched_skills)}

Missing Skills:
{', '.join(missing_keywords)}
"""

        # ATS MODE REPORT

        else:

            report_content = f"""
ATS REPORT

ATS Score: {ats_score}/100

Readiness: {readiness}/100

Skills Found:
{', '.join(skills)}

Resume Strength:
{"Strong Candidate" if ats_score >= 80 else
"Good Candidate" if ats_score >= 60 else
"Average Candidate" if ats_score >= 40 else
"Needs Improvement"}
"""

        pdf_file = generate_report(
            report_content
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name="resume_report.pdf",
                mime="application/pdf"
            )

