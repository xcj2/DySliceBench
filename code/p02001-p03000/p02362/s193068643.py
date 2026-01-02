import collections
import sys
sys.setrecursionlimit(100000)

# ---- belmann-ford -----
V_num, E_num, r = [int(ele) for ele in input().split()]
adjc_list = []
edges = []
for _ in range(V_num):
    adjc_list.append([])

for _ in range(E_num):
    src, dst, w = [int(ele) for ele in input().split()]
    adjc_list[src].append([w, dst])
    edges.append([src, dst, w])

INF = 99999999999999
d = [INF for _ in range(V_num)]
d[r] = 0

# ---- dfs ----
stack = collections.deque()
yet = [ele for ele in range(V_num)]


def main():
    global edges
    # 連結成分の調査
    stack.clear()
    stack.appendleft(r)
    dfs(stack)
    # yet に残っているやつは非連結成分なので、bellman_fordの探索する辺リストから除外する
    edges = list(filter(lambda e: e[0] not in yet and e[1] not in yet, edges))
    output_ans() if bellman_ford() != -1 else print("NEGATIVE CYCLE")


def dfs(stack):
    if not stack:
        return

    n = stack[0]
    yet.remove(n)

    for _, dst in adjc_list[n]:  # stackの表面
        if dst in yet:  # 未訪問なら
            stack.appendleft(dst)
            dfs(stack)
    else:
        stack.popleft()


def bellman_ford():
    for _ in range(V_num - 1):
        for src, dst, w in edges:
            if d[dst] > w + d[src]:
                d[dst] = w + d[src]

    for src, dst, w in edges:
        if d[dst] > w + d[src]:
            return -1

    return


def output_ans():
    for d_i in d:
        if d_i == INF:
            print("INF")
        else:
            print(d_i)


if __name__ == "__main__":
    main()

