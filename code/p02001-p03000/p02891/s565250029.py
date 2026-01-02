
def main():
    s = input()
    k = int(input())
    print(solve(s, k))

def solve(s, k):
    ans = 0
    if len(set(s)) == 1:
        ans += replace_count(len(s)*k)
    else:
        same = 1
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                same += 1
            else:
                ans += replace_count(same) * k
                same = 1
        ans += replace_count(same) * k
        if s[0] == s[i]:
            a = 1
            b = 1
            a_idx = 0
            b_idx = -1
            while s[a_idx] == s[a_idx+1]:
                a += 1
                a_idx += 1
            while s[b_idx] == s[b_idx-1]:
                b += 1
                b_idx -= 1
            dup = (replace_count(a) + replace_count(b) - replace_count(a+b)) * (k-1)
            ans -= dup

    return ans


def replace_count(n):
    return n//2

main()


