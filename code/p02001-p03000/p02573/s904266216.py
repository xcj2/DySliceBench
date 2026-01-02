import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    from collections import deque
    N, M = MI()
    fri_list = [[] for _ in range(N)]
    for i in range(M):
        a, b = MI()
        fri_list[a - 1].append(b - 1)
        fri_list[b - 1].append(a - 1)

    #print(fri_list)
    group_list = []
    num_list = [0] * N
    for i in range(0, N):
        if num_list[i] == 0:
            num_list[i] = 1
            #print(i, 'i')
            cnt = 1
            queue = deque([i])
            while queue:
                v = queue.popleft()
                #print(v, 'v')
                for j in fri_list[v]:
                    #print(j, 'j')
                    if num_list[j] == 0:
                        num_list[j] = 1
                        queue.append(j)
                        cnt += 1
            group_list.append(cnt)

    ans = max(group_list)
    print(ans)

if __name__ == "__main__":
    main()