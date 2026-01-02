class DataSet:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def swap(self):
        temp = self.y
        self.y = self.x
        self.x = temp

def main():
    data = []
    while 1:
        # ????????????????????????????????????
        n = input().split()
        x = int(n[0])
        y = int(n[1])

        if x == 0 and y == 0:
            break

        data.append(DataSet(x, y))

    length = len(data)
    what_large = length > 3000

    if what_large:
        print("Too Large")
    else:
        for i in range(len(data)):
            d_val = data[i]
            if d_val.x > d_val.y:
                d_val.swap()

            print("{0} {1}".format(d_val.x,d_val.y))

if __name__ == '__main__':
    main()