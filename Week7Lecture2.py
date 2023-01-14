
#Recursion

def factorial_iter(n):
    prod = 1
    
    for i in range(1, n+1):
        prod = prod * i
    return prod

def factorial_rec(n):
    
    assert isinstance(n,int)
    assert n >= 0
    
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n-1) 
    
    
print(factorial_rec(3))

#You don't have a working version of the function but you have to trust that it
#will work

lst = ["Hello", "World"]

# first, *rest = lst

# print(first)

#Sum of the length of the strings

def count_string_length(l):
    
    if l == []:
        return 0
    else:
        
        first, *rest = l
        return len(first) + count_string_length(rest)
        
print(count_string_length(lst))

#Sorting

def insertion_sort(lst):
    if lst == []:
        return []
    else:
        first, *rest = lst
        sorted_rest = insertion_sort(rest)
        sorted_lst = insert(first, sorted_rest)
        return sorted_lst
    
def insert(v, lst):
    #assume that list is sorted
    if lst == []:
        return [v]
    else:
        first, *rest = lst
        if v < first:
            return [v] + lst
        else:
            return [first] + insert(v, rest)
        
print(insertion_sort([1,8,6,4,34,0,99]))