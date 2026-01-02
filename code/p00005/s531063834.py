import sys

#最大公約数
def gcd(x, y):
    s = x / y
    r = x % y
    if r == 0:
        return y
    else:
        return gcd(y, r)

#最小公倍数
def lcm(x, y):
    return x*y/gcd(x, y)

def main():
    #print ("a")
    for line in iter(sys.stdin.readline, ""):
        #print (line)
        #tmp = sys.stdin.readline().split(" ")
        #print ("b")
        tmp = line.split(" ")
    
        a = int(tmp[0])
        b = int(tmp[1])
        #print ("a="+str(a))
        #print ("b="+str(b))
        #b = sys.stdin.readline()
        #print ("d")
        if a > b:
            c = a
            d = b
        else:
            c = b
            d = a

        print (str(gcd(c, d)) + " " + str(int(lcm(c,d))))

        #tmp = sys.stdin.readline()
        #if len(tmp) == 1:
        #    break
        #else:
        #    tmp = tmp.split(" ")

    #print ("exit")
     
if __name__ == "__main__":
    main()