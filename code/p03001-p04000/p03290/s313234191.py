D, G = [int(i) for i in input().split()]

p = []
c = []
for i in range(D):
    tmp = [int(i) for i in input().split()]
    p.append(int(tmp[0]))
    c.append(int(tmp[1]))

def AccuracyQestionNum(acc_list, count):
    counter = count
    for i in range(len(acc_list)):
        if acc_list[i] == 1:
            counter += p[i]
    return counter

def MaxScoreIndex(acc_list):
    for i in reversed(range(len(acc_list))):
        if acc_list[i] == 0:
            return i
        
def FinalQestionNum(acc_list, score):
    remain_point = G - score
    counter = 0
    max_score_index = MaxScoreIndex(acc_list)
    for i in range(p[max_score_index]):
        remain_point -= (max_score_index+1) * 100
        counter += 1
        if remain_point <= 0:
            break

    if counter == p[max_score_index]:
        return None
    else:
        return counter
        
def ScoreCalculation(acc_list):
    score = 0
    for i in range(len(acc_list)):
        if acc_list[i] == 1:
            score += (i+1) * 100 * p[i]
            score += c[i]
    return score

def DFSQestion(acc_list):
    """先に全探索で得たスコアを計算して, 正解数もカウントしておく"""
    if len(acc_list) == D:
        score = ScoreCalculation(acc_list)
        if score >= G:
            question_num = AccuracyQestionNum(acc_list, 0)
        else:
            count = FinalQestionNum(acc_list, score)
            if count == None:
                return None
            else:
                question_num = AccuracyQestionNum(acc_list, count)
        return question_num
    else:
        question_num1 = DFSQestion(acc_list + [0])
        question_num2 = DFSQestion(acc_list + [1])
        if question_num1 == None:
            return question_num2
        if question_num2 == None:
            return question_num1
        if question_num1 >= question_num2:
            return question_num2
        else:
            return question_num1
        
question_num = DFSQestion([])

print(question_num)



"""
全ての問題に対する全探索(おバカな探索)
sum_question  = 0
for i in range(D):
    sum_question += p[i]

def ScoreCalculation(question_list):
    pre_i = 0
    count = 0
    score = 0
    for p_i in range(len(p)):
        count = sum(question_list[pre_i : pre_i + p[p_i]])
        pre_i += p[p_i]
        score += (p_i+1) * 100 * count
        if count == p[p_i]:
            score += c[p_i]
        
    return score

def DFSAccuracy(question_list):
    if len(question_list) == sum_question:
        score = ScoreCalculation(question_list)
        if score >= G:
            return question_list
        else:
            return None
    else:
        result1 = DFSAccuracy(question_list + [1])
        result2 = DFSAccuracy(question_list + [0])

        if result1 == None:
            return result2
        elif result2 == None:
            return result1
        else:
            que_num1 = sum(result1)
            que_num2 = sum(result2)
            if  que_num1< que_num2:
                return result1
            else:
                return result2

ans_list = DFSAccuracy([])
accuracy_num = sum(ans_list)
print(accuracy_num)
"""