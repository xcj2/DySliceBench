import sys
input = sys.stdin.readline

class CumulativeSum2D:
    def __init__(self, field):
        self.h = len(field)
        self.w = len(field[0])
        self.h_offset = self.h
        self.w_offset = self.w
        self.field = field
        self.cumsum = [[0] * (self.w + self.w_offset * 2) for _ in range(self.h_offset)]
        for line in self.field:
            self.cumsum.append([0] * self.w_offset + line + [0] * self.w_offset)
        for i in range(self.h_offset):
            self.cumsum.append([0] * (self.w + self.w_offset * 2))
    
    def calc_diagonal_cumsum(self):
        # Calc ul to dr
        for h in range(self.h_offset, self.h_offset + self.h):
            delta = 1
            while delta + h < self.h_offset * 2 + self.h and self.w_offset + delta < self.w_offset * 2 + self.w:
                self.cumsum[h + delta][self.w_offset + delta] += self.cumsum[h + delta-1][self.w_offset + delta-1]
                delta += 1
        for w in range(self.w_offset + 1, self.w_offset + self.w):
            delta = 1
            while delta + w < self.w_offset * 2 + self.w and self.h_offset + delta < self.h_offset * 2 + self.h:
                self.cumsum[self.h_offset + delta][w + delta] += self.cumsum[self.h_offset + delta - 1][w + delta - 1]
                delta += 1
    
    def get_diagonal_sum(self, x1, y1, x2, y2):
        ret = self.cumsum[y2 + self.h_offset][x2 + self.w_offset]
        ret -= self.cumsum[y1 - 1 + self.h_offset][x1 - 1 + self.w_offset]
        return ret

def rotate(field):
    h = len(field)
    w = len(field[0])
    h, w = w, h
    new_field = []
    for col in zip(*field):
        new_field.append(list(reversed(col)))
    return new_field

if __name__ == "__main__":
    n, m = [int(item) for item in input().split()]
    field = [[0] * m for _ in range(n)]
    for i in range(n):
        line = input().rstrip()
        for j in range(m):
            if line[j] == "#":
                field[i][j] = 1

    ans = 0
    for i in range(4):
        n = len(field)
        m = len(field[0])
        cs = CumulativeSum2D(field)
        cs.calc_diagonal_cumsum()
        lu_to_rd = [[] for _ in range(n + m - 1)]
        for i in range(m):
            x = i; y = 0
            delta = 0
            while x + delta < m and y + delta < n: 
                if field[y + delta][x + delta] == 1:
                    lu_to_rd[i].append((x + delta, y + delta))
                delta += 1
        for i in range(1, n):
            x = 0; y = i
            delta = 0
            while x + delta < m and y + delta < n:
                if field[y + delta][x + delta] == 1:
                    lu_to_rd[i + m - 1].append((x + delta, y + delta))
                delta += 1
        for line in lu_to_rd:
            length = len(line)
            if length <= 1:
                continue
            for i in range(length):
                for j in range(i+1, length):
                    x1, y1 = line[i]
                    x2, y2 = line[j]
                    d = abs(x1 - x2)
                    ans += cs.get_diagonal_sum(x1 + d + 1, y1 - d + 1, x2 + d, y2 - d)
        field = rotate(field)[:]
    print(ans)