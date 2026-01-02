# coding: utf-8
# Your code here!

def judge(number):
    def digit(check_num , number):
        if int(check_num) > number:
            return 0
        
        if all(check_num.count(digit_num) > 0 for digit_num in "753"):
            # print("dp:",check_num)
            count = 1
        else:
            # print("no_dp:",check_num)
            count = 0
        
        for add_num in "753":
            count = count + digit(check_num + add_num , number)
            # print("conut:{},add_num:{}".format(count,add_num))
        return count
        
    print(digit("0",number))

def main():
    number = int(input())
    judge(number)
    
if __name__ == "__main__":
    main()
    
