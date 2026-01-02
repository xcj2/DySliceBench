import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    n = II()
    aa = MII()
    bb = MII()
    dn = sum(bb) - sum(aa)
    if dn < 0:
        print('No')
        return None
    cnta = cntb = 0
    for a,b in zip(aa,bb):
        if a>b: cntb += a-b
        else: cnta += (b-a+1)//2
    if cnta <= dn and cntb <= dn:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()