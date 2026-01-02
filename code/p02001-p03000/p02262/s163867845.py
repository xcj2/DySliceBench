import math


def insertion_sort(alist, step):
    size = len(alist)
    count = 0

    for i in range(step, size): 
        v = alist[i]
        j = i - step
        while j >= 0 and alist[j] > v:
            alist[j+step] = alist[j]
            j -= step
            count += 1
        alist[j+step] = v

    return (count, alist)


def shell_sort(alist, steps):   
    total_count = 0
    sorted_list = alist

    for step in steps:
        (count, sorted_list) = insertion_sort(sorted_list, step)
        total_count += count

    return (total_count, sorted_list)


def run():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))

    steps = create_steps(n)
    (cnt, nums) = shell_sort(nums, steps)

    print(len(steps))
    print(" ".join([str(s) for s in steps]))
    print(cnt)
    for n in nums:
        print(n)


def create_steps(n):
    steps = []
    k = 1
    while True:
        steps = [k] + steps
        k =  2 * k + int(math.sqrt(k)) + 1
        if k >= n:
            break

    return steps


if __name__ == '__main__':
    run()

