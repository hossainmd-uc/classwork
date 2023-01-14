#Homework 4 Exercise 5 longer solution

    # for i,each in enumerate(splitted):
    #     if blanks_visible:
    #         if i != len(splitted)-1:
    #             if len(each) < width:
    #                 for _ in range(width-len(each)):
    #                     each += "_"
    #                 cumulative_text += each + "\n"
    #             else:
    #                 cumulative_text += each + "\n"
    #         else:
    #             if len(each) < width:
    #                 for _ in range(width-len(each)):
    #                     each += "_"
    #                 cumulative_text += each
    #             else:
    #                 cumulative_text += each
    #     else:
    #         if i != len(splitted)-1:
    #             cumulative_text += each + "\n"
    #         else:
    #             cumulative_text += each
    
#FUNCTIONS
    
def function_name(arg1, arg2):
    #do something
    return result
    
#Multiply function
def multiply(a,b):
    '''
    Computes the product of two number a,b.
    
    Input:
        a (int)
        b (int)
    
    Output:
        Integer Product (a * b)
        
    '''
    return a * b

print(multiply(5,5))

def main():
    
    x, y, z = 5, 4, 3
    
    print("Calling multiply(x, y)")
    r = multiply(x, y)
    print("Result of multiplying(x, y) is", r)
    print("Calling multiply(x, z)")
    r = multiply(x, z)
    print("Result of multiplying(x, y) is", r)
    print("Calling multiply(y, z)")
    r = multiply(y, z)
    print("Result of multiplying(x, y) is", r)
    
main()

