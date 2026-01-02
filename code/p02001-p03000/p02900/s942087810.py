def divisor(n):
    i = 1
    table = []

    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))

    return table


def common_divisor(a, b):
    table = []
    for i in a:
        if i in b:
            table.append(i)
    return table


def resolve():
    A, B = map(int, input().split())
    a_list = divisor(A)
    b_list = divisor(B)
    common_list = common_divisor(a_list, b_list) if len(a_list) < len(b_list) else common_divisor(b_list, a_list)
    common_list.sort()
    i = 1
    while i < len(common_list):
        j = i + 1
        while j < len(common_list):
            if common_list[j] % common_list[i] == 0:
                del common_list[j]
            else:
                j += 1
        i += 1

    print(len(common_list))
    
resolve()
