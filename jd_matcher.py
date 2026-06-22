import re

from skill_extractor import extract_skills


# ==========================================
# CLEAN TEXT
# ==========================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9 ]",
        " ",
        text
    )

    return text


# ==========================================
# JD MATCH SCORE
# ==========================================

def calculate_jd_match(
    resume_text,
    job_description
):

    if not job_description.strip():

        return 0

    resume_skills = set(
        extract_skills(
            resume_text
        )
    )

    jd_skills = set(
        extract_skills(
            job_description
        )
    )

    if len(jd_skills) == 0:

        return 0

    matched = resume_skills.intersection(
        jd_skills
    )

    score = (
        len(matched)
        / len(jd_skills)
    ) * 100

    return round(score)


# ==========================================
# MATCHED SKILLS
# ==========================================

def get_matched_skills(
    resume_text,
    job_description
):

    resume_skills = set(
        extract_skills(
            resume_text
        )
    )

    jd_skills = set(
        extract_skills(
            job_description
        )
    )

    matched = resume_skills.intersection(
        jd_skills
    )

    return sorted(
        list(matched)
    )


# ==========================================
# MISSING SKILLS
# ==========================================

def find_missing_keywords(
    resume_text,
    job_description
):

    resume_skills = set(
        extract_skills(
            resume_text
        )
    )

    jd_skills = set(
        extract_skills(
            job_description
        )
    )

    missing = jd_skills - resume_skills

    return sorted(
        list(missing)
    )