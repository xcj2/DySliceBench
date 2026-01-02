from collections import Counter

# sys.setrecursionlimit(100000)
from heapq import heappop, heappush, heapify


def main():
    h, w = [int(i) for i in input().strip().split()]
    s = ""
    for _ in range(h):
        s += input().strip()
    counts = Counter(s).most_common()
    cands = [-int(i) for v, i in counts]

    def pop(): return -heappop(cands)
    def push(x): return heappush(cands, -x)

    tasks = [4] * (h // 2) * (w // 2)
    tasks += [2] * ((h % 2) * (w // 2) + (w % 2) * (h // 2))
    tasks += [1] * ((h % 2) * (w % 2))

    flag = True
    for e in tasks:
        c = pop()
        if c < e:
            flag = False
            break
        push(c - e)

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
