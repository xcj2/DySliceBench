from copy import deepcopy

def judge_a(S,T,i,j):
    return S[i+j]==T[j]

def judge_b(S,T,i,j):
    return S[i+j]!=T[j] and S[i+j]=="?"

def ans(ans_list):
    if not ans_list:
        print("UNRESTORABLE")
    else:
        ans_list_2=[]
        for l in ans_list:
            temp=[s if s!="?" else "a" for s in l]
            ans_list_2.append("".join(temp))
        print(min(ans_list_2))

if __name__ == '__main__':
    S_dash=list(input())
    T=list(input())
    N_S=len(S_dash)
    T_N=len(T)
    ans_list=[]

    for i in range(N_S-T_N+1):
        S_2=deepcopy(S_dash)
        flag=True
        for j in range(T_N):
            if judge_a(S_2,T,i,j) or judge_b(S_2,T,i,j):
                S_2[i+j]=T[j]
            else:
                flag=False
                break
        if flag:
            ans_list.append(S_2)
    ans(ans_list)



