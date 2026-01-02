# coding: utf-8
# Here your code !
from sys         import exit
from collections import Iterable
from unittest    import TestCase

#import numpy as np

def top_face_after_rolling_dice():
    try:
        faces    = [int(num) for num in input().rstrip().split()]
        rollings = input().rstrip()
    except:
        return __input_error()

    dice = CubicArbitraryValueDice(faces[0], faces[1], faces[2], faces[3], faces[4], faces[5])
    dice.put(dice.TOP, dice.SOUTH, dice.EAST, dice.WEST, dice.NORTH, dice.BOTTOM)
    
    for operator in rollings:
        dice.roll(operator)

    print(dice.get_value(dice.TOP))

class CubicArbitraryValueDice():
    (TOP, BOTTOM, EAST, WEST, SOUTH, NORTH, RIGHT, LEFT) = ("top", "bottom", "E", "W", "S", "N", "R", "L")
    (stVALUE, stDIRECTION) = ("value", "direction")

    (plus_x, minus_x, plus_y, minus_y, plus_z, minus_z) = ( (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1) )

#    ROLL_x2y = np.array([ [ 0,-1, 0], [ 1, 0, 0], [ 0, 0, 1] ])
#    ROLL_y2x = np.array([ [ 0, 1, 0], [-1, 0, 0], [ 0, 0, 1] ])
#    ROLL_y2z = np.array([ [ 1, 0, 0], [ 0, 0,-1], [ 0, 1, 0] ])
#    ROLL_z2y = np.array([ [ 1, 0, 0], [ 0, 0, 1], [ 0,-1, 0] ])
#    ROLL_z2x = np.array([ [ 0, 0, 1], [ 0, 1, 0], [-1, 0, 0] ])
#    ROLL_x2z = np.array([ [ 0, 0,-1], [ 0, 1, 0], [ 1, 0, 0] ])

    ROLL_x2y = ( ( 0,-1, 0), ( 1, 0, 0), ( 0, 0, 1) )
    ROLL_y2x = ( ( 0, 1, 0), (-1, 0, 0), ( 0, 0, 1) )
    ROLL_y2z = ( ( 1, 0, 0), ( 0, 0,-1), ( 0, 1, 0) )
    ROLL_z2y = ( ( 1, 0, 0), ( 0, 0, 1), ( 0,-1, 0) )
    ROLL_z2x = ( ( 0, 0, 1), ( 0, 1, 0), (-1, 0, 0) )
    ROLL_x2z = ( ( 0, 0,-1), ( 0, 1, 0), ( 1, 0, 0) )
    
    DIRECTION = { EAST : plus_x,   WEST : minus_x,  NORTH : plus_y,   SOUTH : minus_y,  TOP   : plus_z,   BOTTOM : minus_z }
    OPERATOR  = { EAST : ROLL_z2x, WEST : ROLL_x2z, NORTH : ROLL_z2y, SOUTH : ROLL_y2z, RIGHT : ROLL_y2x, LEFT   : ROLL_x2y }
    
    #??¢???index??§?????????,???????????????
    def __init__(self, n_f0, n_f1, n_f2, n_f3, n_f4, n_f5):
        self.info = [ {self.stVALUE: n_fi} for n_fi in [n_f0, n_f1, n_f2, n_f3, n_f4, n_f5]]

    def put(self, dir_f0, dir_f1, dir_f2, dir_f3, dir_f4, dir_f5):  #?????°????????£?????????
        for (info, dir_fi) in zip(self.info, [dir_f0, dir_f1, dir_f2, dir_f3, dir_f4, dir_f5]):
            info[self.stDIRECTION] = self.DIRECTION[dir_fi]

    def roll(self, operator) : #opetator: (EAST, WEST, SOUTH, NORTH, RIGHT, LEFT) ??????????????????
        for info in self.info:
#            info[self.stDIRECTION] = tuple( np.dot(self.OPERATOR[operator], np.array(info[self.stDIRECTION])))
            vector = info[self.stDIRECTION]
            matrix = self.OPERATOR[operator]
            info[self.stDIRECTION] = tuple([sum( [matrix[row][col]*vector[col] for col in range(len(vector))] ) for row in range(len(matrix))])
            
    def get_value(self, direction):
        for info in self.info:
            if info[self.stDIRECTION] == self.DIRECTION[direction] :
                return info[self.stVALUE]
    
    def get_direction(self, value):
        for info in self.info:
            if info[self.stVALUE] == value :
                dir_key_values = self.DIRECTION.items()
                for items in dir_key_values:
                    if info[self.stDIRECTION] in items:
                        return items[0]

def __input_error():
    print("input error")
    return -1
    

class __TestValueClass(TestCase):
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
                for info_state in info :
                    print(info_state[0].ljust(swidth) + ":", info_state[1])
                exit()

        if print_success :
            print(func.__name__,": succeeded")

#test
if __name__ == "__main__" :
#    test = __TestValueClass()
    top_face_after_rolling_dice()
    
    
   
    
    