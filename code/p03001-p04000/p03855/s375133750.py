from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline
from math import factorial



def union_r(node):
    global road_union
    if road_union[node] != node:
        road_union[node] = union_r(road_union[node])
    return road_union[node]

def union_t(node):
    global train_union
    if train_union[node] != node:
        train_union[node] = union_t(train_union[node])
    return train_union[node]


road_union, train_union = [], []


def main():
    node_num, road_num, train_num = map(int, input().split())

    global road_union
    road_union = [i for i in range(node_num + 1)]
    for i in range(road_num):
        a, b = map(int, input().split())
        parent_a = union_r(a)
        parent_b = union_r(b)
        road_union[min(parent_a, parent_b)] = max(parent_a, parent_b)
        # print(road_union)

    global train_union
    train_union = [i for i in range(node_num + 1)]
    for i in range(train_num):
        a, b = map(int, input().split())
        parent_a = union_t(a)
        parent_b = union_t(b)
        train_union[min(parent_a, parent_b)] = max(parent_a, parent_b)

    # print(train_union, road_union)

    ryouhou = [0 for i in range(node_num + 1)]
    for i in range(1, node_num + 1):
        parent_r = union_r(i)
        parent_t = union_t(i)
        ryouhou[i] = (parent_r, parent_t)

    # print(train_union, road_union, 'uuu')

    count_d = Counter(ryouhou)

    for i in range(1, node_num + 1):
        now_flg = ryouhou[i]
        print(count_d[now_flg], end=' ')
    print()





if __name__ == '__main__':
    main()