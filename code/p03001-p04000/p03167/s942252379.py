import fileinput

def find_path_count(n, m, wall_set):
    modulo = 10**9 + 7
    path_table = []
    def get_path_count(x, y):
        if x < 0 or y < 0 or (x, y) in wall_set:
            return 0
        return path_table[x][y]

    for x in range(n):
        path_table.append([0] * m)
        for y in range(m):
            if x == 0 and y == 0:
                path_table[x][y] = 1
            else:
                path_table[x][y] = (get_path_count(x - 1, y) + get_path_count(x, y - 1)) % modulo

    return path_table[n - 1][m - 1]

def parse_vall_set(map_strings):
    wall_set = set()
    for x, s in enumerate(map_strings):
        for y, ch in enumerate(s):
            if ch == "#":
                wall_set.add((x, y))
    return wall_set


inp = fileinput.FileInput()
n, m = inp.readline().split(" ")
n, m = int(n), int(m)
map_strings = []
for _ in range(n):
    map_strings.append(inp.readline())

print(find_path_count(n, m, parse_vall_set(map_strings)))