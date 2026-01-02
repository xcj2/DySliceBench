# get line input split by space
def getLnInput():
    return input().split()


# ceil(a / b) for a > b
def ceilDivision(a, b):
    return (a - 1) // b + 1


def main():
    while True:
        H, W = list(map(int, getLnInput()))
        printFromSharp = True
        if H == 0 and W == 0:
            break
        if H != 0 or W != 0:
            for i in range(H):
                isCurrentSharp = printFromSharp
                for j in range(W):
                    print("#" if isCurrentSharp else ".", end="")
                    isCurrentSharp = not isCurrentSharp
                print()
                printFromSharp = not printFromSharp
        print()
    return


main()