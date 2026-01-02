def out_calc(num):
    for i in range(0, num):
        print("#",end="")
    print("")


def in_calc(num, num2):
    for i in range(0, num-2):
        print("#", end="")
        for j in range(0, num2-2):
            print(".", end="")
        print("#")


def main():
    array = []
    while True:
        value = input().split()
        value = [int(x) for x in value]
        if value[0] == 0 and value[1] == 0:
            break
        else:
            array.append(value)

    for i in range(0, len(array)):
        out_calc(array[i][1])
        in_calc(array[i][0], array[i][1])
        out_calc(array[i][1])
        print("")


if __name__ == '__main__':
    main()