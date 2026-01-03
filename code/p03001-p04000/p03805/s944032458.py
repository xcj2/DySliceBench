def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))

def tansaku(already, paths, cur, n):
    global ans
    aim = [i for i in paths[cur] if i not in already]
    #print(cur,aim,already,ans)
    if aim == []:
        if len(already) == n-1:
            #print("here")
            ans += 1
        return

    for a in aim:
        tansaku(already+[cur], paths, a, n)

N, M = getNM()
paths = [[] for i in range(N)]
ans = 0
for i in range(M):
    a, b = getNM()
    paths[a-1].append(b-1)
    paths[b-1].append(a-1)

tansaku([], paths, 0, N)
print(ans)

