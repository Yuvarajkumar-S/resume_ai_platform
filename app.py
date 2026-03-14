import streamlit as st
import pandas as pd
import plotly.express as px
from skill_gap import detect_skill_gap

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from bert_scorer import score_resume_bert
from ats_simulator import ats_score
from skill_gap import detect_skill_gap
from project_extractor import extract_projects
from local_llm_summary import generate_summary
from vector_resume_search import build_resume_index, search_resumes
from candidate_ranker import rank_candidates
from cover_letter_generator import generate_cover_letter
from job_recommender import recommend_jobs


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Intelligence Platform",
    layout="wide",
    page_icon="🚀"
)

st.title("🚀 AI Resume Intelligence Platform")
st.caption("Next Generation AI Resume Analysis System")


# ---------------- SIDEBAR ----------------

st.sidebar.header("Upload Resume")

resume_file = st.sidebar.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

jd_text = st.sidebar.text_area("Paste Job Description")

st.sidebar.header("Candidate Comparison")

multi_resumes = st.sidebar.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)


# ---------------- HELPER FUNCTIONS ----------------

def detect_sections(text):

    sections = {
        "Education": [],
        "Skills": [],
        "Projects": [],
        "Experience": []
    }

    lines = text.split("\n")

    for line in lines:

        l = line.lower()

        if "education" in l:
            sections["Education"].append(line)

        elif "skill" in l:
            sections["Skills"].append(line)

        elif "project" in l:
            sections["Projects"].append(line)

        elif "experience" in l:
            sections["Experience"].append(line)

    return sections


def score_bullets(text):

    bullets = []

    lines = text.split("\n")

    for line in lines:

        if len(line) > 10 and ("•" in line or "-" in line):
            bullets.append(line)

    scores = []

    action_words = [
        "developed",
        "designed",
        "implemented",
        "built",
        "optimized",
        "created"
    ]

    for b in bullets:

        score = 0

        for w in action_words:

            if w in b.lower():
                score += 2

        if "%" in b or "improved" in b:
            score += 2

        scores.append(score)

    return bullets, scores


# ---------------- MAIN TABS ----------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📄 Resume Insights",
    "📊 Skills Analytics",
    "🧠 Bullet Analysis",
    "🏆 Candidate Ranking",
    "🤖 AI Tools"
])


# ---------------- RESUME ANALYSIS ----------------

if resume_file:

    text = extract_text_from_pdf(resume_file)

    skills = extract_skills(text)

    projects = extract_projects(text)

    bert_score = score_resume_bert(text)

    ats = ats_score(text, skills)

    summary = generate_summary(text)

    sections = detect_sections(text)

    bullets, bullet_scores = score_bullets(text)


    # DASHBOARD METRICS

    col1, col2, col3 = st.columns(3)

    col1.metric("BERT Resume Score", f"{bert_score}/10")

    col2.metric("ATS Score", f"{ats}%")

    col3.metric("Projects Detected", len(projects))


    # ---------------- TAB 1 ----------------

    with tab1:

        st.subheader("Professional Summary")

        st.success(summary)

        st.subheader("Detected Sections")

        st.write(sections)


    # ---------------- TAB 2 ----------------

    with tab2:

        st.subheader("Skill Distribution")

        df = pd.DataFrame({
            "Skill": skills,
            "Count": [1]*len(skills)
        })

        fig = px.bar(df, x="Skill", y="Count")

        st.plotly_chart(fig, use_container_width=True)


    # ---------------- TAB 3 ----------------

    with tab3:

        st.subheader("Bullet Point Impact Score")

        if bullets:

            df = pd.DataFrame({
                "Bullet": bullets,
                "Score": bullet_scores
            })

            st.dataframe(df)

            fig = px.bar(df, x="Bullet", y="Score")

            st.plotly_chart(fig, use_container_width=True)

        else:

            st.info("No bullet points detected")


    # ---------------- TAB 5 ----------------

    with tab5:

        st.subheader("Job Recommendations")

        recommended = recommend_jobs(skills)

        st.write(recommended)


        if jd_text:

            matched, missing = detect_skill_gap(text, jd_text)

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Matching Skills")

                st.success(matched)

            with col2:

                st.subheader("Missing Skills")

                st.error(missing)


        st.divider()

        st.subheader("Generate AI Cover Letter")

        name = st.text_input("Candidate Name")

        if st.button("Generate Cover Letter"):

            letter = generate_cover_letter(name, skills, jd_text)

            st.text_area("Generated Cover Letter", letter, height=300)


# ---------------- MULTIPLE RESUME PROCESSING ----------------

if multi_resumes:

    resume_texts = {}

    for r in multi_resumes:

        t = extract_text_from_pdf(r)

        resume_texts[r.name] = t


    build_resume_index(list(resume_texts.values()))


    with tab4:

        st.subheader("Candidate Ranking")

        ranking = rank_candidates(resume_texts)

        df = pd.DataFrame(ranking, columns=["Candidate", "Score"])

        st.dataframe(df)

        fig = px.bar(df, x="Candidate", y="Score")

        st.plotly_chart(fig, use_container_width=True)


        st.divider()

        st.subheader("Recruiter Semantic Resume Search")

        query = st.text_input("Search resumes by skill or role")

        if query:

            results = search_resumes(query)

            st.write(results)


else:

    st.info("Upload a resume to begin analysis.")