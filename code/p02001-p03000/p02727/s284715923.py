import sys

sys.setrecursionlimit(10 ** 6)
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]



def main():
    a=LI()
    x=a[0]
    y=a[1]
    b=a[3]
    c=a[4]
    a=a[2]
    pa=LI()
    pb=LI()
    pc=LI()
    pa.sort()
    pb.sort()
    pc.sort()
    pa.reverse()
    pb.reverse()
    pc.reverse()
    pa=pa[0:x]
    pb=pb[0:y]
    pa+=pb
    pa.sort()
    pa.reverse()
    j=len(pa)-1
    summ=0
    for i in range(0, len(pa)):
        summ+=pa[i]
    for i in range(0, len(pc)):
        if j>=0 and pc[i]<=pa[j]:
            break
        else:
            summ-=pa[j]
            summ+=pc[i]
            j-=1
    print(summ)
main()
