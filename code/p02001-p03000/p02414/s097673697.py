class Matrix:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        if values is not None:
            self.values = values
        else:
            row = [0 for i in range(cols)]
            self.values = [row[:] for j in range(rows)]

    def row(self, i):
        return self.values[i-1]

    def col(self, j):
        return [row[j-1] for row in self.values]

    def __mul__(self, other):
        assert self.cols == other.rows

        m = self.__class__(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                m[i, j] = sum(a * b for (a, b) in zip(self.row(i),
                                                      other.col(j)))
        return m

    def __getitem__(self, idx):
        row, col = idx
        return self.values[row-1][col-1]

    def __setitem__(self, idx, val):
        row, col = idx
        self.values[row-1][col-1] = val

    def __str__(self):
        s = []
        for row in self.values:
            s.append(" ".join([str(i) for i in row]))
        return "\n".join(s)


def run():
    n, m, l = [int(v) for v in input().split()]

    m1 = []
    for i in range(n):
        m1.append([int(v) for v in input().split()])

    m2 = []
    for i in range(m):
        m2.append([int(v) for v in input().split()])

    print(Matrix(n, m, m1) * Matrix(m, l, m2))


run()
