import sys
def input(): return sys.stdin.readline().strip()


def prod_max(a, d, b, e, n):
    """
    初項a、公差dの等差数列および初項b、公差eの等差数列を各項ごとに
    掛け合わせた時の第0項から第n項までの最大値を返す。
    a>0, d>0, b>0, e<0を仮定する。
    """
    if n < 0: return 0
    idx = round((-(b / e) - (a / d)) / 2)
    if idx < 0: return a * b
    if idx <= n: return (a + idx * d) * (b + idx * e)
    return (a + n * d) * (b + n * e)

def main():
    """
    解説放送にしたがって決め打ち二分探索による実装。
    まずa<=bを仮定しても良い。a*bよりも小さい積がX個作れるかを考える。
    これは1, 2, ..., a-1, a+1, ...からX個、1, 2, ..., b-1, b+1, ...からX個選んで
    小さいものと大きいもののペアで積を取ったものが全てa*b未満であることをいえば良い。

    積を実際に全て計算していては間に合わないが、実質これは等差数列の積なので
    これらの積のうち最大値はO(1)で計算可能。
    """
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        if a > b: a, b = b, a

        # 決め打ち二分探索
        left = a - 1
        right = 10 ** 10
        while right - left > 1:
            mid = (left + right) // 2
            if mid < b:
                """
                この時ペアリングは
                1*mid, 2*(mid-1), ..., (a-1)*(mid-a+1), (a+1)*(mid-a), ..., (mid+1)*1
                前半後半でそれぞれ最大値を取得する。
                """
                cand1 = prod_max(1, 1, mid, -1, a-2)
                cand2 = prod_max(a+1, 1, mid-a+1, -1, mid-a)
                if cand1 < a * b and cand2 < a * b: left = mid
                else: right = mid
                #print("case1 left={}, right={}".format(left, right))
            elif mid < a + b - 1:
                """
                この時ペアリングは
                1*(mid+1), 2*mid, ..., (mid-b+1)*(b+1),
                (mid-b+2)*(b-1), ..., (a-1)*(mid-a+2),
                (a+1)*(mid-a+1), ..., (mid+1)*1
                より3つに分けて最大値を求める。
                """
                cand1 = prod_max(1, 1, mid+1, -1, mid-b)
                cand2 = prod_max(mid-b+2, 1, b-1, -1, a+b-mid-3)
                cand3 = prod_max(a+1, 1, mid-a+1, -1, mid-a)
                if cand1 < a * b and cand2 < a * b and cand3 < a * b: left = mid
                else: right = mid
                #print("case2 left={}, right={}".format(left, right))
            else:
                """
                この時ペアリングは
                1*(mid+1), 2*mid, ..., (mid-a+3)*(a-1),
                (a+1)*(mid-a+2), ..., (mid-b+2)*(b+1),
                (mid-b+3)*(b-1), ..., (mid+1)*1
                より3つに分けて最大値を求める。
                """
                cand1 = prod_max(1, 1, mid+1, -1, a-2)
                cand2 = prod_max(a+1, 1, mid-a+2, -1, mid-a-b+1)
                cand3 = prod_max(mid-b+3, 1, b-1, -1, b-2)
                if cand1 < a * b and cand2 < a * b and cand3 < a * b: left = mid
                else: right = mid
                #print("case3 left={}, right={}".format(left, right))
        print(left)


if __name__ == "__main__":
    main()
