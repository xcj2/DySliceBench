import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()

def main():
    N=ii()

    k = N
    ans = []
    a_ord = ord('a')

    def mod(n):
        return n%26 if n % 26 > 0 else 26


    while k > 0:
        # print(k%26)
        ans.append(chr(a_ord+mod(k)-1))
        if k % 26 > 0:
            k //= 26
        else:
            k -= 1
            k //= 26

    # if N % 26 == 0:
    #     print("".join(ans[::-2]))
    # else:
    print("".join(ans[::-1]))


if __name__ == "__main__":
  main()