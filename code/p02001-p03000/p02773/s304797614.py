def A():
    A, B, C = map(int, input().split())
    if A == B or B == C or A == C:
        if (A+B+C) != A*3:
            print('Yes')
            return
    print('No')

def B():
    N = int(input())
    A = [int(i) for i in input().split()]
    for i in A:
        if i%2==0 and not (i%3==0 or i%5==0):
            print('DENIED')
            return
    print('APPROVED')

from collections import Counter
from itertools import takewhile
def C():
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(input())

    c = Counter(lst)
    m = max(c.values())
    r = [x for x, _ in takewhile(lambda x: x[1]==m, c.most_common())] 
    for s in sorted(r):
        print(s)
C()