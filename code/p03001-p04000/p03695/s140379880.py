def mapint_inp():
    return map(int, input().split())

def intinp():
    return int(input())

N = intinp()
a = mapint_inp()

def get_color(x):
    c = None
    if 399 >= x: c = "Gray"
    elif 799 >= x: c = "Blown"
    elif 1199 >= x: c = "Green"
    elif 1599 >= x: c = "Sky"
    elif 1999 >= x: c = "Blue"
    elif 2399 >= x: c = "Yellow"
    elif 2799 >= x: c = "Orange"
    elif 3199 >= x: c = "Red"
    else:
        c = "Any"
    return c

color_set = set()
num_of_any = 0

for a_i in a:
    c_i = get_color(a_i)
    if c_i == "Any":
        num_of_any += 1
        continue
    if c_i not in color_set:
        color_set.add(c_i)

num_of_colors = len(color_set)

if num_of_colors == 0:
    print(1, num_of_any)
else:
    print(num_of_colors, num_of_colors+num_of_any)