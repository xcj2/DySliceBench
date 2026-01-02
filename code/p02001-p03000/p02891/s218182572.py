def count(S):
    ans = 0
    i = 1
    while i < len(S):
        if S[i-1] == S[i]:
            i += 1
            ans += 1
        i += 1
    return ans

def first_last_count(S):
    first = 1
    c = S[0]
    for i in range(1, len(S)):
        if S[i] == c:
            first += 1
        else:
            break

    last = 1
    c = S[0]
    for i in range(len(S)-2, 0, -1):
        if S[i] == c:
            last += 1
        else:
            break

    return (first//2) + (last//2) - ((first+last)//2)

def is_same(S):
    c = S[0]
    for i in range(1, len(S)):
        if S[i] != c:
            return False
    return True

def main():
    S = input()
    K = int(input())

    if is_same(S):
        print((len(S) * K) // 2)
        exit()

    ans = count(S)
    ans *= K
    if S[-1] == S[0]:
        ans -= first_last_count(S) * (K-1)

    print(ans)

if __name__ == '__main__':
    main()