def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n,m,k = map(int,input().split())

    fre = [[] for i in range(n)]

    for i in range(m):
        a,b = map(int,input().split())
        fre[a-1].append(b-1)
        fre[b-1].append(a-1)

    group = [-1]*n
    def check():
        dic = {}
        count = 1
        for i in range(n):
            if group[i] == -1:
                a = dfs(i,count)
                dic[count] = a
                count += 1
        return group,dic

    def dfs(i,count):
        num = 0
        group[i] = count
        q = deque([])
        q.append(i)
        while q:
            bef = q.pop()

            for nex in fre[bef]:
                if group[nex] == -1:
                    group[nex] = count
                    q.append(nex)
                    num += 1
        return num
    group,dic = check()
    ans = []
    for i in range(n):
        a = group[i]
        ans.append([dic[a]-len(fre[i]),a])
    for i in range(k):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        if ans[a][1] == ans[b][1]:
            ans[a][0] -= 1
            ans[b][0] -= 1
    for i,j in ans:
        print(i,end=" ")

if __name__ == "__main__":
    main()

