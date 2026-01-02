cnt = 0

def main():
    n = int(input())
    m = len(str(n))
    nl = len(str(n))

    def cal(A):
        l = len(A) - 1
        ans = 0
        for idx, i in enumerate(A):
            ans += i*10**(l - idx)
        return ans

    def dfs(A):
        global cnt
        if len(A) == m:
            if len(list(set(A) & set([3, 5, 7]))) == 3:
                if (cal(A)) <= n:
                    # print(cal(A))
                    cnt += 1
            return
        for i in (3, 5, 7):
            A.append(i)
            dfs(A)
            A.pop()
    for m in range(nl+1):
         dfs([])
    print(cnt)

if __name__ == '__main__':
    main()