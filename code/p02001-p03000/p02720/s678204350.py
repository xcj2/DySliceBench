import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    K=ii()
    L=list(range(10))

    if K <= 9:
        print(K)
        exit()
    
    # print(L)
    head_i = 1
    while len(L) < K+10:
        assert head_i < len(L)
        head = L[head_i]
        head_tail = head % 10
        for x in [head_tail-1,head_tail,head_tail+1]:
            if x < 0 or x >= 10: continue
            
            # print(head_i,head,head_tail)
            # assert not head * 10 + x in L
            L.append(head * 10 + x)
        
        head_i += 1

    # print(L)
    print(L[K])

    


if __name__ == "__main__":
    main()