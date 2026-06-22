skills_db = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "javascript",

    # Web Development
    "html",
    "css",
    "react",
    "nodejs",
    "angular",

    # Databases
    "sql",
    "mysql",
    "mongodb",
    "dbms",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "computer vision",
    "tensorflow",
    "pytorch",
    "opencv",
    "scikit learn",

    # Data Science
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "power bi",
    "tableau",
    "excel",

    # Core CS
    "data structures",
    "algorithms",
    "operating systems",
    "computer networks",

    # Cloud & Tools
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "linux",
    "git",
    "github",
    "streamlit",

    # Soft Skills
    "communication",
    "communication skills",
    "leadership",
    "teamwork",
    "problem solving",
    "analytical thinking",
    "time management",

    # HR
    "recruitment",
    "payroll",
    "employee relations",
    "hrms",

    # Mechanical
    "autocad",
    "solidworks",
    "catia",

    # Civil
    "staad pro",
    "revit",

    # Testing
    "selenium",
    "manual testing",
    "automation testing"
]


def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills_db:

        if skill.lower() in text:

            found_skills.append(skill)

    return sorted(
        list(set(found_skills))
    )