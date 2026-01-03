x, y = map(int, input().split())
 
def xy_judge(x, y):
    if x >= 0:
        x_pos = True
    else:
        x_pos = False
    
    if y > 0:
        y_pos = True
    else:
        y_pos = False
        
    if abs(x) > abs(y):
        bifunc = 'g'
    elif abs(x) == abs(y):
        bifunc = 'e'
    else:
        bifunc = 'l'
    
    return x_pos, y_pos, bifunc
  
def x_pos_func(x, y, y_pos, bifunc):
    
    if bifunc == 'g' and y_pos:
        return (x - y) + 2
    
    elif bifunc == 'l' and y_pos:
        return (y - x)
    
    elif bifunc == 'g' and not y_pos:
        return (x - abs(y)) + 1
    
    elif bifunc == 'l' and not y_pos:
        return (abs(y) - x) + 1
    
    elif bifunc =='e' and y_pos:
        return 0
    
    elif bifunc =='e' and not y_pos:
        return 1
      
def x_neg_func(x, y, y_pos, bifunc):
    
    if bifunc == 'g' and y_pos:
        return (abs(x) - y) + 1
    
    elif bifunc == 'l' and y_pos:
        return (y - abs(x)) + 1
    
    elif bifunc == 'g' and not y_pos:
        return (abs(x) - abs(y))
    
    elif bifunc == 'l' and not y_pos:
        return (abs(y) - abs(x)) + 2
    
    elif bifunc =='e' and y_pos:
        return 1
    
    elif bifunc =='e' and not y_pos:
        return 0
      
x_pos, y_pos, bifunc = xy_judge(x, y)
 
if x_pos:
    print(x_pos_func(x, y, y_pos, bifunc))
elif not x_pos:
    print(x_neg_func(x, y, y_pos, bifunc))