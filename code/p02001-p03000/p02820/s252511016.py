import sys
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N,K = LI()
R,S,P = LI()
T = list(input())
hand = []

def main():
    ans = 0
    for i in range(N):
        if T[i] == 's':
            if i<K or hand[i-K]!='r':
                ans += R
                hand.append('r')
            else:
                hand.append('x')
        if T[i] == 'p':
            if i<K or hand[i-K] != 's':
                ans += S
                hand.append('s')
            else:
                hand.append('x')
        if T[i] == 'r':
            if i<K or hand[i-K] != 'p':
                ans += P
                hand.append('p')
            else:
                hand.append('x')
    print(ans)

if __name__ == "__main__":
    main()
