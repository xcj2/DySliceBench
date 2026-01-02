#  --*-coding:utf-8-*--


def f(N, S, st):
    R = [0]*(N)

    Q = set([st])
    R[st] = 1
    idx = 1
    cnt = 0

    while(len(Q) > 0):
        Q2 = set()
        cnt += 1
        idx += 1
        
        for i in Q:
            for j, s in enumerate(S[i]):
                if s == '1':
                    if R[j] == idx - 1:
                        return -1
                    elif R[j] == 0:
                        R[j] = idx
                        Q2.add(j)
                    
        Q = Q2
        
    return cnt
        


def g(N, S):
    m = 0

    for i in range(N):
        k = f(N, S, i)
        if k == -1:
            return -1

        m = max(m, k)

    return m



def main():
    N = int(input())
    S = list(input() for _ in range(N))

    print(g(N, S))





if __name__ == '__main__':
    main()
