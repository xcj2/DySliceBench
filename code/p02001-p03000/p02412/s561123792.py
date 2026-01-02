import itertools
results = []

def comb_gen(n):
    combs = []
    comb = []

    mb = 2 ** n
    for i in range(mb - 1):
        bi = bin(i + 1)[2:]
        con = "0" * (n - len(bi)) + str(bin(i + 1)[2:])
        #print(con)
        sum = 0
        for j in range(len(con)):
            if con[j] == "1" and sum < 3:
                comb.append(j + 1)
                sum += 1
        if len(comb) == 3 and comb not in combs:
            #print(comb)
            combs.append(comb)
        con = ""
        comb = []
    return combs

def combgen(n):
    nums = [i for i in range(1, n+1)]
    combs = []
    for i in itertools.combinations(nums, 3):
        combs.append(i)
    return combs

def sum_chk(combs, x):
    combs = combs
    res = 0
    for i in range(len(combs)):
        #print(combs[i])
        if sum(combs[i]) == x:
            #print(combs[i])
            res += 1
    return res

#print(comb_gen(5))


while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    combs = combgen(n)
    result = sum_chk(combs, x)
    results. append(result)

for i in range(len(results)):
    print(results[i])
