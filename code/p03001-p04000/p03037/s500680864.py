def input_from_console():
    n, m = map(int, input().split())
    lr_list = []
    for i in range(m):
        l, r = map(int, input().split())
        lr_list.append((l,r))
    return n, m, lr_list

def solve(n, m, lr_list):
    lr_list.append((1,n))
    l_max = 0
    r_min = n
    for item in lr_list:
        l, r = item
        if l > l_max:
            l_max = l
        if r < r_min:
            r_min = r
    result = r_min - l_max + 1
    if result < 0:
        result = 0
    return result

def main():
    n, m, lr_list = input_from_console()
    print(solve(n, m, lr_list))


if __name__ == "__main__":
    main()