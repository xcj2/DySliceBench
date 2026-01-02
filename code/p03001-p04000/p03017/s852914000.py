import sys

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(list(sys.stdin.readline())[:-1])

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def main():
    N,A,B,C,D = LI()
    s = S()

    for i in range(B-1,D-1):
        if s[i] == "#" and s[i+1] == "#":
            return "No"

    if C<D:
        for i in range(A-1,C-1):
            if s[i] == "#" and s[i+1] == "#":
                return "No"
        return "Yes"

    flag = False
    for i in range(B-2,D-1):
        if s[i] == "." and s[i+1] == "." and s[i+2] == ".":
            flag = True
    if flag:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(main())
