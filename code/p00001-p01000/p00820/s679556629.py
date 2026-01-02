def initSquaresArray():
    arr = []
    n = 1
    while True:
        if n * n >= 32768:
            break
        arr.append(n * n)
        n += 1
    return arr

def get2Squares(num):
    global squares
    global memo2

    if num in memo2:
        return memo2[num]

    squareSums = set()
    for square in squares:
        if square >= num:
            break
        if num - square in squares:
            squareSums.add( (min(square, num - square), max(square, num - square)) )
    
    memo2[num] = squareSums
    return memo2[num]

def get3Squares(num):
    global squares
    global memo3

    if num in memo3:
        return memo3[num]

    squareSums = set()
    for square in squares:
        if square >= num:
            break
        other = get2Squares(num - square)
        for o in other:
            a = square
            b = o[0]
            c = o[1]
            tpl = tuple(sorted([ a, b, c ]))
            squareSums.add(tpl)

    memo3[num] = squareSums
    return memo3[num]

def get4Squares(num):
    global squares
    global memo4

    if num in memo4:
        return memo4[num]

    squareSums = set()
    for square in squares:
        if square >= num:
            break
        other = get3Squares(num - square)
        for o in other:
            a = square
            b = o[0]
            c = o[1]
            d = o[2]
            tpl = tuple(sorted([ a, b, c, d ]))
            squareSums.add(tpl)

    memo4[num] = squareSums
    return memo4[num]

if __name__ == '__main__':
    memo2 = {}
    memo3 = {}
    memo4 = {}
    squares = initSquaresArray()
    
    while True:
        num = int(input())
        if num == 0:
            break

        s2 = get2Squares(num)
        s3 = get3Squares(num)
        s4 = get4Squares(num)

        count = 1 if num in squares else 0
        count += len(s2)
        count += len(s3)
        count += len(s4)

        print(count)
