A, B, C, D, E, F = map(int, input().split())

def check_weight(a, b, c, d):
    if 100*A*a + 100*B*b + C*c + D*d <= F:
        return True
    else:
        return False

def check_conc(a, b, c, d):
    if C*c + D*d <= E * (A*a + B*b):
        return True
    else:
        return False

def check(a, b, c, d):
    if check_weight(a, b, c, d) and check_conc(a, b, c, d):
        return True
    else:
        return False

max_conc = 0
max_sugar_water = 0
max_sugar = 0

for a in range(F//(100*A) + 1):
    for b in range((F - 100*A*a)//(100*B) + 1):
        for c in range((F - 100*A*a - 100*B*b)//C + 1):
            for d in range((F - 100*A*a - 100*B*b - C*c)//D + 1):
                sugar = C*c + D*d
                water = 100*A*a + 100*B*b
                if water + sugar == 0:
                    continue
                if check(a, b, c, d) and max_conc <= 100*sugar/(water + sugar):
                    max_conc = 100*sugar/(water + sugar)
                    max_sugar = sugar
                    max_sugar_water = water + sugar

print(max_sugar_water, max_sugar)
