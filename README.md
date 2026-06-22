## Live Demo

🔗 Live Application: https://ai-interview-coach-gr9apws3negwhbdtlezbks.streamlit.app/

🔗 GitHub Repository: https://github.com/Likithareddy29/AI-Interview-Coach

# 🚀 AI Interview Coach

AI Interview Coach is an AI-powered Resume Analysis and Interview Preparation platform built using Python, Streamlit, and Groq LLM.

The application helps users analyze resumes, evaluate ATS compatibility, compare resumes against job descriptions, identify skill gaps, generate interview questions, and receive AI-powered recommendations.

---

## ✨ Features

### 📄 Resume Analysis
- Upload Resume (PDF)
- Extract Resume Content
- ATS Score Evaluation
- Resume Readiness Analysis

### 🛠 Skill Detection
- Detect Technical Skills
- Detect Resume Keywords
- JD Skill Matching
- Missing Skill Identification

### 🎯 Job Description Matching
- JD Match Score
- JD Readiness Score
- Missing Skills Analysis
- AI-Powered JD Recommendations

### 🤖 Interview Preparation
- AI Interview Question Generation
- JD-Based Interview Questions
- Answer Evaluation & Feedback

### 🚀 Resume Improvement
- Resume Enhancement Suggestions
- JD-Based Resume Optimization
- Career Recommendations

### 📥 Reporting
- Download PDF Reports
- ATS Summary
- JD Match Summary

---

## 🛠 Technologies Used

- Python
- Streamlit
- Groq API
- Plotly
- PDFPlumber
- ReportLab

---

## 📂 Project Structure

```text
AI_Interview_Coach/
│
├── app.py
├── config.py
├── ats_score.py
├── readiness_score.py
├── skill_extractor.py
├── jd_matcher.py
├── jd_analyzer.py
├── jd_questions.py
├── question_generator.py
├── groq_helper.py
├── answer_evaluator.py
├── resume_improver.py
├── jd_resume_improver.py
├── career_recommender.py
├── report_generator.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Interview-Coach.git
cd AI-Interview-Coach
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a file named:

```python
config.py
```

Add:

```python
GROQ_API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🎯 Future Enhancements

- Resume Ranking System
- Multi-Resume Comparison
- AI Resume Builder
- LinkedIn Profile Analysis
- Company-Specific Interview Preparation
- Voice-Based Mock Interviews

---

## 👩‍💻 Author

**Lakkam Likitha Reddy**

B.Tech - Artificial Intelligence & Machine Learning

CMR College of Engineering & Technology

Graduation Year: 2026

---

## 📜 License

This project is developed for educational and portfolio purposes.
