def main():
    def get_inputs():
        li = []
        try:
            while True:
                li.append(input())
        except EOFError:
            return li

    def my_round(num, ndigits=3):
        num = num * 10**ndigits
        num = (num*2 + 1)//2
        num = num / 10**ndigits
        num = "{0:.3f}".format(num) ##
        return num

    li = get_inputs()
    for str_num in li:
        tmp = str_num.split(" ")
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        a,b,c,d,e,f = tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5]
        x = (c*e - b*f) / (a*e - b*d)
        x = my_round(x)
        y = (c*d - a*f) / (b*d - a*e)
        y = my_round(y)
        print("{} {}".format(x,y))
    return None


if __name__ == '__main__':
    main()