import sys

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
 
def gcd_list(li):
	if len(li) > 2:
		x = gcd(li[-1], li[-2])
		li = li[:-2] + [x]
		return gcd_list(li)
	else:
		return gcd(li[0], li[1])


def main():
    a = int(input())
    lists = list(map(int, input().split()))
    score = []

    if len(lists)==1:
        print(lists[0])
        sys.exit()

    bai = gcd_list(lists)

    for i in lists :
        num = bai / i
        score.append(num)

    bunbo = sum(score)

    ans = bai /bunbo
    print(ans)


if __name__ == '__main__' :
    main()