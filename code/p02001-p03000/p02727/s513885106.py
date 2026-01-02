from collections import defaultdict

############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input().rstrip()))
def inlt():
    return(list(map(int,input().rstrip().split())))
def insr():
    s = input().rstrip()
    return(s[:len(s) - 1])
def invr():
    return(map(int,input().rstrip().split()))
################################################################
X,Y,a,b,c = invr()
red = inlt() ; red.sort(reverse = True)
green = inlt(); green.sort(reverse = True)
colorless = inlt(); colorless.sort(reverse = True)

red = red[:X]
green = green[:Y]

red.reverse()
green.reverse()

r_index = 0
g_index = 0
c_index = 0
while True:
    if r_index >= len(red) or g_index >= len(green) or c_index >= len(colorless):
        break
    if red[r_index] > green[g_index]:
        if colorless[c_index] > green[g_index]:
            green[g_index] = colorless[c_index]
            g_index += 1
            c_index += 1
        else:
            break
    else:
        if colorless[c_index] > red[r_index]:
            red[r_index] = colorless[c_index]
            r_index += 1
            c_index += 1
        else:
            break

if r_index < len(red):
    if c_index < len(colorless):
        while r_index < len(red) and c_index < len(colorless):
            if red[r_index] < colorless[c_index]:
                red[r_index] = colorless[c_index]
                r_index+= 1
                c_index += 1
            else:
                break

if g_index < len(green):
    if c_index < len(colorless):
        while g_index < len(green) and c_index < len(colorless):
            if green[g_index] < colorless[c_index]:
                green[g_index] = colorless[c_index]
                g_index+= 1
                c_index += 1
            else:
                break

print(sum(red) + sum(green))
            
