import sys
input=sys.stdin.readline

def solve_odd(n,AB):
    AB.sort()
    median_min=AB[n//2][0]
    AB.sort(key=lambda x: x[1])
    median_max=AB[n//2][1]
    #print(median_max,median_min)
    return max(0,median_max-median_min+1)

def solve_even(n,AB):
    AB.sort()
    median_min=AB[n//2-1][0]+AB[n//2][0]
    AB.sort(key=lambda x: x[1])
    median_max=AB[n//2-1][1]+AB[n//2][1]
    #print(median_max,median_min)
    return max(0,median_max-median_min+1)

def main():
    n=int(input())
    AB=[list(map(int,input().split())) for _ in range(n)]
    if n%2==0:
        ans=solve_even(n,AB)
    else:
        ans=solve_odd(n,AB)
    print(ans)
    
if __name__=='__main__':
    main()