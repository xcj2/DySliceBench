formula_str = input()                                                                                                                                                                                       
formula_splitted = formula_str.split()                                                                                                                                                                      
                                                                                                                                                                                                            
def initialize(List): List[0] = 0                                                                                                                                                                           
                                                                                                                                                                                                            
def IsEmpty(List): List[0] == 0                                                                                                                                                                             
                                                                                                                                                                                                            
def IsFull(List): List[0] >= len(List) - 1                                                                                                                                                                  
                                                                                                                                                                                                            
def push(List, val):                                                                                                                                                                                        
    if IsFull == True: raise ValueError('Full')                                                                                                                                                             
    List[0] += 1                                                                                                                                                                                            
    List[List[0]] = val                                                                                                                                                                                     
                                                                                                                                                                                                            
def pop(List):                                                                                                                                                                                              
    if IsEmpty == True: raise ValueError('Empty')                                                                                                                                                           
    content = List[List[0]]                                                                                                                                                                                 
    List[0] -= 1                                                                                                                                                                                            
    return content                                                                                                                                                                                          
                                                                                                                                                                                                            
formula = [0 for i in range(0, len(formula_splitted) + 1)]                                                                                                                                                  
for content in formula_splitted:                                                                                                                                                                            
    if content == '*':                                                                                                                                                                                      
        val1, val2 = pop(formula), pop(formula)                                                                                                                                                             
        push(formula, val2 * val1)                                                                                                                                                                          
    elif content == '+':                                                                                                                                                                                    
        val1, val2 = pop(formula), pop(formula)                                                                                                                                                             
        push(formula, val2 + val1)                                                                                                                                                                          
    elif content == '-':                                                                                                                                                                                    
        val1, val2 = pop(formula), pop(formula)                                                                                                                                                             
        push(formula, val2 - val1)                                                                                                                                                                          
    else:                                                                                                                                                                                                   
        push(formula, int(content))                                                                                                                                                                         
                                                                                                                                                                                                            
print(pop(formula)) 
