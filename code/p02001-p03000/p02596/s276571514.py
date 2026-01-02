import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    K=ii()

    i = 1
    x = 7 % K
    if x == 0:
        print(1)
        exit()

    for i in range(10**6+10):
        x = x*10+7
        x %= K
        if x == 0:
            print(i+2)
            exit()
    
    print(-1)


    # i = 1
    # while True:
    #     x = (7**i) * K
    #     if x % 7 == 0:
    #         y = x // 7
    #         f = True
    #         for s in str(y):
    #             if s != "1":
    #                 f = False
    #                 break
            
    #         if f:
    #             print(len(str(y)))
    #             exit()
                
    #     i+=1


if __name__ == "__main__":
    main()