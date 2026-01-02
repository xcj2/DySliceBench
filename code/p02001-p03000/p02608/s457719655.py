#from matplotlib import pyplot as plt
def binary_search(mn,mx,a,x,y):
    #リストlからaの値のインデックスをサーチする。
    #二分探索を可能にするためにはリストlはソートされていなければならない。
    z = (mx+1)//2
    low = mn
    high = mx+1
    while low <= high:
        temp = rule2(x,y,z)
        if temp == a:
            if z <= 0:
                return None
            return z
        elif temp < a:
            low = z + 1
        elif temp > a:
            high = z - 1

        z = (low + high) // 2
    return None

def rule2(x,y,z):
    return x ** 2 + y ** 2 + z**2 + x * y + y * z + z*x
def main():
    n = int(input())
    x = []
    y = []
    for i in range(1,n+1):
        #x.append(i)
        #y.append(f(i))
        print(f(i))
    #plt.scatter(x,y)
    #plt.show()


def f(n):
    counter = 0
    for x in range(1,n):
        if x ** 2 > n:
            break
        for y in range(x,n-x**2):
            if y < x:
                continue
            if x ** 2 + y ** 2 > n:
                break
            z = binary_search(y,n-x**2-y**2-x*y,n,x,y)
            if z == None:
                continue
            else:
                if rule2(x,y,z) == n:
                    if x == y and y == z and z == x:
                        counter += 1
                    elif x != y and y != z and z != x:
                        counter += 6
                    else:
                        counter += 3

    return counter


if __name__ == '__main__':
    main()

#6 24 54 96
#1  4  9 16
#18