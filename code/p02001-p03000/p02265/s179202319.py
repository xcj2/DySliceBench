import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()
    command = [LSS() for _ in range(n)]

    que = collections.deque()
    for i in command:
        if i[0]=='insert':
            que.appendleft(i[1])
        elif i[0]=='delete':
            if i[1] in que:
                que.remove(i[1])
        elif i[0]=='deleteFirst':
            que.popleft()
        elif i[0]=='deleteLast':
            que.pop()

    print(*que)

if __name__ == '__main__':
    resolve()
