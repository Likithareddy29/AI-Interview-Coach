def calculate_readiness_score(
    ats_score,
    skills_count
):

    score = 0

    score += ats_score * 0.6

    score += min(skills_count * 4, 40)

    score = min(int(score), 100)

    return score