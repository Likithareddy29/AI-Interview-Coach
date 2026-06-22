def calculate_ats_score(skills):

    score = 0

    # Skill Score
    score += min(len(skills) * 5, 50)

    # Bonus for High Value Skills
    high_value_skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "aws",
        "docker",
        "react",
        "github",
        "data structures"
    ]

    for skill in skills:

        if skill.lower() in high_value_skills:
            score += 5

    # Cap at 100
    score = min(score, 100)

    return score