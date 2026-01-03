
import collections
def main():

    N = int(input())
    city = []
    for i in range(N):
        x, y = map(int, input().split())
        city.append([x, y, i])

    edges = []
    city.sort(key = lambda x: x[0])
    for i in range(N-1):
        edges.append([city[i][2], city[i+1][2], abs(city[i][0]-city[i+1][0])])
    city.sort(key = lambda x: x[1])
    for i in range(N-1):
        edges.append([city[i][2], city[i+1][2], abs(city[i][1]-city[i+1][1])])
    edges.sort(key = lambda x: x[2])

    parent = [a for a in range(N)]
    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    def union(a, b, c):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pb] = pa
            return c, 1
        else:
            return 0, 0

    cost = 0
    connected = N
    for a, b, c in edges:
        cst, cmp = union(a, b, c)
        cost += cst
        connected -= cmp
        if connected == 1:
            return cost



if __name__ == '__main__':
    print(main())