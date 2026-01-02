import collections
def main():
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        a, b = map(int, input().split())
        bridges.append([a, b])
    bridges = bridges[::-1]
    parent = [i for i in range(N+1)]
    count = dict()
    for i in range(N+1): count[i] = 1

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        pi, pj = find(i), find(j)
        df = 0
        if pi != pj:
            if count[pi] > count[pj]:
                parent[pj] = pi
                df += count[pi] * count[pj]
                count[pi] += count[pj]
                del count[pj]
            else:
                parent[pi] = pj
                df += count[pi] * count[pj]
                count[pj] += count[pi]
                del count[pi]                
        return df

    ans = [N*(N-1)//2]
    for a, b in bridges[:-1]:
        d = union(a, b)
        ans.append(ans[-1]-d)
    return ans[::-1]

if __name__ == '__main__':
    output = main()
    for v in output:
        print(v)