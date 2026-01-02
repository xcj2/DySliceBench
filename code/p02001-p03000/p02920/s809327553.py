import sys

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])


def main():
    N = I()
    S = sorted(LI(),reverse=True)

    flag = [True]*len(S)

    cur = []
    cur.append(S[0])
    flag[0] = False

    for i in range(N):
        nxt = [x for x in cur]
        j = 0

        for k in range(len(S)):
            if j >= len(cur):
                break
            elif flag[k] and S[k]<cur[j]:
                nxt.append(S[k])
                j+=1
                flag[k] = False
        if len(cur) != j:
            return("No")
        cur = sorted(nxt,reverse=True)
    return("Yes")

if __name__ == "__main__":
    print(main())