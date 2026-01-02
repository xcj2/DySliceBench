M = 1046527

def charToKey(a):
    if a == "A":
        return 1
    elif a == "C":
        return 2
    elif a == "G":
        return 3
    elif a == "T":
        return 4
    else:
        return 0

def strToKey(s):
    sum = 0
    coef = 1
    for c in s:
        key = charToKey(c)
        sum += coef * key
        coef *= 5
    return sum

def hash1(key):
    return key % M

def hash2(key):
    return 1 + (key % (M - 1))

def insert(A, value):
    key = strToKey(value)
    for i in range(M):
        hash = (hash1(key) + i * hash2(key)) % M
        if A[hash] == value:
            return
        elif A[hash] is None:
            A[hash] = value
            return
    return

def find(A, value):
    key = strToKey(value)
    for i in range(M):
        hash = (hash1(key) + i * hash2(key)) % M
        if A[hash] == value:
            return True
        elif A[hash] is None:
            return False
    return False

if __name__ == "__main__":
    A = [None for i in range(M)]

    N = int(input())
    for i in range(N):
        command, value = input().split()
        if command == "insert":
            insert(A, value)
        else:
            if (find(A, value)):
                print("yes")
            else:
                print("no")

