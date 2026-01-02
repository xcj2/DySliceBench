#date: 2020-03-15 21:24
import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    s = ns()
    for i, si in enumerate(s):
        if i % 2 == 0:
            if si in ("R", "U", "D"):
                continue
            else:
                print("No")
                quit()
        else:
            if si in ("L", "U", "D"):
                continue
            else:
                print("No")
                quit()
    print("Yes")

if __name__ == "__main__":
    main()