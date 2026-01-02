import sys

def get_gcd(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        return get_gcd(b, a % b)

def get_lcm(a, b, gcd):
    lcm = a * b // gcd
    return lcm

def main():
    while True:
        data = sys.stdin.readline().strip()
        if data is None or data == '':
            break

        nums = data.split(' ')
        a = int(nums[0])
        b = int(nums[1])
        gcd = get_gcd(a, b)
        lcm = get_lcm(a, b, gcd)
        print(gcd, lcm)
        
        
if __name__ == '__main__':
    main()
    