import sys
# sys.setrecursionlimit(100000)
import heapq


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    from collections import Counter
    # 計算量 O(n*log_n + m*log_m)

    # 入力
    n, m = input_int_list()
    hq = list(Counter(input_int_list()).items())  # O(n)
    # 最小値管理にPriorityQueueを使う

    heapq.heapify(hq)  # O(n*log_n)

    queries = []
    for _ in range(m):
        queries.append(input_int_list())

    queries.sort(key=lambda x: x[1], reverse=True)  # O(m * log_m)

    # cが大きい数字から処理したほうが効率的になる
    for b, c in queries:
        while b > 0:
            k, v = heapq.heappop(hq)
            if k >= c:
                heapq.heappush(hq, (k, v))
                break
            else:
                if v == b:
                    heapq.heappush(hq, (c, b))
                    b = 0
                elif v > b:
                    heapq.heappush(hq, (c, b))
                    heapq.heappush(hq, (k, v - b))
                    b = 0
                elif b > v:
                    heapq.heappush(hq, (c, v))
                    b -= v
    ans = 0
    for k, v in hq:
        ans += k * v

    print(ans)

    return


if __name__ == "__main__":
    main()
