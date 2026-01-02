def itp_replace(stri,a,b,c):
    a = int(a)
    b = int(b)
    return stri[:a] + c + stri[b+1:]

def itp_reverse(stri,a,b):
    a = int(a)
    b = int(b)
    return stri[:a] + stri[a:b+1][::-1]+stri[b+1:]

def itp_print(stri,a,b):
    a = int(a)
    b = int(b)
    print(stri[a:b+1])

test_str = input()
test_num = int(input())
order = []
for a in range(test_num):
    temp = input().split()
    order.append(temp)

for a in order:
    if a[0] == 'replace':
        test_str = itp_replace(test_str,a[1],a[2],a[3])
    if a[0] == 'reverse':
        test_str = itp_reverse(test_str,a[1],a[2])
    if a[0] == 'print':
        itp_print(test_str,a[1],a[2])

