import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque

    n = int(readline())
    a = [int(readline()) for _ in range(n)]
    a.sort()

    def calc1():
        b = deque(a)

        que = deque()
        que.append(b.popleft())

        while b:
            if len(b) >= 2:
                que.append(b.pop())
                que.appendleft(b.pop())
            elif len(b) == 1:
                if abs(que[0] - b[0]) > abs(que[-1] - b[0]):
                    que.appendleft(b.pop())
                else:
                    que.append(b.pop())
            if len(b) >= 2:
                que.append(b.popleft())
                que.appendleft(b.popleft())
            elif len(b) == 1:
                if abs(que[0] - b[0]) > abs(que[-1] - b[0]):
                    que.appendleft(b.popleft())
                else:
                    que.append(b.popleft())
        score = 0
        prev = que[0]
        for x in que:
            score += abs(x - prev)
            prev = x
        return score

    def calc2():
        b = deque(a)

        que = deque()
        que.append(b.pop())

        while b:
            if len(b) >= 2:
                que.append(b.popleft())
                que.appendleft(b.popleft())
            elif len(b) == 1:
                if abs(que[0] - b[0]) > abs(que[-1] - b[0]):
                    que.appendleft(b.popleft())
                else:
                    que.append(b.popleft())
            if len(b) >= 2:
                que.append(b.pop())
                que.appendleft(b.pop())
            elif len(b) == 1:
                if abs(que[0] - b[0]) > abs(que[-1] - b[0]):
                    que.appendleft(b.pop())
                else:
                    que.append(b.pop())
        score = 0
        prev = que[0]
        for x in que:
            score += abs(x - prev)
            prev = x
        return score

    print(max(calc1(), calc2()))


if __name__ == '__main__':
    main()
