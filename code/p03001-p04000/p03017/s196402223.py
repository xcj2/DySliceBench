def valid_check(n, a, b, c, d, s):
    if not two_rocks(s[b:d]):
        return 0
    # if not two_rocks()
    if c < d:
        return two_rocks(s[a:c])
    else:
        return three_spaces(s[b-1:d+2]) and two_rocks(s[a:c])


def three_spaces(s):
    for i in range(len(s)-2):
        if s[i]=='.' and s[i+1]=='.' and s[i+2]=='.':
            return 1
    return 0

# def enumerate_possibilities(b, d, s):
#     possibilities = []
#     for i in range(d-b+1):
#         if s[b+i]=='.':
#             tmp = s.copy()
#             tmp[b+i] = '#'
#             possibilities.append(tmp)
#     return possibilities


def two_rocks(s):
    for i in range(len(s)-1):
        if s[i]=='#' and s[i+1]=='#':
            return 0
    return 1

n, a, b, c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
s = list(input())


if valid_check(n, a, b, c, d, s):
    print('Yes')
else:
    print('No')
