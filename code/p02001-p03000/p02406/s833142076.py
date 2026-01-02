# get line input split by space
def getLnInput():
    return input().split()


# ceil(a / b) for a > b
def ceilDivision(a, b):
    return (a - 1) // b + 1


def call(n):
    i = 1
    while i < n:
        i += 1
        x = i
        if not x % 3:
            print(" " + str(i), end="")
        else:
            while True:
                if x % 10 == 3:
                    print(" " + str(i), end="")
                    break
                x //= 10
                if not x:
                    break
    print()


def main():
    n = int(getLnInput()[0])
    call(n)
    return


main()