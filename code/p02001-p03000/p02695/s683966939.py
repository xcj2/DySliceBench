def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, deque
from sys import exit
import math

def calc(arr, query):
    ret = 0
    # print(arr)\
    for q in query:
        if arr[q[1] - 1] - arr[q[0] - 1] == q[2]:
            ret += q[3]

    return ret

def dfs(n, m, query, tlen, tail, score, deq):
    if tlen == n:
        return calc(list(deq), query)
    else:
        for i in range(tail, m+1):
            deq.append(i)
            ret = dfs(n, m, query, tlen+1, i, score, deq)
            if ret > score:
                score = ret
            deq.pop()

    return score




def main():
    n,m,q = getList()
    query = []
    for _ in range(q):
        query.append(getList())
    deq = deque([1])
    ans = dfs(n, m ,query, 1, 1, 0, deq)
    print(ans)

if __name__ == "__main__":
    main()