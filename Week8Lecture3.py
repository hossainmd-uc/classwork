
#Merged Sort

#l1 = [1,2,8,12]
#l2 = [5,7,16,23]


def merge(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    else:
        first1, *rest1 = l1
        first2, *rest2 = l2
        
        if first1 < first2:
            return [first1] + merge(rest1, l2)
        else:
            return [first2] + merge(l1, rest2)
    
def merge_sort(lst):
    
    if 0 <= len(lst) and len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        sorted_left = merge_sort(lst[0:mid])
        sorted_right = merge_sort(lst[mid:])
        
        return merge(sorted_left, sorted_right)

print(merge_sort([1,99,5,4,33,45]))

def binary_search(lst, val):
    if lst == []:
        return False
    else:
        mid = len(lst) // 2
        if  val == lst[mid]:
            return True
        elif val > lst[mid]:
            binary_search(lst[mid:], val)
        else:
            binary_search(lst[:mid], val)
            
def binary_search_alt(lst, val, low, high):
    if lst == []:
        return False
    else:
        mid = (low + high) // 2
        if  val == lst[mid]:
            return True
        elif val > lst[mid]:
            binary_search(lst, val, mid + 1, high)
        else:
            binary_search(lst, val, low, mid)