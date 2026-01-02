T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

a1 = T1 * A1
a2 = T2 * A2
a = a1 + a2
b1 = T1 * B1
b2 = T2 * B2
b = b1 + b2


def bis(p, ok, ng):
    mid = (ok + ng) // 2
    return (
        ok if abs(ok - ng) == 1 else
        bis(p, mid, ng) if p(mid) else
        bis(p, ok, mid)
    )


def p(k):
    x = k * a
    y = k * b
    # print(f"k: {k}, x: {x}, y: {y}")
    #print(f"k: {k}, x+: {x + a1}, y+: {y + b1}")
    if x < y:
        return x + a1 >= y + b1
    else:
        return y + b1 >= x + a1


def p2(k):
    x = k * a + a1
    y = k * b + b1
    if x < y:
        return x + a2 >= y + b2
    elif x > y:
        return y + b2 >= x + a2
    else:
        return False

if a == b:
    ans = "infinity"
else:
    # print(bis(p, -1, 10**16))
    # print(bis(p2, -1, 10**16))
    c = 1 if (a1 < b1 and a > b) or (b1 < a1 and b > a) else 0
    # k = bis(lambda k: k * a + a1 >= k * b + b1, 0, 10**16) if a < b else bis(lambda k: k * a + a1 <= k * b + b1, 0, 10**16)
    # d = if k * a + a1 == k * b + b1
    ans = bis(p, 0, 10**16) + bis(p2, 0, 10**16) + c

print(ans)

# print('-------')

# x = 0
# y = 0
# for i in range(114):
#     x += a1
#     y += b1
#     #print(x, y)
#     print(f"{i} {x < y}")
#     x += a2
#     y += b2
#     print(f"{i} {x < y}")
#     #print(x, y)


