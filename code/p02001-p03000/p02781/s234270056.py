#input
N = int(input())
K = int(input())

#output
def K_is_one(n):
    p = len(str(n))
    q = int(str(n)[0])
    return q + 9*(p-1)

def K_is_two(n):
    p = len(str(n))
    q = int(str(n)[0])
    if p == 1:
        return 0
    elif p == 2:
        return n - K_is_one(n)
    else:
        r = int(str(n)[1:])
        temp = 0
        for i in range(1, p-1):
            temp += 9*K_is_one(int("9"*i))
        temp += (q-1) * K_is_one(int("9"*(p-1))) + K_is_one(r)
        return temp

def K_is_three(n):
    p = len(str(n))
    q = int(str(n)[0])
    if p == 1:
        return 0
    elif p == 2:
        return 0
    else:
        r = int(str(n)[1:])
        temp = 0
        for i in range(1, p-1):
            temp += 9*K_is_two(int("9"*i))
        temp += (q-1) * K_is_two(int("9"*(p-1))) + K_is_two(r)
        return temp

if K == 1:
    print(K_is_one(N))
elif K == 2:
    print(K_is_two(N))
else:
    print(K_is_three(N))