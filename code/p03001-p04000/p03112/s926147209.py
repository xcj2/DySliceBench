def solve(a, b, q, al, bl, ql):
    sql = sorted(ql)
    adic = search(al, q, sql)
    bdic = search(bl, q, sql)
    qstep(adic, bdic, ql)


limit_begin = -1
limit_end = 10 ** 10 + 1
def search(tl, q, sql):
    z = list(zip([limit_begin] + tl, tl + [limit_end]))
    zi = 0
    dic = {}
    for e in sql:
        while(True):
            begin, end = z[zi]
            if (begin <= e) and (e <= end):
                dic[e] = (begin, end)
                break
            else:
                zi += 1
                if zi == (q + 1):
                    raise "system error"

    return dic

def qstep(adic, bdic, ql):
    
    for e in ql:
        asmall, abig = adic[e]
        bsmall, bbig = bdic[e]
        
        answer = 2 * (10 ** 10)
    
        # small , small
        if (asmall != limit_begin) and (bsmall != limit_begin):
            t = min(asmall,bsmall)
            v = e - t
            if v < answer:
                answer = v

        # big , big
        if (abig != limit_end) and (bbig != limit_end):
            t = max(abig,bbig)
            v = t - e
            if v < answer:
                answer = v

        # small , big
        if( asmall != limit_begin) and (bbig != limit_end):
            v = (bbig - asmall) + min(bbig - e, e - asmall)
            if v < answer:
                answer = v

        # big , small
        if( abig != limit_end) and (bsmall != limit_begin):
            v = (abig - bsmall) + min(abig - e, e - bsmall)
            if v < answer:
                answer = v

        print(answer)

        
a, b, q = map(int,input().split())

al = []
for i in range(a):
    al.append(int(input()))
bl = []
for i in range(b):
    bl.append(int(input()))
ql = []
for i in range(q):
    ql.append(int(input()))

solve(a, b, q, sorted(al), sorted(bl), ql)
