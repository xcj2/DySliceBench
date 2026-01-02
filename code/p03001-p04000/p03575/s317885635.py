from sys import stdin, stdout
def readLine_int_list():return list(map(int, stdin.readline().split()))


n,m = readLine_int_list()
g = [[] for j in range(n)]

for i in range(m):
    a,b = readLine_int_list()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    

prenum = [None] * n
parent = [None] * n
lowest = [None] * n
counter = 0
bridges = set()
 
 
def dfs(cur, prev):
    global counter
    prenum[cur] = lowest[cur] = counter
    counter += 1
    for edge in g[cur]:
        if prenum[edge] is not None:
            if edge != prev:
                lowest[cur] = min(lowest[cur], prenum[edge])
            continue
        parent[edge] = cur
        dfs(edge, cur)
        lowest[cur] = min(lowest[cur], lowest[edge])
    if prenum[cur] == lowest[cur]:
        bridges.add((cur, prev) if cur < prev else (prev, cur))

def main():
    dfs(0, -1)
    print(len(bridges)-1)
    
if __name__ == "__main__":
    main()
