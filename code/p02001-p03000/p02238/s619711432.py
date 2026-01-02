from typing import List


def alds_1_11a():
    n = int(input())
    for i in range(n):
        u, k, *v = map(int, input().split())
        a = [0] * n
        for i_v in v:
            index_v = i_v - 1
            a[index_v] = 1
        print(*a)
    return


def print_matrices_list(matrices_list):
    for index_row in range(len(matrices_list)):
        print(*matrices_list[index_row])
    return


# def depth_first_search(u, stack, color, d):
#     stack.append(u)
#     color[u] = 1
#     while len(stack) != 0:
#     pass


def accept_adjacency_list() -> List[List[int]]:
    n = int(input())
    adjancy_list = []
    for i in range(n):
        list_u = list(map(int, input().split()))
        adjancy_list.append(list_u)
    return adjancy_list


def adjacency_list2adjacency_matrices(adj_list: List[List[int]]) -> List[List[int]]:
    adjancy_matrices = []
    n = len(adj_list)
    for list_u_i in adj_list:
        id_u, degree_k, *list_v = list_u_i
        list_row = [0] * n
        for v_i in list_v:
            list_row[v_i - 1] = 1
        adjancy_matrices.append(list_row)
    return adjancy_matrices


def dfs(adj_mat):
    n = len(adj_mat)
    list_colors = [0] * n  # 0:white, 1:gray, 2:black
    time = 0
    d = [0] * n  # 最初に訪問した頂点uの発見時刻
    f = [0] * n  # uの隣接リストを調べ終えた完了時刻

    for u in range(n):
        if list_colors[u] == 0:
            list_colors, time, d, f = dfs_visit(u, list_colors, adj_mat, d, f, time)

    for u in range(n):
        print(u + 1, d[u], f[u])
    return


def dfs_visit(u: int, list_colors: list, adj_mat: list, d: list, f: list, time: int):
    list_colors[u] = 1  # uを訪問
    time += 1
    d[u] = time
    for v in range(len(list_colors)):  # v:次に探索する場所
        if adj_mat[u][v] == 0:  # uからvに行く辺がないなら次へ
            continue
        if list_colors[v] == 0:  # uからvに道があるかつ行ったことがないなら行く。
            list_colors, time, d, f = dfs_visit(
                u=v, list_colors=list_colors, adj_mat=adj_mat, d=d, f=f, time=time
            )
    list_colors[u] = 2
    time += 1
    f[u] = time
    return list_colors, time, d, f


if __name__ == "__main__":
    # init
    adjacency_list = accept_adjacency_list()
    adjacency_matirces = adjacency_list2adjacency_matrices(adj_list=adjacency_list)

    dfs(adj_mat=adjacency_matirces)

