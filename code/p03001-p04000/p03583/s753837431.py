import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        N=int(input())
        while True:
            for h in range(1,3501):
                for n in range(h,3501):
                    if 4*h*n-N*n-N*h==0:
                        continue
                    else:
                        temp=(N*h*n)/(4*h*n-N*n-N*h)
                        if temp>0 and temp.is_integer():
                            return [h,n,int(temp)]
    for i in main():
        print(i,end=' ')


resolve()