


def solve1():
    import re

    s = input()
    pattern = re.compile("(A?KIHA?BA?RA?)")

    ret = pattern.findall(s)


    #print(ret)
    if ret is not None and len(ret) ==  1 and len(ret[0]) == len(s):
        ans = "YES"
    else:
        ans = "NO"

    print(ans)


def solve2():
    s = input()

    base = "AKIHABARA"
    candidates = set()

    def rec(str_, index):
        fpos = str_.find('A',index)

        if fpos == -1:
            return 

        t = str_[:fpos] + str_[fpos+1:]

        candidates.add(str_)
        candidates.add( t )
        rec(str_, fpos+1)
        rec(t , fpos+1)

    rec(base,0)

#    print(len(candidates),candidates)
    
    ans = "YES" if s in candidates else "NO"
    print(ans)

solve2()