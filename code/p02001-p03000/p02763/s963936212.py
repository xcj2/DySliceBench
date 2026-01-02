n = int(input())
s = input()
q = int(input())

queris = []
for _ in range(q):
    t, a, b = input().split()
    queris.append((t, a, b))


size = 1
while size < n:
    size *= 2

seg = [0] * (2 * size - 1)

def alph2bit(alph):
    return 1 << (ord(alph) - ord('a'))

def update(i, x, segment_tree):
    i += size - 1
    segment_tree[i] = alph2bit(x)
    while i > 0:
        i = (i - 1) // 2 # 親を更新していく。
        segment_tree[i] = segment_tree[i * 2 + 1] | segment_tree[i * 2 + 2]

def query(s, t, k, l, r, segment_tree):
    if r <= s or t <= l: # 区間が全くかぶらない場合
        return 0
    if s <= l and r <= t: # 求められた区間が、l, rを完全に含んでいる。
        return segment_tree[k]
    else:
        ask_left = query(s, t, k * 2 + 1, l, (l + r) // 2, segment_tree)
        ask_right = query(s, t, k * 2 + 2, (l + r) // 2, r, segment_tree)
        return ask_left | ask_right

for i in range(n):
    update(i, s[i], seg)

for t, a, b in queris:
    if t == '1':
        update(int(a) - 1, b, seg)
    else:
        result = query(int(a) - 1, int(b), 0, 0, size, seg)
        print(bin(result).count('1'))
