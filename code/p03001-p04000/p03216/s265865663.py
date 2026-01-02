import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
S = LS2()
Q = I()
K = LI()


def query(k):
    res = 0
    a = 0  # (i-k,i] にあるDの個数
    b = 0  # (i-k,i] にあるMの個数
    c = 0  # (i-k,i] にある(D,M)の個数
    for i in range(N):
        if i >= k:
            if S[i-k] == 'D':
                a -= 1
                c -= b
            elif S[i-k] == 'M':
                b -= 1
        if S[i] == 'D':
            a += 1
        elif S[i] == 'M':
            b += 1
            c += a
        elif S[i] == 'C':
            res += c
    return res


print(*[query(k) for k in K],sep='\n')
