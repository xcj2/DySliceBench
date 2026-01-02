import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,A,B,C = MI()
X = [S() for _ in range(N)]

if A+B+C == 0:
    print('No')

elif A+B+C == 1:
    ANS = []
    for i in range(N):
        if A == 1:
            if X[i] == 'BC':
                print('No')
                break
            elif X[i] == 'AB':
                ANS.append('B')
                A,B,C = 0,1,0
            else:
                ANS.append('C')
                A,B,C = 0,0,1
        elif B == 1:
            if X[i] == 'AC':
                print('No')
                break
            elif X[i] == 'AB':
                ANS.append('A')
                A,B,C = 1,0,0
            else:
                ANS.append('C')
                A,B,C = 0,0,1
        else:
            if X[i] == 'AB':
                print('No')
                break
            elif X[i] == 'BC':
                ANS.append('B')
                A,B,C = 0,1,0
            else:
                ANS.append('A')
                A,B,C = 1,0,0
    else:
        print('Yes')
        print(*ANS,sep='\n')

else:
    if X[0] == 'AB' and C == A+B+C:
        print('No')
    elif X[0] == 'BC' and A == A+B+C:
        print('No')
    elif X[0] == 'AC' and B == A+B+C:
        print('No')
    else:
        print('Yes')
        ANS = []
        if A+B+C >= 3:
            for i in range(N):
                if X[i] == 'AB':
                    if A > B:
                        A -= 1
                        B += 1
                        ANS.append('B')
                    else:
                        A += 1
                        B -= 1
                        ANS.append('A')
                elif X[i] == 'AC':
                    if A > C:
                        A -= 1
                        C += 1
                        ANS.append('C')
                    else:
                        A += 1
                        C -= 1
                        ANS.append('A')
                else:
                    if B > C:
                        B -= 1
                        C += 1
                        ANS.append('C')
                    else:
                        B += 1
                        C -= 1
                        ANS.append('B')
        else:
            for i in range(N):
                if A == B == 1 and X[i] == 'AB' and i < N-1:
                    if X[i+1] == 'AC':
                        ANS.append('A')
                        A += 1
                        B -= 1
                    else:
                        ANS.append('B')
                        A -= 1
                        B += 1
                elif A == C == 1 and X[i] == 'AC' and i < N-1:
                    if X[i+1] == 'AB':
                        ANS.append('A')
                        A += 1
                        C -= 1
                    else:
                        ANS.append('C')
                        A -= 1
                        C += 1
                elif B == C == 1 and X[i] == 'BC' and i < N-1:
                    if X[i+1] == 'AB':
                        ANS.append('B')
                        B += 1
                        C -= 1
                    else:
                        ANS.append('C')
                        B -= 1
                        C += 1
                else:
                    if X[i] == 'AB':
                        if A > B:
                            A -= 1
                            B += 1
                            ANS.append('B')
                        else:
                            A += 1
                            B -= 1
                            ANS.append('A')
                    elif X[i] == 'AC':
                        if A > C:
                            A -= 1
                            C += 1
                            ANS.append('C')
                        else:
                            A += 1
                            C -= 1
                            ANS.append('A')
                    else:
                        if B > C:
                            B -= 1
                            C += 1
                            ANS.append('C')
                        else:
                            B += 1
                            C -= 1
                            ANS.append('B')

        print(*ANS,sep='\n')

