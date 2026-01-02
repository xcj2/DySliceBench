def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

def walk_on_multiplication_table(n):

    ans = 10**13
    yaku = make_divisors(n)
    yaku.sort()
    count = len(yaku)
    for i in range(int(count//2)):
        ans = min(ans, (yaku[i]+yaku[count-i-1]-2))

    if count % 2 == 0:
        return ans
    return min(ans, (yaku[int(count//2)]*2)-2)

def main():
    n = int(input())
    print(walk_on_multiplication_table(n))

if __name__ == '__main__':
    main()