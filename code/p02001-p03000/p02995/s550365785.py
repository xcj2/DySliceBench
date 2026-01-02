def gcd(a, b):
    a, b = sorted([a, b], reverse=True)
    while(b != 0):
        a, b = (b, a%b)
    return a

def getMultiCount(start, end, times):
    if end < times: return 0
    s = start-(start%times)
    if s != start: s += times
    e = end-(end%times)
    if s > e: return 0
    return ((e-s)//times)+1
    
def answer(a, b, c, d):
    cCount = getMultiCount(a, b, c)
    dCount = getMultiCount(a, b, d)
    cdCount = getMultiCount(a, b, c*d//gcd(c,d))
    return (b-a+1)-(cCount + dCount - cdCount)

a, b, c, d = map(int, input().split())
print(answer(a, b, c, d))