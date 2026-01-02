class Graph(object):
    def __init__(self, size):
        self.size = size
        # node_i belong to group_i
        self.groups = {i: {i} for i in range(1, size+1)}
        self.indicators = {i: i for i in range(1, size+1)}

    def __getitem__(self, i):
        # i: index of node
        ind = self.indicators[i]
        return self.groups[ind]
    
    def union(self, i, j):
        # i, j: index of node
        ind_i = self.indicators[i]
        ind_j = self.indicators[j]

        # update group [N]
        group_j = self.groups.pop(ind_j)
        self.groups[ind_i] = self.groups[ind_i].union(group_j)

        # update indicator [N?]
        for j in group_j:
            self.indicators[j] = ind_i


class UnionFind(object):
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}
        # self.group = {i: [i] for i in range(n)}
        self.size = {i: 1 for i in range(n)}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y

        else:
            self.parent[y] = x

            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

        self.size[x] += self.size[y]
        self.size[y] = self.size[x]


    def get_size(self, x):
        return self.size[self.find(x)]
    #     return len(self.group[x])


def main_naive():
    # N, M
    n_lands, n_bridges = map(int, input().split())
    # A, B
    edges = list()
    for i in range(n_bridges):
        edge = list(map(int, input().split()))
        edges.append(edge)

    ans_list = list()
    ans_list.append(n_lands * (n_lands - 1) // 2)

    graph = Graph(n_lands)
    for edge in edges[::-1]:
        beg, end = edge
        # beg -> end was impossible
        if graph.indicators[beg] != graph.indicators[end]:
            ans = ans_list[-1] - len(graph[beg]) * len(graph[end])

            # unite group
            graph.union(beg, end)

        else:
            ans = ans_list[-1]
        ans_list.append(ans)
        

    # at the initial stage
    assert ans_list[-1] == 0
    ans_list.pop()

    for ans in ans_list[::-1]:
        print(ans)


def main():
    # N, M
    n_lands, n_bridges = map(int, input().split())
    # A, B
    edges = list()
    for i in range(n_bridges):
        edge = list(map(int, input().split()))
        edges.append(edge)

    ans_list = list()
    ans_list.append(n_lands * (n_lands - 1) // 2)

    graph = UnionFind(n_lands)
    for edge in edges[::-1]:
        # print(graph.size)
        beg, end = edge
        beg -= 1
        end -= 1

        # beg -> end was impossible
        if graph.find(beg) != graph.find(end):
            ans = ans_list[-1] - graph.get_size(beg) * graph.get_size(end)

            # unite group
            graph.union(beg, end)

        else:
            ans = ans_list[-1]
        ans_list.append(ans)
        

    # at the initial stage
    assert ans_list[-1] == 0
    ans_list.pop()

    for ans in ans_list[::-1]:
        print(ans)


if __name__ == '__main__':
    main()
    # main_naive()