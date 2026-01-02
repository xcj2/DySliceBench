def main():
    n, m = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in [0]*m]
    g = [[] for _ in [0]*n]
    [g[a].append(b) for a, b in abc]

    def closed2(start, g_set, visited):
        root = [start]
        root_set = {start}
        r = 1
        while root_set:
            now = root[r-1]
            if r == 1:
                past = -1
            else:
                past = root[r-2]
            if len(g_set[now]) > 0:
                j = g_set[now].pop()
                if j == past:
                    continue
                if j in root_set:
                    return root
                now = j
                root.append(j)
                root_set.add(j)
                visited.add(j)
                r += 1
            else:
                root_set.remove(now)
                now = past
                root.pop()
                r -= 1
        return []

    def closed(g):
        g_set = [set(i) for i in g]
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            ret = closed2(i, g_set, visited)
            if ret != []:
                return ret
        return []

    print(int(len(closed(g)) > 0))


main()

