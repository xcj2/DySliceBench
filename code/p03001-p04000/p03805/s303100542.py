ans = 0
to = []

def main():
    global to
    n, m = map(int, input().split())
    to = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        to[a].append(b)
        to[b].append(a)
    #print(f'{to = }')
    solve(n, m)
    print(ans)

def dfs(pos, arrived):

    global ans

    #print(f'{pos = }')
    ##print(f'{to[pos] = }')

    arrived[pos] = True

    #全部到達した
    if all(arrived):
        #print('arrived')
        ans += 1
        return

    for nt in to[pos]:
        if arrived[nt] == False:
            dfs(nt, [i for i in arrived])

def solve(n, m):
    arrived = [False for i in range(n)]
    dfs(0, arrived)
    return


if __name__ == '__main__':
    main()