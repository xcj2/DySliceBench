results = {"01234567": 0}


def main():
    while True:
        try:
            tmp = input().replace(' ', '')
            print(results[tmp])
        except EOFError:
            break


def swap(field, a, b):
    tmp = list(field)
    tmp[b], tmp[a] = tmp[a], tmp[b]
    return "".join(tmp)


def convert_matrix_index(index):
    return index % 4, int(index / 4)


def convert_array_index(x, y):
    return x + y * 4


def bfs(results):
    q = [["01234567", 0]]

    while len(q) is not 0:
        field, res = q.pop(0)
        x, y = convert_matrix_index(field.find('0'))
        for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 2:
                continue

            next_field = swap(field, convert_array_index(x, y), convert_array_index(nx, ny))
            if next_field not in results:
                results[next_field] = res + 1
                q.append([next_field, res + 1])

    return results


if __name__ == '__main__':
    results = bfs(results)
    main()