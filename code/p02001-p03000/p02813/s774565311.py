n = int(input())
p = [int(v) for v in input().split()]
q = [int(v) for v in input().split()]

def index_of(array, v):
    for i in range(len(array)):
        if v == array[i]:
            return i
    return -1

def perm(v):
    p = 1
    for i in range(2, v+1):
        p *= i
    return p

memo = [1] * (n+1)
for i in range(1, n+1):
    memo[i] = perm(i)
    #print("P!: ", i, memo[i])

def to_n(array):

    m = 0
    sa = sorted(array)
    while len(array) > 0:
        v = array.pop(0)
        index = index_of(sa, v)
        k = len(array)
        #print("v: ",v, ", index: ", index, ", memo: ", memo[k], index * memo[k])
        m += index * memo[k]

        if k == 0:
            break
        sa = sorted(array)

    return m

a = to_n(p)
#print("a", a)

b = to_n(q)
#print("b", b)
print(abs(a - b))