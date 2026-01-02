# Standard module
import math

# 3rd party's module

# Original module  

class CalcVal():
    def set_num(self, num):
        self._num = num
        self._calc_ord()
        
    def get_sum_pow(self):
        max_rng = math.ceil(self._ord/2.)
        sum_data = 0
        for i in range(max_rng):
            sum_data += 9*10**(i*2)
        return sum_data
    
    def get_remain_cal(self):
        self._ord = math.floor(math.log10(self._num))
        if self._ord == 0:
            #DO NOT count 0
            return self._num
        else:
            return self._num - 10**self._ord + 1
        
    def do(self):
        sum_data = self.get_sum_pow()
        if self._ord%2 == 0:
            sum_data += self.get_remain_cal()
        return sum_data
        
    
    def _calc_ord(self):
        self._ord = math.floor(math.log10(self._num))


def main_func():
    cv = CalcVal()
    cv.set_num(int(input()))
    print(cv.do())
        

main_func()