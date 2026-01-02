N,K = map(int,input().split(' '))
R,S,P = map(int,input().split(' '))
T = input()

def reverse_rocks(s):
    if 'r' == s:
        return 'p'
    elif 's' == s:
        return 'r'
    elif 'p' == s:
        return 's'

def except_rocks(s):
    if 'r' == s:
        return ['s','p']
    elif 's' == s:
        return ['r','p']
    elif 'p' == s:
        return ['s','r']

def score(s):
    if 'r' == s:
        return R
    elif 's' == s:
        return S
    elif 'p' == s:
        return P

sum_score = 0
chechs = []
for i in range(N):
    must_not_char = ''
    if i >= K: 
        flag = True
        for c in chechs[i-K]:
            if c != reverse_rocks(T[i]):
                sum_score += score(reverse_rocks(T[i]))
                chechs.append([reverse_rocks(T[i])])
                flag = False
                break
        if flag:
            chechs.append(except_rocks(reverse_rocks(T[i])))
        continue
            
    sum_score += score(reverse_rocks(T[i]))
    chechs.append([reverse_rocks(T[i])])
            
print(sum_score)