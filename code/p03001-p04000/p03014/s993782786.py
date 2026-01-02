
class UnionFind:

    # n is element num
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * (n + 1)
        self.rnk = [0]*(n+1)

    # find root of x node
    def find_root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find_root(self.parent[x])
            return self.parent[x]

    # union disjoint sets of x and y
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)

        if x == y:
            return

        elif self.rnk[x] > self.rnk[y]:
            self.parent[x] += self.parent[y]  # update num of nodes in united tree
            self.parent[y] = x

        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y

            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    # check x and y are in same tree
    def is_same_tree(self, x, y):
        return self.find_root(x) == self.find_root(y)

    # count nodes in tree what x belong to
    def count_nodes(self, x):
        return -self.parent[self.find_root(x)]


def read_input():
    h, w = map(int, input().split())

    board = []
    for i in range(h):
        board.append([0 if c == '.' else 1 for c in input()])

    return h, w, board


def union(vec):
    u = UnionFind(len(vec))

    for i, (v1, v2) in enumerate(zip(vec, vec[1:])):
        if v1 == v2 == 0:
            u.unite(i, i + 1)

    return u

def submit():
    h, w, board = read_input()

    hunions = []
    for i in range(h):
        hunions.append(union(board[i]))

    wunions = []
    for j in range(w):
        v = [board[i][j] for i in range(h)]
        wunions.append(union(v))


    max_lit = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                hv = hunions[i].count_nodes(j)
                wv = wunions[j].count_nodes(i)

                if max_lit < hv + wv - 1:
                    max_lit = hv + wv - 1


    print(max_lit)



if __name__ == '__main__':
    submit()
