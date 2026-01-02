N, M = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))


def sortkey(a, b, c):
    def f(x):
        return (x[a], x[b], x[c])
    return f


def invertSum(a, b, c):
    def f(x):
        return (-x[0] if a else x[0]) + (-x[1] if b else x[1]) + (-x[2] if c else x[2])
    return f


mp = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]


mats = []
for sign in mp:
    mats.append(list(map(invertSum(*sign), mat)))

for idx, m in enumerate(mats):
    mats[idx] = sorted(m, reverse=True)


def funcSelectM(M):
    def select(seq):
        return seq[:M]
    return select


from pprint import pprint


takeMmats = list(map(funcSelectM(M), mats))
# for m in takeMmats:
#     pprint(m)
print(max(map(sum, takeMmats)))
