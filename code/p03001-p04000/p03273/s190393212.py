def b_grid_compression():
    H, W = [int(i) for i in input().split()]
    A = [list(input()) for _ in range(H)]

    def rotate_clockwise(matrix):
        return list(map(list, zip(*matrix)))[::-1]

    def rotate_counterclockwise(matrix):
        return list(map(lambda x: list(x[::-1]), zip(*matrix)))

    def remove_white_line(matrix):
        return [row for row in matrix if row.count('.') < len(row)]

    ans = rotate_counterclockwise(remove_white_line(rotate_clockwise(remove_white_line(A))))
    return '\n'.join([''.join(row) for row in ans])

print(b_grid_compression())