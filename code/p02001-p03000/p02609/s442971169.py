import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    X=input()

    x=int(X,2)
    pop_X=bin(x).count("1")

    pm1 = x % (pop_X-1) if pop_X-1 else 0
    pp1 = x % (pop_X+1)
    
    for i in range(N):
        sign = 1
        pop_Xi = pop_X
        if X[i] == "1": 
            sign *= -1
            pop_Xi -= 1
            _x = pm1
        else:
            pop_Xi += 1
            _x = pp1
        
        if pop_Xi == 0:
            print(0)
            continue
        
        
        two = pow(2,N-1-i,pop_Xi)
        X_i = _x + sign * two
        X_i %= pop_Xi
        count = 1
        while X_i:
            pop_Xi = bin(X_i).count("1")
            X_i = X_i % pop_Xi
            count += 1

        print(count)



if __name__ == "__main__":
    main()