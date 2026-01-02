import sys
from collections import deque
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]

def main():
    N, Q = MI()
    #木
    tree = [[] for i in range(N)]
    for i in range(N-1):
        a,b = MI()
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    #カウンター保存用、初期化
    counter = [0]* N
    score = [0]* N
    dq = deque()
    dq.append([0,-1])
    for i in range(Q):
        p, x = MI()
        counter[p-1] += x
    score[0] = counter[0]
    #score[tree[0][0]] = counter[tree[0][0]]
    while dq:
        temp, past = dq.pop()
        for num in tree[temp]:
            if num != past:
                score[num] = score[temp]+counter[num]
                dq.append([num,temp])
    score = [str(i) for i in score]
    print(" ".join(score))
    return None

if __name__ == "__main__":
    main()