
def parentNode(k):
    return k // 2


def leftNode(k):
    return 2 * k


def rightNode(k):
    return 2 * k + 1

banyak = int(input())
elems = [0] + [int(x) for x in input().split()]
# for k in range(1, banyak + 1):
#      print(k,parentNode(k),leftNode(k),rightNode(k))
for k in range(1, banyak+1):
    print("node {}: ".format(k), end="")
    print("key = {}, ".format(elems[k]), end="")
    if parentNode(k) >= 1:
        print("parent key = {}, ".format(
            elems[parentNode(k)]), end="")
    if leftNode(k) <= banyak:
        print("left key = {}, ".format(
            elems[leftNode(k)]), end="")
    if rightNode(k) <= banyak:
        print("right key = {}, ".format(
            elems[rightNode(k)]), end="")
    print()




