n = int(input())
s = input()
q = int(input())
commands = []
for _ in range(q):
    com, x, y = input().split()
    commands.append((com, int(x), y))

size = 1
while size < n:
    size *= 2

# initialize
segment_tree = [0 for _ in range(2 * size - 1)]


def alphabet2bit(string):
    return 1 << (ord(string) - ord('a'))

def update(i, x, segment_tree):
    i += size - 1
    segment_tree[i] = alphabet2bit(x)
    while i > 0:
        i = (i - 1) // 2
        left = segment_tree[i * 2 + 1]
        right = segment_tree[i * 2 + 2]
        segment_tree[i] = left | right

def getSum(s, t, k, l, r, segment_tree):
    if r <= s or t <= l:
        return 0
    if s <= l and r <= t:
        return segment_tree[k]
    else:
        ask_left = getSum(s, t, k * 2 + 1, l, (l + r) // 2, segment_tree)
        ask_right = getSum(s, t, k * 2 + 2, (l + r) // 2, r, segment_tree)
        return ask_left | ask_right

for i in range(n):
    update(i, s[i], segment_tree)

for com, x, y in commands:
    if com == '1':
        update(x - 1, y, segment_tree)
    else:
        result = getSum(x - 1, int(y), 0, 0, size, segment_tree)
        print(bin(result).count('1'))