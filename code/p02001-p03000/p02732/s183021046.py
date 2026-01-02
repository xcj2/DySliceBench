import math
def A():
    N, M = map(int, input().split())
    if N == 1 == M:
        print(0)
        return
    ans = 0
    if N > 1:
        ans += math.factorial(N)//(2*(math.factorial(N-2)))
    if M > 1:
        ans += math.factorial(M)//(2*(math.factorial(M-2)))
    print(ans)

def B():
    S = input()
    if not S:
        print('No')
        return
    # for i in range(len(S)//4):
    #     # print(S[i], S[len(S)//2-i-1], S[len(S)//2+i+1], S[-i-1])
    #     if not (S[i] == S[(len(S)-1)//2-i-1] == S[(len(S)+3)//2+i-1] == S[-i-1]):
    #         print('No')
    #         return
    for i in range(len(S)):
        if not S[i] == S[len(S)-i-1]:
            print('No')
            return
    for i in range((len(S)-1)//2):
        if not S[i] == S[(len(S)-1)//2-i-1]:
            print('No')
            return
        if not S[(len(S)+3)//2+i-1] == S[len(S)-i-1]:
            print('No')
            return
    print('Yes')

import math
def C():
    L = int(input())
    print(math.pow((L/3), 3))

from collections import Counter
def D():
    N = int(input())
    A = [int(i) for i in input().split()]
    counts = Counter(A)
    combi = 0
    for a in counts:
        if counts[a] > 1:
            combi += math.factorial(counts[a])//(2*(math.factorial(counts[a]-2)))
    for k in range(N):
        print(max(0, combi-(counts[A[k]]-1)))
D()