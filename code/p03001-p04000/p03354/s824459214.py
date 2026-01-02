# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))


def main():
    def find(x):
        parent = data[x]
        if parent < 0: return x
        root = find(parent)
        data[x] = root
        return root

    def union(x, y):
        root, second = find(x), find(y)
        if root == second: return False
        if data[root] > data[second]:
            second, root = root, second
        data[root] += data[second]
        height[root] = max(height[root], height[second]+1)
        data[second] = root
        return True

    def size(x):
        return -data[find(x)]

    N, M = lr()
    P = lr()
    data = [-1] * (N+1)  # 1-indexed rootには-sizeが入る
    height = [0] * (N+1)

    for _ in range(M):
        x, y = lr()
        union(x, y)
    
    answer = 0
    for i in range(N):
        if find(i+1) == find(P[i]):
            answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()