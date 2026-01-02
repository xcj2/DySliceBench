n, k = map(int, input().split())


def simple(l):
    if not l:
        return "P"
    mid = simple(l - 1)
    return "B{}P{}B".format(mid, mid)


def length(l):
    return -2 + (1 - 2**(l + 2)) // (1 - 2)


def plen(l):
    return (1 - 2**(l + 1)) // (1 - 2)


def check(x, left, center, right, result):
    if x < center:
        if x == left:
            pos = -2
        else:
            return -1
    elif x > center:
        if x == right:
            pos = 2
        else:
            return 1
    else:
        pos = 0
    if pos in [-2, 0, 2]:
        if pos == -2:
            # print("end left")
            pass
        elif pos == 2:
            # print("end right")
            result += plen(depth + 1)
        else:
            # print("end center", plen(depth), depth)
            result += plen(depth) + 1
        print(result)
        # print(s[:k + 1].count("P"))
        exit()
k -= 1
# s = simple(n)
# print(s[:k], s[k], s[k + 1:])
# print(" - - - - - ", length(1))

left = 0
right = length(n)
center = (left + right) // 2
result = 0
depth = n - 1
# tmp = s
for i in range(50):
    # print(left, center, right, "depth", depth)
    # print(s[:center], s[center], s[center + 1:])
    # tmp = s[left : right + 1]
    # if len(tmp) != 3:
    #     print(tmp[0], tmp[1:len(tmp) // 2], tmp[len(tmp) // 2], tmp[len(tmp) // 2 + 1:-1], tmp[-1])
    # else:
    #     print("P P P")

    pos = check(k, left, center, right, result)
    if pos == -1:
        if depth == 0:
            print(result + 1)
            exit()
        left += 1
        right = center - 1
        center = (left + right) // 2
        # print("left")
    else:
        if depth == 0:
            print(result + 3)
            exit()
        right -= 1
        left = center + 1
        center = (left + right) // 2
        result += plen(depth) + 1
    #     print("right", result, plen(depth) + 1)
    # print()
    depth -= 1
