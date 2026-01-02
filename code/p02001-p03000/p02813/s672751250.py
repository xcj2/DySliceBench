N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def order(n, list):
    total = 0
    for i in range(1, n):
        for j in range(i, n):
            if list[i-1] <= list[j]:
                list[j] -= 1
            else:
                pass

        total += (list[i-1]-1)*factorial(n-i)
    return total

def main():
    a = order(N, P)
    b = order(N, Q)
    if 0 <= a-b:
        print(a-b)
    else:
        print(-(a-b))

if __name__ == "__main__":
    main()
