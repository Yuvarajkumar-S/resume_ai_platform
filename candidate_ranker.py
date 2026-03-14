from bert_scorer import score_resume_bert

def rank_candidates(resumes):

    ranking = []

    for name, text in resumes.items():

        score = score_resume_bert(text)

        ranking.append((name, score))

    ranking.sort(key=lambda x: x[1], reverse=True)

    return ranking