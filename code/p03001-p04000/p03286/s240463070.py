def sigma4jou(k):
    total = 0
    for i in range(k):
        total += 4 ** (i)
    return(total)

def pketa(N):
    k = 1
    while N - sigma4jou(k) > 0:
        k += 1
    return(2 * k - 1)

def mketa(N):
    k = 1
    while N + 2 * sigma4jou(k) < 0:
        k += 1
    return(2 * k)

def getResult(N):
    result = ""
    if N == 0:
        result += "0"
    elif N > 0:
        k = pketa(N)
        for i in range(k, 0, -2):
            j = int((i+1)/2)
            if abs((sigma4jou(j) - N) // (2 ** (i-1))) % 2 == 0:
                result += "1"
            else:
                result += "0"
            if i > 1:
                if abs(((sigma4jou(j) - N)) // (2 ** (i-2))) % 2 == 1:
                    result += "1"
                else:
                    result += "0"
    elif N < 0:
        k = mketa(N)
        for i in range(k, 0, -2):
            j = int(i/2)
            if abs((N + 2 * sigma4jou(j)) // (2 ** (i-1))) % 2 == 0:
                result += "1"
            else:
                result += "0"
            if i > 1:
                if abs(((N + 2 * sigma4jou(j))) // (2 ** (i-2))) % 2 == 1:
                    result += "1"
                else:
                    result += "0"
    return(result)

N = int(input())
print(getResult(N))