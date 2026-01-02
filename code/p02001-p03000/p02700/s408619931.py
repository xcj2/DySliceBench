import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))


def main():
    A,B,C,D = MI()

    while True:
        C = C-B
        if C <= 0:
            print("Yes")
            break
        A = A - D
        if A <= 0:
            print("No")
            break
    """
    if w>=s:
        print("unsafe")
    else:
        print("safe")
        """




if __name__ == "__main__":
	main()