def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A.sort()
    from collections import deque

    def make1():
        d = deque(A)
        ret = deque([d.popleft()])
        for i in range((N-1)//2):
            if i & 1:
                j = d.popleft()
                k = d.popleft()
            else:
                j = d.pop()
                k = d.pop()
            if abs(ret[0] - j) < abs(ret[-1] - j):
                ret.appendleft(j)
                ret.append(k)
            else:
                ret.append(j)
                ret.appendleft(k)
        if len(d) == 1:
            j = d.pop()
            if abs(ret[0] - j) < abs(ret[-1] - j):
                ret.append(j)
            else:
                ret.appendleft(j)
        ans = 0
        for i in range(1, N):
            ans += abs(ret[i-1] - ret[i])
        return ans

    def make2():
        d = deque(A)
        ret = deque([d.pop()])
        for i in range((N-1)//2):
            if i & 1:
                j = d.pop()
                k = d.pop()
            else:
                j = d.popleft()
                k = d.popleft()
            if abs(ret[0] - j) < abs(ret[-1] - j):
                ret.appendleft(j)
                ret.append(k)
            else:
                ret.append(j)
                ret.appendleft(k)
        if len(d) == 1:
            j = d.pop()
            if abs(ret[0] - j) < abs(ret[-1] - j):
                ret.append(j)
            else:
                ret.appendleft(j)
        ans = 0
        for i in range(1, N):
            ans += abs(ret[i-1] - ret[i])
        return ans

    print(max(make1(), make2()))


if __name__ == '__main__':
    main()
