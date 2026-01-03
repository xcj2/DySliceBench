import sys
def main():
    input = sys.stdin.readline
    s = input().rstrip()
    K = int(input())

    def c(x): return ord(x) - ord('a')
    def d(x): return chr(x + ord('a'))
    ans = []
    i = 0
    while i < (len(s) - 1):
        to_a = (26 - c(s[i])) % 26
        if to_a <= K:
            ans.append('a')
            K -= to_a
        else:
            ans.append(s[i])
        i += 1
    if K > 0:
        ans.append(d((c(s[-1]) + K) % 26))
    else:
        ans.append(s[i])
    print(''.join(ans))

if __name__ == '__main__':
    main()