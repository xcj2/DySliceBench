def hasParent(id, n, h):
    pk = (id+1)//2
    if pk >= 1 and pk <= n:
        return "parent key = {}, ".format(h[pk-1])
    else:
        return ""


def hasChildren(id, n, h):
    lk = (id+1)*2
    rk = (id+1)*2+1
    ret = ""
    if lk >= 1 and lk <= n:
        ret = "left key = {}, ".format(h[lk-1])

    if rk >= 1 and rk <= n:
        ret += "right key = {}, ".format(h[rk-1])

    return ret


def main():
    N = int(input())
    H = list(map(int, input().split()))

    for node, key in enumerate(H):
        addtext = hasParent(node, N, H)
        addtext += hasChildren(node, N, H)

        print("node {}: key = {}, {}".format(node+1, key, addtext))


if __name__ == '__main__':
    main()
