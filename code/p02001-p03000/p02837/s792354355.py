def hou2(tarrs, s, N):
    def checkTestimony(s, t):
        scopy = s[:]
        for i in range(len(s)):
            if s[i] != t[i] and s[i] != 0 and t[i] != 0:
                return None
            if t[i]:
                scopy[i] = t[i]
        return scopy
 
    def search(pos, N, s, acc):
        if pos < N:
            check_tp = checkTestimony(s, tarrs[pos])
            if s[pos] == 1:
                s[pos] = -1
                if check_tp:
                    check_tp[pos] = 1
                    return search(pos + 1, N, check_tp, acc + 1)
                else:
                    return 0
            if check_tp and s[pos] == 0:
                s[pos] = -1
                check_tp[pos] = 1
                return max(search(pos + 1, N, check_tp, acc + 1), search(pos + 1, N, s, acc))
            else: # testimony unacceptable, assuming unkind
                s[pos] = -1
                return search(pos + 1, N, s, acc)
        else:
            return acc
 
    return search(0, N, s, 0)
    
 
if __name__ == "__main__":
    import sys
    in_arr = []
    for line in sys.stdin:
        in_arr.append([int(_) for _ in line.strip().split()])
    N = in_arr[0][0]
    i = 1
    tarrs = []
    s = [0] * N
    while i < len(in_arr):
        tnum = in_arr[i][0]
        tarr = [0] * N
        for j in range(tnum):
            x, y = in_arr[1 + j + i]
            tarr[x - 1] = 1 if y else -1 # -1 claimed unkind, 1 claimed honest
        if tarr[len(tarrs)] == -1: # claimed self to be unkind
            s[len(tarrs)] = -1
        tarrs.append(tarr)
        i += tnum + 1
    print(hou2(tarrs, s, N))
