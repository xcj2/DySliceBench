AB, BC, AC = [int(_) for _ in input().split(" ")]

M = [[0, AB, AC],
     [AB, 0, BC],
     [AC, BC, 0]]

def A(l):
    t = [0] * l
    def Sub(targetList, n):
        if 1:
            if len(targetList) == 1:
                t[n] = targetList[0]
                yield t
                t[n] = 0
            for i in range(len(targetList)):
                p = targetList[:i] + targetList[i+1:]
                t[n] = targetList[i]
                for j in Sub(p, n+1):
                    yield j
        else:
            pass
    
    for i in (Sub(tuple(range(l)), 0)):
        yield i

def Calc(list):
    _sum = 0
    for index in range(1, len(list)):
        _from = list[index-1]
        _to = list[index]
        _sum += M[_from][_to]
    return _sum

_min = Calc([0,1,2])
for i in A(3):
    _sum = Calc(i)
    if _min > _sum:
        _min = _sum
print (_min)
        