
def permutations(lst):
    if lst == []:
        return [lst]
    else:
        rv = []
        for x in lst:
            lst_minus_x = [v for v in lst if v!= x]
            perms = permutations(lst_minus_x)
            for p in perms:
                permutation = [x] + p
                rv.append(permutation)
            
        return rv
    
# print(d for d in permutations([1,2,3,4]))

# for each in permutations([1,2,3,4]):
#     print(each)
    
print(permutations([1,2,3,4]))    
    
#Trees (Binary tree, unary tree etc)

