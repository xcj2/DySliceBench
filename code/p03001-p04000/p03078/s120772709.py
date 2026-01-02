def cake_gen(a,b,c,k):
    d=[]
    for i in a:
        for j in b:
            d.append(i+j)
    d.sort(reverse = True)
    d=d[:k]
    e=[]
    for i in c[:k]:
        for j in d:
            e.append(i+j)
    e.sort(reverse = True) 
    for i in range(k):
        print(e[i])           
    
def ma(): return map(int, input().split())
def main():
    x,y,z,k = ma()
    a = list(ma())
    b = list(ma())
    c = list(ma())
    a.sort(reverse = True)
    b.sort(reverse = True)
    c.sort(reverse = True)
    cake_gen(a,b,c,k)


if __name__ == '__main__':
    main()