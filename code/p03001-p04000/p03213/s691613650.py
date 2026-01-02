def d_756(N):
    def exponential_list(n):
        # ret[k]: nを素因数分解したときのkの指数
        ret = [0] * (n + 1)
        for j in range(2, n + 1):
            current = j
            for k in range(2, j + 1):
                while current % k == 0:
                    ret[k] += 1
                    current //= k
        return ret

    def num(m):
        # Nを素因数分解したときの指数のリスト(e)について、
        # 要素の値がm-1より大きなものの個数
        return len(list(filter(lambda x: x >= m - 1, e)))

    e = exponential_list(N)
    # 素因数のうち、指数が74以上の数を1つ選ぶ。約数の個数の性質より、
    # その数の約数の個数は75以上であるから、約数の個数がちょうど75の数が得られる
    ans = num(75)
    # 指数が24以上の数と3以上の数を1つずつ選ぶと、約数の個数の性質より、
    # それらの数の積における約数の個数は75以上である
    # -1しているのは、指数が2以上の素因数のうち1つを指数が24以上の素因数として
    # (それが存在するならば)選んでいるから
    ans += num(25) * (num(3) - 1)
    ans += num(15) * (num(5) - 1)  # 同上
    # 指数が4以上の素因数を重複して数えている(p^4q^4=q^4p^4)ため、2で割る
    ans += num(5) * (num(5) - 1) * (num(3) - 2) // 2
    return ans

N = int(input())
print(d_756(N))