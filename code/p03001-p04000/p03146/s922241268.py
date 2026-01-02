import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    s=ii()
    X = [s]
    seen = set([s])
    for i in range(10**6+10):
        x = X[-1]
        if x % 2 == 0:
            y = x//2
        else:
            y = 3*x+1
        
        X.append(y)
        if y in seen:
            print(i+2)
            # print(X)
            exit()

        seen.add(y)
    
    assert False




        





if __name__ == "__main__":
    main()