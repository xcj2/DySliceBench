
import copy
def fa():  # final answer
    global ans
    print(ans)


def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))

def check_bridge(n, a, b, edge):
    edge[a-1][b-1] = 0
    edge[b-1][a-1] = 0
    link = [1]
    stack = []
    for i in range(n):
        if edge[0][i] == 1:
            link.append(i+1)
            stack.append(i+1)

    while(stack != []):
        dep = stack[0]
        for i in range(n):
            if edge[dep-1][i] == 1:
                if i+1 not in link:
                    link.append(i+1)
                    stack.append(i+1)
        stack = stack[1:]

    if len(link) == n:
        return True
    else:
        return False

n,m = getNM()
edge = [[0 for i in range(n)] for j in range(n)]
pile = []
for i in range(m):
    a,b = getNM()
    edge[a-1][b-1] = 1
    edge[b-1][a-1] = 1
    pile.append((a,b))

ans = 0
for pair in pile:
    a, b = pair[0], pair[1]
    edge2 = copy.deepcopy(edge)
    if check_bridge(n, a, b, edge2) == False:
        ans += 1

print(ans)


