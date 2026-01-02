def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
    return a * b // gcd(a, b)

def akarabmadecde(a: int, b: int, c: int):
    if a % c == 0:
        return (b // c) - (a // c) + 1
    else:
        return (b // c) - (a // c + 1) + 1

def main():
    input_str = input()

    a, b, c, d = input_str.split()

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    x = akarabmadecde(a, b, c)
    y = akarabmadecde(a, b, d)
    z = akarabmadecde(a, b, lcm(c, d))

    print((b - a + 1) - (x + y - z))

if __name__=="__main__":
    main()