import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    lunlun = [i for i in range(10)]
    def make(s,keta):
        lst = []
        end = int(s[-1])
        if end == 0:
            lst = [s+"0",s+"1"]
        elif end == 9:
            lst = [s+"8",s+"9"]
        else:
            lst = [s+str(end+i) for i in range(-1,2)]
        if keta == 1:
            for lun in lst:
                lunlun.append(int(lun))
        else:
            for lun in lst:
                make(lun,keta-1)
            
    for keta in range(1,10):
        for i in range(1,10):
            make(str(i),keta)

    k = I()
    ans = lunlun[k]
    print(ans) 
                
        

main()
