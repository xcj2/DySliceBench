def pre_order(u):
    if u == -1:
        return
    print('', u, end='')
    pre_order(T[u])
    pre_order(T[u + N])

def in_order(u):
    if u == -1:
        return
    in_order(T[u])
    print('', u, end='')
    in_order(T[u + N])

def post_order(u):
    if u == -1:
        return
    post_order(T[u])
    post_order(T[u + N])
    print('', u, end='')

N = int(input())
T = [0, 0] * N
for _ in range(N):
    a, b, c = map(int, input().split())
    T[a], T[a + N] = b, c
root = (set(range(N)) - set(T)).pop()
print('Preorder')
pre_order(root)
print('\nInorder')
in_order(root)
print('\nPostorder')
post_order(root)
print()
