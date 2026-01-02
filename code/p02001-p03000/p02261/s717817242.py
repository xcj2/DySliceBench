import sys

def bubble_sort(size, numbers):
    for i in range(size):
        sorted = True
        for j in range(size - 1, i, -1):
            if numbers[j][1] < numbers[j - 1][1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                sorted = False

        if sorted:
            break


def selection_sort(size, numbers):
    for i in range(size):
        minindex = i
        for j in range(i, size):
            if numbers[minindex][1] > numbers[j][1]:
                minindex = j
        if minindex != i:
            numbers[minindex], numbers[i] = numbers[i], numbers[minindex]


def write_result(stdout, sorted_array, original_array):
    stable = True
    for i in range(1, len(sorted_array)):
        if (sorted_array[i - 1][1] != sorted_array[i][1]):
            continue

        index_a = original_array.index(sorted_array[i - 1])
        index_b = original_array.index(sorted_array[i])

        if index_a > index_b:
            stable = False

    stdout.write(" ".join([str(x) for x in sorted_array]) + "\n")
    if stable:
        stdout.write("Stable\n")
    else:
        stdout.write("Not stable\n")


def main(stdin=None, stdout=None):
    if stdin is None:
        stdin = sys.stdin
    if stdout is None:
        stdout = sys.stdout

    size = int(stdin.readline().strip())
    _numbers = stdin.readline().strip().split(" ")

    numbers = _numbers[::]
    swap_count = bubble_sort(size, numbers)
    write_result(stdout, numbers, _numbers)

    numbers = _numbers[::]
    swap_count = selection_sort(size, numbers)
    write_result(stdout, numbers, _numbers)

main()
