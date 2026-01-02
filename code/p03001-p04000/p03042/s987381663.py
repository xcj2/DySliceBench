def isY(num):
    return True

def isM(num):
    if num <= 12 and num >= 1:
        return True

    return False

def isYYMM(first, second):
    return (isY(first) and isM(second))

def isMMYY(first, second):
    return (isM(first) and isY(second))

line = input()
first = int(line[:2])
second = int(line[2:])

ans = "NA"

if (not isMMYY(first, second)) and isYYMM(first, second):
    ans = "YYMM"

if isMMYY(first, second) and (not isYYMM(first, second)):
    ans = "MMYY"

if isMMYY(first, second) and isYYMM(first, second):
    ans = "AMBIGUOUS"

        
print(ans)

