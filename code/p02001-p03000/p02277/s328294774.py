def partition(a, p, r):
    x = a[r]["value"]
    i = p - 1
    for j in range(p, r):
        if a[j]["value"] <= x:
            i += 1
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    tmp = a[i+1]
    a[i+1] = a[r]
    a[r] = tmp
    return i + 1


def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


def print_a(a):
    for x in a:
        print(x["design"], x["value"])


n = int(input())
a = []
for _ in range(n):
    s = input().split()
    a.append({"design": s[0], "value": int(s[1])})
b = a.copy()

quick_sort(a, 0, n - 1)

for i in range(n - 1):
    if a[i]["value"] == a[i+1]["value"]:
        if b.index(a[i]) > b.index(a[i + 1]):
            print("Not stable")
            break
else:
    print("Stable")

print_a(a)
