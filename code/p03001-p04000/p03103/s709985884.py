N,M = map(int,input().split())
sets = []
for _ in range(N):
    sets.append(list(map(int,input().split())))
    
def mergesort(sets):
    if len(sets) == 1:
        return [sets[0]]
    else:
        leng = len(sets)
        sets1 = mergesort(sets[:leng//2])
        sets2 = mergesort(sets[leng//2:])
        return merge(sets1,sets2)

def merge(set1,set2):
    i=0
    j=0
    result = []
    for _ in range(len(set1)+len(set2)):
        if i<len(set1) and j<len(set2):
            if set1[i][0] >= set2[j][0]:
                result.append(set2[j])
                j += 1
            elif set2[j][0] > set1[i][0]:
                result.append(set1[i])
                i += 1
        elif i == len(set1):
            result.append(set2[j])
            j += 1
        elif j == len(set2):
            result.append(set1[i])
            i += 1
    return result

def minimummoney(m,sets):
    sets = mergesort(sets)
    rest = m
    cost = 0
    for i in range(len(sets)):
        if rest > sets[i][1]:
            cost += sets[i][0]*sets[i][1]
            rest -= sets[i][1]
            continue
        if 0 < rest and rest <= sets[i][1]:
            cost += rest * sets[i][0]
        break
    return cost

print(minimummoney(M,sets))