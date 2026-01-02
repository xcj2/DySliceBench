def solve(N,X):
    ans = []
    cnt = X.count("1")
    rem_ori = [0,0]
    for i in range(N):
        if X[i] == "1":
            if cnt != 1:
                rem_ori[0] += pow(2,N-i-1,cnt-1)
                rem_ori[0] %= (cnt-1)
            else:
                rem_ori[0] = 0
            rem_ori[1] += pow(2,N-i-1,cnt+1)
            rem_ori[1] %= (cnt+1)

    rem = [(rem_ori[0] if X[i] == "1" else rem_ori[1]) for i in range(N)]
    for i in range(N):
        if X[i] == "1":
            if cnt != 1:
                rem[i] -= pow(2,N-i-1,cnt-1)
                rem[i] %= (cnt-1)
                ans.append(cal(rem[i],1))
            else:
                ans.append(0)
        else:
            rem[i] += pow(2,N-i-1,cnt+1)
            rem[i] %= (cnt+1)
            ans.append(cal(rem[i],1))

    return ans

def cal(rem,rec):
    if rem == 0:
        return rec
    else:
        b = bin(rem)[2:]
        cnt = b.count("1")
        rem %= cnt
        return cal(rem,rec+1)

def main():
    N = int(input())
    X = input()

    ans = solve(N,X)
    for i in range(N):
        print(ans[i])

if __name__ == "__main__":
    main()
