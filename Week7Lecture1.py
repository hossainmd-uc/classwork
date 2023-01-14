
#Try Catch blocks


try: 
    int("h21")
except ValueError as err:
    print("message:", err)
    
import sys #Why?

try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())

except OSError as err:
    print("OSError", err)
except ValueError as err:
    print("ValueError", err)
except Exception as err:
    print(f"Unexcepted: {err=}: {type(err)=}")
    raise


#manually raise errors

try:
    raise NotImplementedError("Hey something didn't do right.")
except NotImplementedError as err:
    print("NIE:", err)
finally:
    print("prints no matter what. Exception or no exception")

#Creating own error
class NegativeNumber(Exception):
    """Raised when there is a negative number"""
    pass

x = -1

try:
    if x < 0:
        raise NegativeNumber
except NegativeNumber as err:
    print("There is a negative number!")
    

#Example of callstack error handling


def foo(x, y):
    # print(x/y)
    print(x/p)
    
def baz():
    try:
        foo(1/0)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        
    except NameError as err:
        print("variable doesn't exist", err)
        

baz()
    
    
    
#ITERATOR

# class NotIter:
    
#     def __init__(self, x):
#         self.x = x
        
# ni = NotIter(3)
# for i in ni:
#     print(i)
    
    

class YesIter:
    
    def __init__(self, x):
        self.x = x 
        
    def __iter__(self):
        self.iter_counter = self.x
        return self
    
    #Condition to raise exception to stop program
    def __next__(self):
        if self.iter_counter <=0:
            raise StopIteration
        rv = self.iter_counter
        self.iter_counter  = self.iter_counter - 1
        return rv
    
yi = YesIter(10)

for each in yi:
    print(each)
for each in yi:
    print(each)