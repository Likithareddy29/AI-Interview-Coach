def recommend_career(skills):

    recommendations = []

    skills = [skill.lower() for skill in skills]

    if (
        "python" in skills and
        "machine learning" in skills
    ):

        recommendations.append({
            "role": "Machine Learning Engineer",
            "salary": "₹5 - ₹12 LPA",
            "readiness": "High"
        })

    if (
        "python" in skills and
        "sql" in skills
    ):

        recommendations.append({
            "role": "Data Analyst",
            "salary": "₹4 - ₹10 LPA",
            "readiness": "High"
        })

    if (
        "html" in skills and
        "css" in skills and
        "javascript" in skills
    ):

        recommendations.append({
            "role": "Frontend Developer",
            "salary": "₹4 - ₹8 LPA",
            "readiness": "Medium"
        })

    if (
        "react" in skills and
        "nodejs" in skills
    ):

        recommendations.append({
            "role": "Full Stack Developer",
            "salary": "₹6 - ₹14 LPA",
            "readiness": "High"
        })

    if (
        "java" in skills
    ):

        recommendations.append({
            "role": "Software Engineer",
            "salary": "₹5 - ₹12 LPA",
            "readiness": "Medium"
        })

    if (
        "aws" in skills or
        "azure" in skills
    ):

        recommendations.append({
            "role": "Cloud Engineer",
            "salary": "₹6 - ₹15 LPA",
            "readiness": "Medium"
        })

    if len(recommendations) == 0:

        recommendations.append({
            "role": "Graduate Engineer Trainee",
            "salary": "₹3 - ₹6 LPA",
            "readiness": "Beginner"
        })

    return recommendations