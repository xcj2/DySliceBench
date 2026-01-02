def A():
    c = input()
    print(chr(ord(c)+1))

def B():
    temp = [int(k) for k in input().split()]
    N = temp[0]
    K = temp[1]
    M = temp[2]
    A = [int(k) for k in input().split()]
    ans = M*N - sum(A)
    if ans <= K:
        print(max(0, ans))
    else:
        print(-1)

from collections import defaultdict
def C():
    temp = [int(k) for k in input().split()]
    N = temp[0]
    M = temp[1]
    penal = defaultdict(int)
    P = []
    S = []
    for i in range(M):
        temp = input().split()
        P.append(int(temp[0]))
        S.append(temp[1])
    ac_problems = set()

    for i in range(M-1, -1, -1):
        if P[i] not in ac_problems and S[i] == 'AC':
            ac_problems.add(P[i])
        elif P[i] in ac_problems:
            if S[i] == 'WA':
                penal[P[i]] += 1
            elif S[i] == 'AC':
                penal[P[i]] = 0
    
    print(len(ac_problems), sum(penal.values()))

def D():
    temp = [int(k) for k in input().split()]
    H = temp[0]
    W = temp[1]
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def bfs(x, y):
        to_visit = [(x, y, 0)]
        visited = set()
        ret = 0
        while to_visit:
            x, y, distance = to_visit[0]
            del to_visit[0]
            if (x, y) in visited:
                continue
            visited.add((x, y))
            ret = max(distance, ret)
            for d in directions:
                if x+d[0] < H and x+d[0] >= 0:
                    if y+d[1] < W and y+d[1] >= 0:
                        if (x+d[0], y+d[1]) not in visited:
                            if S[x+d[0]][y+d[1]] == '.':
                                to_visit.append((x+d[0], y+d[1], distance+1))
        #print(memo)
        return ret

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans = max(bfs(i, j), ans)
                
    #print(memo)

    print(ans)

D()