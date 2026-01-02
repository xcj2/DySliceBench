from math import sqrt

def cal(x,y,z):
    return x**2 + y**2 + z**2 + x*y + y*z + z*x

def solve(N):
    ans = [0 for _ in range(N+1)]
    for x in range(1,int(sqrt(N))+1):
        for y in range(1,int(sqrt(N))+1):
            for z in range(1,int(sqrt(N))+1):
                tmp = cal(x,y,z)
                if tmp <= N:
                    ans[tmp] += 1
                else:
                    break

    return ans

def main():
    N = int(input())

    ans = solve(N)
    for i in range(1,N+1):
        print(ans[i])

if __name__ == "__main__":
    main()
