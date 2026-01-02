def preorder(i, A):
    if i == -1:
        return ""
    n = A[i]
    l = n[1]
    ls = preorder(l, A)
    r = n[2]
    rs = preorder(r, A)
    ans = " {}".format(i)
    if ls != "":
        ans += ls
    if rs != "":
        ans += rs

    return ans

def inorder(i, A):
    if i == -1:
        return ""
    n = A[i]
    l = n[1]
    ls = inorder(l, A)
    r = n[2]
    rs = inorder(r, A)
    ans = " {}".format(i)
    if ls != "":
        ans = ls + ans
    if rs != "":
        ans += rs

    return ans

def postorder(i, A):
    if i == -1:
        return ""
    n = A[i]
    l = n[1]
    ls = postorder(l, A)
    r = n[2]
    rs = postorder(r, A)
    ans = ""
    if ls != "":
        ans = ls
    if rs != "":
        ans += rs
    ans += " {}".format(i)

    return ans

n = int(input())
root = set([x for x in range(n)])

T = [None] * n
for x in range(n):
    N = list(map(int, input().split()))
    T[N[0]] = N
    root -= set(N[1:])

r = root.pop()
print("Preorder")
print(preorder(r, T[:]))

print("Inorder")
print(inorder(r, T[:]))

print("Postorder")
print(postorder(r, T[:]))