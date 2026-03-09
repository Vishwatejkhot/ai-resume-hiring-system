def calculate_ats(skill_match, experience_score, keyword_score):

    score = (
        0.4 * skill_match +
        0.3 * experience_score +
        0.3 * keyword_score
    )

    return round(score, 2)