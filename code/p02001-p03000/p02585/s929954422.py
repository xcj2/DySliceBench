N, K = [int(i) for i in input().split()]
P = [int(i)-1 for i in input().split()]
C = [int(i) for i in input().split()]
def f(s):
    tmp = s
    circle_length = 0
    circle_score = 0
    for i in range(1, N+1):
        tmp = P[tmp]
        circle_length += 1
        circle_score += C[tmp]
        if s == tmp:
            return (True, circle_length, circle_score)
        if i == K:
            return (False, K, -10**10)

def f1(s, circle_length):
    tmp = s
    max_score = -10**10
    tmp_score = 0
    for i in range(1, circle_length+1):
        tmp = P[tmp]
        tmp_score += C[tmp]
        if max_score < tmp_score:
            max_score = tmp_score
        if tmp_score < 0:
            return max_score
        if i == K:
            return max_score
    return max_score

def f2(s, circle_length, circle_score):
    max_score = (K//circle_length) * circle_score
    tmp = s
    tmp_score = 0
    for i in range(1, (circle_length)+1):
        tmp = P[tmp]
        tmp_score += C[tmp]
        score = ((K-i)//circle_length) * circle_score + tmp_score
        if max_score < score:
            max_score = score
        if tmp_score < 0:
            return max_score
        if i == K:
            return max_score
    return max_score

tot_max = -10**10
for i in range(N):
    is_circle, circle_length, circle_score = f(i)
    max_score = f1(i, circle_length)
    if is_circle and circle_score > 0:
        max_score2 = f2(i, circle_length, circle_score)
        if max_score2 > max_score:
            max_score = max_score2
    if max_score > tot_max:
        tot_max = max_score
print(tot_max)
