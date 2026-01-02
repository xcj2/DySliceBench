from sys import stdin, stdout

int_in = lambda: int(stdin.readline())
arr_in = lambda: [int(x) for x in stdin.readline().split()]
mat_in = lambda rows: [arr_in() for _ in range(rows)]
str_in = lambda: stdin.readline().strip()
out = lambda o: stdout.write("{}\n".format(o))
arr_out = lambda o: out(" ".join(map(str, o)))
bool_out = lambda o: out("YES" if o else "NO")
tests = lambda: range(1, int_in() + 1)
case_out = lambda i, o: out("Case #{}: {}".format(i, o))


def count_black(subset, c):
    black = total_black
    for i in range(len(c)):
        if i in subset:
            for item in c[i]:
                if '#' == item:
                    black -= 1

    for i in range(len(c[0])):
        if len(c) + i in subset:
            for j in range(len(c)):
                if j not in subset:
                    if '#' == c[j][i]:
                        black -= 1
    return black


def candidates(subset, k, c):
    start_at = 0 if len(subset) == 0 else subset[-1] + 1
    go_to = len(c) + len(c[0])
    for i in range(start_at, go_to):
        yield subset + [i]


solutions = 0
def backtrack(subset, k, c):
    curr = count_black(subset, c)
    if curr < k:
        return
    if curr == k:
        global solutions
        solutions += 1
    for cand in candidates(subset, k, c):
        backtrack(cand, k, c)


def solve(h, w, k, c):
    backtrack([], k, c)
    return solutions


total_black = 0
if __name__ == "__main__":
    h, w, k = arr_in()
    c = []
    for _ in range(h):
        c.append(str_in())
        total_black += c[-1].count("#")
    out(solve(h, w, k, c))