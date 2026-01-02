# ALDS1_11_D Connected Components
import sys
import queue


sys.setrecursionlimit(1000000)

def check(adj, foot_print):
    n = len(foot_print)
    que = queue.Queue()
    num = 0
    for i in range(n):
        if foot_print[i] == 0:
            num += 1
            que.put(i)
            foot_print[i] = num
            bfs(adj, que, foot_print, num)


def bfs(adj, que, foot_print, num):
    if not que.empty():
        now = que.get()
        for i in adj[now]:
            if foot_print[i] == 0:
                foot_print[i] = num
                que.put(i)
        bfs(adj, que, foot_print, num)
    else:
        return


def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    adj_list = [[] for _ in range(n)]
    for i in range(m):
        s, t = map(int, sys.stdin.readline().strip().split())
        adj_list[s].append(t)
        adj_list[t].append(s)

    foot_print = [0] * n
    check(adj_list, foot_print)

    q = int(input())
    for i in range(q):
        s, t = map(int, sys.stdin.readline().strip().split())
        if foot_print[s] == foot_print[t]:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    main()

