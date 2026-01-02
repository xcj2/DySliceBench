
def remove_lowest_step(flowers):
    flowers = [f-1 if f > 0 else 0 for f in flowers]
    return flowers


def count_lowest_step(flowers):
    binary_flowers = [1 if f > 0 else 0 for f in flowers]
    merge_flowers = binary_flowers[0:1]

    for b in binary_flowers[1:]:
        if merge_flowers[-1] == b:
            continue
        merge_flowers.append(b)

    return sum(merge_flowers)


def check_end(flowers):
    if sum(flowers) == 0:
        return True
    return False


def input_flowers():
    n = int(input())
    flowers = input().split()
    flowers = list(map(int, flowers))

    return n, flowers


n, flowers = input_flowers()
count = 0

while not check_end(flowers):
    count += count_lowest_step(flowers)
    flowers = remove_lowest_step(flowers)

print(count)