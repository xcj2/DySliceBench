from collections.abc import Iterable

n = int(input())
nodes = {}
for _ in range(n):
    key, left, right = map(int, input().split())
    nodes[key] = (left, right)
keys = set(nodes.keys())
for left, right in nodes.values():
    keys -= {left, right}
root = keys.pop()


def flatten(arr):
    for a in arr:
        if isinstance(a, Iterable) and not isinstance(a, (str, bytes)):
            yield from flatten(a)
        else:
            yield a


def pre_tw(key):
    left, right = nodes[key]
    if left == -1 and right == -1:
        return [key]
    elif left == -1:
        return [key, pre_tw(right)]
    elif right == -1:
        return [key, pre_tw(left)]
    else:
        return [key, pre_tw(left), pre_tw(right)]


def in_tw(key):
    left, right = nodes[key]
    if left == -1 and right == -1:
        return [key]
    elif left == -1:
        return [key, in_tw(right)]
    elif right == -1:
        return [in_tw(left), key]
    else:
        return [in_tw(left), key, in_tw(right)]


def post_tw(key):
    left, right = nodes[key]
    if left == -1 and right == -1:
        return [key]
    elif left == -1:
        return [post_tw(right), key]
    elif right == -1:
        return [post_tw(left), key]
    else:
        return [post_tw(left), post_tw(right), key]


print("Preorder")
for a in flatten(pre_tw(root)):
    print(" {}".format(a), end="")
print()

print("Inorder")
for a in flatten(in_tw(root)):
    print(" {}".format(a), end="")
print()

print("Postorder")
for a in flatten(post_tw(root)):
    print(" {}".format(a), end="")
print()

