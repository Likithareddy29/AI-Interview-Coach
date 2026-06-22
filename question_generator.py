def generate_questions(skills):

    questions = []

    if "python" in skills:
        questions.extend([
            "What is Python?",
            "Difference between List and Tuple?",
            "What are Functions in Python?"
        ])

    if "sql" in skills:
        questions.extend([
            "What is a Primary Key?",
            "Difference between DELETE and DROP?"
        ])

    if "machine learning" in skills:
        questions.extend([
            "What is Machine Learning?",
            "What is Overfitting?"
        ])

    if "java" in skills:
        questions.extend([
            "What is OOP?",
            "What is Inheritance?"
        ])

    return questions