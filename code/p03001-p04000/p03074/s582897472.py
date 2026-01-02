def burst(S):
    S += "_" #dummyを追加
    st,sp,ep = S[0],0,0
    S0,S1 = [],[]
    for i in range(1,len(S)):
        if st == S[i]:
            ep += 1
        else:
            if st == "0":
                S0.append((sp,ep))
            else:
                S1.append((sp,ep))
            st,sp,ep = S[i],i,i

    return [S0,S1]

def connect(S0,S1,K,len_S):
    if len(S0) == 0 or len(S1) == 0:
        return len_S
    else:
        if S1[0][0] != 0:
            S1 = [(0,0)] + S1
        if S1[len(S1)-1][1] != len_S-1:
            S1.append((len_S-1,len_S-1))
        if len(S1)-1 <= K:
            return len_S
        else:
            output = 0
            for i in range(len(S1)-K):
                output = max(output,S1[i+K][1]-S1[i][0]+1)
            return output

def main():
    N,K = map(int,input().split())
    S = input()

    T = burst(S)
    S0,S1 = T[0],T[1]
    print(connect(S0,S1,K,N))

if __name__ == "__main__":
    main()
