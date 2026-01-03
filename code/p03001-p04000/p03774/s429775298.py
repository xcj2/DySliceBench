

def read_input():
    n, m = map(int, input().split())

    students = []
    for i in range(n):
        a, b = map(int, input().split())
        students.append((a, b))

    checkpoints = []
    for j in range(m):
        c, d = map(int, input().split())
        checkpoints.append((c, d))

    return n, m, students, checkpoints


def search_nearest_checkpoint(st, checks):
    def manhattan_dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    mindist = float('inf')
    minid = None
    for i, check in enumerate(checks):
        mdist = manhattan_dist(st, check)
        if mdist < mindist:
            mindist = mdist
            minid = i + 1

    return minid

def submit():
    n, m, students, checkpoints = read_input()


    for student in students:
        print(search_nearest_checkpoint(student, checkpoints))


if __name__ == '__main__':
    submit()
