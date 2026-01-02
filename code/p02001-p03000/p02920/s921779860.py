import sys

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])


def main():
    N = I()
    S = sorted(LI(),reverse=True)

    flag = [True]*len(S)

    cur = []
    nxt = []
    cur.append(S[0])
    nxt.append(S[0])
    
    flag[0] = False

    for i in range(N):
        j = 0
        for k in range(len(S)):
            if flag[k] and S[k]<cur[j]:
                nxt.append(S[k])
                j+=1
                flag[k] = False
                if j==len(cur):
                  break
        else:
            return("No")
        nxt.sort(reverse=True)
        cur = [x for x in nxt]
    return("Yes")

if __name__ == "__main__":
    print(main())
