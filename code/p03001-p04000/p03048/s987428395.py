import collections

def useOne(a, b, c, n):
    count = 0
    if n%a == 0: count += 1
    if n%b == 0: count += 1
    if n%c == 0: count += 1
    return count

def useTwo(a, b, n):
    a, b = sorted([a, b])
    count = 0
    maxCountOfA = n//a
    maxCountOfB = n//b
    
    startCount = 1
    for i in range(maxCountOfA, 0, -1):
        for j in range(startCount, maxCountOfB+1):
            _sum = i*a + j*b
            if _sum == n:
                count += 1
                startCount = j+1
                break
            if _sum > n:
                startCount = j
                break
    return count

def useThree(a, b, c, n):
    a, b, c = sorted([a, b, c])
    maxCountOfA = n//a
    maxCountOfB = n//b
    maxCountOfC = n//c
    count = 0
    for i in range(1, maxCountOfA+1):
        startCountOfC = maxCountOfC
        for j in range(1, maxCountOfB+1):
            _sum = i*a + j*b
            if _sum >= n:
                maxCountOfB = j
                break
            for k in range(startCountOfC, 0, -1):
                _sum = i*a + j*b + k*c
                if _sum == n:
                    count += 1
                    startCountOfC = k-1
                    break
                if _sum < n:
                    startCountOfC = k
                    break
    return count

def answer(a, b, c, n):
    count = useOne(a, b, c, n)
    count += useTwo(a, b, n)
    count += useTwo(a, c, n)
    count += useTwo(b, c, n)
    count += useThree(a, b, c, n)
    return count
    
a, b, c, n = map(int, input().split())
print(answer(a, b, c, n))