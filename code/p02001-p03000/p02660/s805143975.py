def factorization(n):
    if(n == 1):
        return []
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def solve(N):
    ans = 0
    arr_list = factorization(N)
    for arr in arr_list:
        prime = arr[0]
        times = arr[1]
        count = 1
        while True:
            times -= count
            if(times < 0):
                break
            ans += 1
            count += 1
    return ans

#print(solve(24))
#print(solve(1))
#print(solve(64))
#print(solve(1000000007))
#print(solve(997764507000))

def main():
    N = int(input())
    print(solve(N))

main()