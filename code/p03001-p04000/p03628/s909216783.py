def ri(): return int(input())
def rli(): return list(map(int, input().split()))
def rls(): return list(input())
def pli(a): return "".join(list(map(str, a)))
def plis(a): return " ".join(list(map(str, a)))

N = ri()
S1 = rls()
S2 = rls()
mode = None
mode_p = None
ans = 0
mod = 10**9 + 7

i = 0
while(i < N):
    if(S1[i] == S2[i]):
        if(mode is None):
            mode = "c"
        else:
            mode_p = mode
            mode = "c"
    else:
        i += 1
        if(mode is None):
            mode = "r"
        else:
            mode_p = mode
            mode = "r"
    
    if(mode_p is None):
        ans = 3 if mode == "c" else 6
    else:
        if(mode_p == "c"):
            ans = ans*2%mod
        elif(mode == "r"):
            ans = ans*3%mod
    i += 1

print(ans)
