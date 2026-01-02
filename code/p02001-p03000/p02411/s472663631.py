def end_check(score):
    end_judge = False
    if(score.count("-1") == 3):
        return True
    return end_judge

def evalution_check(score):
    total_score= int(score[0]) + int(score[1])
    re_test_score = int(score[2])

    score_evalution = "F"

    if (score.count("-1") > 1):
        score_evalution = "F"
    elif (total_score >= 80):
        score_evalution = "A"
    elif (total_score >= 65):
        score_evalution = "B"
    elif (total_score >= 50 or re_test_score >= 50):
        score_evalution = "C"
    elif (total_score >= 30):
        score_evalution = "D"


    return score_evalution

def print_evalutions(evalutions):
    for evalution in evalutions:
        print(evalution)

evalutions =[]

while True:
    score = list(input().split())

    if(end_check(score)):
        break

    evalutions.append(evalution_check(score))

print_evalutions(evalutions)

    
