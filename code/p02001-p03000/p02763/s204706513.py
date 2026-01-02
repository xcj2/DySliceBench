import math

n = int(input())
s = input()
S = [ord(i) - 97 for i in s]
q = int(input())
HEIGHT = math.ceil(math.log(n) / math.log(2))
SIZE = 1 << HEIGHT

def build_tree():
    tree = [0 for _ in range(SIZE<<1)]

    for i, letter in enumerate(s):
        tree[i+SIZE] = 1<<(ord(letter)-97)

    for i in range(HEIGHT - 1, -1, -1):
        for x in range(1<<i, 2<<i):
            tree[x] = tree[x<<1] | tree[(x<<1)+1]

    return tree




def update(x, number):
    tree[x] = number
    while x > 1:
        x >>= 1
        tree[x] = tree[x << 1] | tree[(x << 1) + 1]


def query(l, r):
    total = 0
    while l < r:
        if l&1:
            total |= tree[l]
            l += 1
        l >>= 1
        if r&1:
            r -= 1
            total |= tree[r]
        r >>= 1
    return bin(total).count('1')



tree = build_tree()

for i in range(q):
    a, b, c = input().split()
    b = int(b) - 1
    if int(a) == 1:
        update(b + SIZE, S[b])
        c = 1 << (ord(c) - 97)
        S[b] = c
        update(b + SIZE, c)
    else:
        print(query(b + SIZE, int(c)+SIZE))






