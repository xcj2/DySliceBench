# input
n = int(input())
bs_input = tuple(int(i) for i in input().split())


# imposibility check
# any integer's index > i
def valid(list_):
    return all(i >= l - 1 for i, l in enumerate(list_))


def can_remove(list_, i):
    # index and number doesn't match
    if list_[i - 1] != i:
        return False

    # doesn't affect validity by removing
    if not valid(list_[:(i - 1)] + list_[i:]):
        return False

    return True


def remove(list_, i):
    return list_[:(i - 1)] + list_[i:]

reconstruct = []

bs = list(bs_input)
for i in range(n):
    if not valid(bs):
        reconstruct = []
        break
    for j in range(n - i):
        if can_remove(bs, bs[j]):
            reconstruct.insert(0, bs[j])
            bs = remove(bs, bs[j])
            break


if reconstruct == [] or len(reconstruct) != n:
    print(-1)
else:
    print('\n'.join(str(i) for i in reconstruct))
