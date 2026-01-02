from sys import stdin


def fetch_one_line():
    return stdin.readline().rstrip()


def fetch_int_input():
    return [int(s) for s in fetch_one_line().split()]


def fetch_inputs(times):
    return [fetch_one_line() for _ in range(times)]


def fetch_int_inputs(times):
    return [fetch_int_input() for _ in range(times)]


N, M = fetch_int_input()
gate_len = fetch_int_inputs(M)
# range_card = [[False] * N for _ in range(M)]
l, r = 0, N
for gl in gate_len:
    if l < gl[0]:
        l = gl[0]
    if r > gl[1]:
        r = gl[1]

# range_card = list(zip(*range_card))
# print(sum([all(r) for r in range_card]))
result = r - l + 1
if result < 0: result = 0

print(result)
