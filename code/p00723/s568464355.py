def main_a():
    y, m, d = map(int, input().split())
    a = (y - 1) // 3
    b = (y - 1) % 3
    c = a * 590 + 195 * b 
    if y % 3:
        a = (m - 1) // 2
        b = (m - 1) % 2
        c += a * 39 + b * 20
    else:
        c += (m - 1) * 20
    c += d - 1
    print(196470 - c)
def a():
    n = int(input())
    for i in range(n):
        main_a()

def main_b():
    s = input()
    ans = []
    for i in range(1,len(s)):
        ans.append(s[:i] + s[i:])
        ans.append(s[i-1::-1] + s[i:])
        ans.append(s[i-1::-1] + s[len(s):i-1:-1])
        ans.append(s[:i] + s[len(s):i - 1:-1])
        ans.append(s[i:] + s[:i])
        ans.append(s[i:] + s[i - 1::-1])
        ans.append(s[len(s):i - 1:-1] + s[i - 1::-1])
        ans.append(s[len(s):i - 1:-1] + s[:i])
    print(len(set(ans)))

def b():
    n = int(input())
    for i in range(n):
        main_b()

b()
