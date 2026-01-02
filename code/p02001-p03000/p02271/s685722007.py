def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    m = list(map(int, input().split()))

    res = list()

    def mul(a, b):
        return a * b

#   # bit探索
    # for i in range(2**n):
    #     x = [0] * n
    #     for j in range(n):
    #         if(i >> j) & 1:
    #             x[j] = 1
    #     res.append(sum(list(map(mul, a, x))))
    # for i in m:
    #     if i in res:
    #         print('yes')
    #     else:
    #         print('no')
#   # 再帰
    def dfs(A):
        # 終端条件 --- nループまで回したら処理して打ち切り
        if len(A) == n:
            # print(A)
            res.append(sum(list(map(mul, a, A))))
            return
        for v in range(2):
            A.append(v)
            dfs(A)
            A.pop()
    dfs([])
    for i in m:
        if i in res:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    main()
