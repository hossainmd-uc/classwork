#Return statements

#Is Prime function
define is_prime(num):
    
    if num == 1:
        return False
    else:
        for i in range (2, num):
            if num % 1 == 0:
                return False
            
        return True
    
def minmax(lst):
    '''
    Given list of numbers, return min and max values as a tuple
    
    Input:
    
        lst: a list of numbers
    
    Output: Min and Max Value (tuple)
    
    '''
    
    return (min(lst), max(lst))

