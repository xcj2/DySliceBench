def A():
    c = input()
    print(chr(ord(c)+1))

def B():
    temp = [int(k) for k in input().split()]
    N = temp[0]
    K = temp[1]
    M = temp[2]
    A = [int(k) for k in input().split()]
    ans = M*N - sum(A)
    if ans <= K:
        print(max(0, ans))
    else:
        print(-1)

from collections import defaultdict
def C():
    temp = [int(k) for k in input().split()]
    N = temp[0]
    M = temp[1]
    penal = defaultdict(int)
    P = []
    S = []
    for i in range(M):
        temp = input().split()
        P.append(int(temp[0]))
        S.append(temp[1])
    ac_problems = set()

    for i in range(M-1, -1, -1):
        if P[i] not in ac_problems and S[i] == 'AC':
            ac_problems.add(P[i])
        elif P[i] in ac_problems:
            if S[i] == 'WA':
                penal[P[i]] += 1
            elif S[i] == 'AC':
                penal[P[i]] = 0
    
    print(len(ac_problems), sum(penal.values()))
C()