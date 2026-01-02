def cal_single(S,N):
    output = 0
    for i in range(N):
        output += S[i].count("AB")
    return output

def cal_cont(S,N):
    a,b,ab = 0,0,0
    for i in range(N):
        if S[i][0] == "B" and S[i][-1] == "A":
            ab += 1
        elif S[i][0] == "B":
            b += 1
        elif S[i][-1] == "A":
            a += 1

    if ab == 0:
        return min(a,b)
    elif a + b == 0:
        return ab-1
    else:
        return ab + min(a,b)

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    ans = cal_single(S,N)+cal_cont(S,N)

    print(ans)

if __name__ == "__main__":
    main()
