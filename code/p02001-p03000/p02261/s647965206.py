def selection_sort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(c[j][-1]) < int(c[minj][-1]):
                minj = j
        temp = c[i]
        c[i] = c[minj]
        c[minj] = temp
    return c


def bubble_sort(c, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(c[j][-1]) < int(c[j-1][-1]):
                temp = c[j]
                c[j] = c[j-1]
                c[j-1] = temp
    return c


def is_stable(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            print('Not stable')
            return
    print('Stable')


def main():
    n = int(input())
    nums = input().split(' ')
    bubble_nums = [i for i in nums]
    select_nums = [i for i in nums]
    bubble_nums = bubble_sort(bubble_nums, n)
    select_nums = selection_sort(select_nums, n)

    print(' '.join(bubble_nums))
    print('Stable')
    print(' '.join(select_nums))
    is_stable(bubble_nums, select_nums)


if __name__ == "__main__":
    main()

