# coding: utf-8
# Here your code !
import sys
from collections import Iterable
import unittest

def top_face_after_rolling_dice():
    try:
        faces    = [int(num) for num in input().rstrip().split()]
        rollings = input().rstrip()
    except:
        return __input_error()

    dice = CubicArbitraryValueDice(faces[0], faces[1], faces[2], faces[3], faces[4], faces[5])
    dice.put(dice.TOP, dice.SOUTH, dice.EAST, dice.WEST, dice.NORTH, dice.BOTTOM)
    
    for direction in rollings:
        dice.roll(direction)

    print(dice.faces[dice.direction[dice.TOP]])

class CubicArbitraryValueDice():
    TOP    = "top"
    BOTTOM = "bottom"
    EAST   = "E"
    WEST   = "W"
    SOUTH  = "S"
    NORTH  = "N"
    OPOSITE_DIRECTION_PAIRS = ( (EAST, WEST), (SOUTH, NORTH) )
    
    #??¢???index??§???????????????????????????
    def __init__(self, n_f0, n_f1, n_f2, n_f3, n_f4, n_f5):
        self.faces = [n_f0, n_f1, n_f2, n_f3, n_f4, n_f5]

    #???????????¢???index?????¢??£??????
    def put(self, dir_f0, dir_f1, dir_f2, dir_f3, dir_f4, dir_f5):  #?????°????????£?????????
        self.direction = { dir_fi : i for i,dir_fi in enumerate([dir_f0, dir_f1, dir_f2, dir_f3, dir_f4, dir_f5]) }

    #??¢???index????????´
    def roll(self, direction) : #dirction: (EAST, WEST, SOUTH, NORTH) ??????????????????
        for pair in self.OPOSITE_DIRECTION_PAIRS :
            if direction in pair :
                oposite = pair[0] if (pair[1] == direction) else pair[1]
        
        current = {}
        for direct in (self.TOP, self.BOTTOM, direction, oposite):
            current.update({direct : self.direction[direct]})

        #            direction to bottom,       bottom to oposite,      oposite to top,     top to direction 
        for pair in ((direction, self.BOTTOM), (self.BOTTOM, oposite), (oposite, self.TOP), (self.TOP, direction)):
            self.direction[pair[1]] = current[pair[0]]

def __input_error():
    print("input error")
    return -1

class __TestValueClass(unittest.TestCase):
    def testEqual(self, func, tuples, eff_digit = None, print_success = False):
        self.testFunction(self.assertEqual,func,tuples,eff_digit,print_success)
    
    def testFunction(self,assertfunc,func,tuples,eff_digit,print_success):
        #tuples[index] = ([*arguments of func], compared value)
        for item in tuples:
            try:
                if isinstance(item[0], Iterable):
                    value = func(*item[0])
                else:
                    value = func(item[0])
                
                if eff_digit is None :
                    assertfunc(value,item[1])
                else :
                    format_str = "{0:."+str(eff_digit)+"g}"
                    assertfunc(format_str.format(value),format_str.format(item[1]))
                    
            except Exception as msg:
                swidth = 15
                print("="*50)
                print("-- Assertion Error in '" + func.__name__ + "' --")
                info = []
                info.append(["arguments"     , item[0]    ])
                info.append(["compared value", item[1]    ])
                info.append(["message"       , "\n" + msg ])
                for state in info :
                    print(state[0].ljust(swidth) + ":", state[1])
                sys.exit()

        if print_success :
            print(func.__name__,": succeeded")

#test
if __name__ == "__main__" :
#    test = __TestValueClass()
    top_face_after_rolling_dice()
    