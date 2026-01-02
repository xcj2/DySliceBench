def isValidNumOfBill(x, y, z, N):
    return x + y + z == N

def isValidSumOfMoney(x, y, z, Y):
    return 10000 * x + 5000 * y + 1000 * z == Y

def outputResult(x, y, z):
    print('{x:d} {y:d} {z:d}'.format(x=x, y=y, z=z))

def outputFailure():
    print('-1 -1 -1')

def searchA(N, Y):
    # define range
    xlim = range(0, Y // 10000 + 1)
    ylim = range(0, Y // 5000 + 1)
    zlim = range(0, Y // 1000 + 1)

    for x in xlim:
        for y in ylim:
            for z in zlim:
                # print(x, y, z)
                if not isValidNumOfBill(x, y, z, N):
                    continue
                if isValidSumOfMoney(x, y, z, Y):
                    return (x, y, z)

def searchB(N, Y):
    # 最初に金額を合わせる
    calcX = lambda Y: Y // 10000
    calcY = lambda x, Y: (Y - 10000 * x) // 5000
    calcZ = lambda x, y, Y: (Y - 10000 * x - 5000 * y) // 1000
    x = calcX(Y)
    y = calcY(x, Y)
    z = calcZ(x, y, Y)

    while x >= 0:
        while y >= 0:
            # print(x, y, z)
            if sum((x, y, z)) == N:
                return (x, y, z)
            y -= 1
            z = calcZ(x, y, Y)
        x -= 1
        y = calcY(x, Y)
        z = calcZ(x, y, Y)

def main():
    # read 'N Y'
    args = input().split(" ")
    N = int(args[0])
    Y = int(args[1]) 

    # search for 10000x + 5000y + 1000z = Y
    # result = searchA(N, Y)
    result = searchB(N, Y)
    if result is not None:
        x, y, z = result
        outputResult(x, y, z)
    else:
        outputFailure()

if __name__ == '__main__':
    main()
