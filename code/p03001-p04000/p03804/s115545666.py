def main():
    #infile = open("compprog.txt", mode="r")
    #n, m = [int(x) for x in infile.readline().split()]
    n, m = [int(x) for x in input().split()]
    a = []
    b = []
    for _ in range(n):
        #a.append(infile.readline())
        a.append(input())
    for _ in range(m):
        #b.append(infile.readline())
        b.append(input())
    if solve(a, b, n, m):
        print("Yes")
    else:
        print("No")


def solve(a, b, n, m):
    for row in range(n - m + 1):
        for col in range(n - m + 1):
            if check(a, row, col, b, m):
                return True
    return False


def check(a, row, col, b, m):
    for this_row in range(row, row + m):
        for this_col in range(col, col + m):
            if a[this_row][this_col] != b[this_row - row][this_col - col]:
                return False
    return True


if __name__ == "__main__":
    main()
