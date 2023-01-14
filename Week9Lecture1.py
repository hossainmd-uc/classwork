
#New Recursive Sorting?

def quicksort(lst):
    if lst == []:
        return []
    else:
        pivot, *rest = lst
        left_side = []
        right_side = []
        for v in rest:
            if v < pivot:
                left_side.append(v)
            else:
                right_side.append(v)
        return quicksort(left_side) + [pivot] + quicksort(right_side)
    
print(quicksort([1,8,3,9,0,-20]))
      
      