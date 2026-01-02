# import sys
# input = sys.stdin.readline
import collections

def main():
    n, m = input_list()
    Friend = [[] for i in range(n+1)]
    for _ in range(m):
        a, b = input_list()
        Friend[a].append(b)
        Friend[b].append(a)
    Flag = [False for i in range(n+1)]
    ans = 1
    for i in range(1, n+1):
        if Flag[i]:
            continue
        q = collections.deque()
        q.append(i)
        cnt = 1
        while q:
            st = q.popleft()
            Flag[st] = True
            for j in Friend[st]:
                if Flag[j]:
                    continue
                cnt += 1
                Flag[j] = True
                q.append(j)
            ans = max(ans, cnt)
    print(ans)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
