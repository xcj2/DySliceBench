import math

P = []
# 素数一覧リスト
Max = 1000000

def Era(P, Max) :
    D = list(range(2, Max))
    limit = math.sqrt(Max)
    while True :
        p = D[0]
        
        if limit <= p :
            P += D
            return P
        
        P.append(p)
        D = [d for d in D if d % p != 0]
        
def Sub(x) :
    return abs(x - n)

def Sub2(x) :
    return abs(x - n // 2)

def Near(List, num):
# Listからnumに最も近い値を返す

    Ind = list(map(Sub, List))
    ind = min(Ind)
    # list要素とnumの差分を計算し最小値のインデックスを取得
    return Ind.index(ind)

def Near2(List, num):

    Ind = list(map(Sub2, List))
    ind = min(Ind)
    return Ind.index(ind)

Era(P, Max)

while True :
    n = int(input())
    
    if n == 0 :
        break
    else :
        l = Near2(P, n // 2) + 1
        N = Near(P, n) + 1
        cnt = 0
        s = 0
        I = []
        
        for i in range(N + 1, l - 2, -1) :
            for j in range(s, l + 1) :
                if n == P[i] + P[j] :
                    if P[j] not in I :
                        cnt += 1
                        s = j
                        I.append(P[i])
                        
                elif n < P[i] + P[j] :
                    break
                    
        print(cnt)
        

