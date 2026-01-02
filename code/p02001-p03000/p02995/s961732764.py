
A, B, C, D = list(map(int, input().split()))

def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)


sais = lcm(C, D)

buff_a = A - 1


sais_mx = B // sais
sais_mm = buff_a // sais
sais_count = sais_mx - sais_mm
if sais_mx > 0:
    sais_count = sais_mx - sais_mm
else:
    sais_count = 0

# print('sais_mx ' + str(sais_mx))
# print('sais_count ' + str(sais_count))

c_mx = B // C
c_mm = buff_a // C
c_count = c_mx - c_mm

d_mx = B // D
d_mm = buff_a // D
d_count = d_mx - d_mm

# print("c d")
# print(c_count, d_count)
zentai = c_count + d_count

# zentai = zentai - (sais_count*2)
zentai = zentai - (sais_count)

b_a = B - A
ans = b_a - zentai
# print(zentai)
print(ans+1)
