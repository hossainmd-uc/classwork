# #Hello World

# i = 0

# while i < 5: 
#     print("i = "+ str(i))
#     i = i + 1
    
    
# for i in range(0,5):
#     print("i = "+ str(i))
#     i = i + 1
    
# lst = [1, 6, 7, 12]

# #Preallocation of memory
# total = 0 
# for i in lst:
#     total = i + total
#     #break
# print(total)
    
# #Even / Odd in list
# for i in lst:
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")
        
#Sort a list (Inefficient)

unsorted = [-1000, 1, 9, 23, 5653, 56, 11, 99, 0, -2]
##Sorter based on comparing adjacent numbers
# SUCCESS_THRESHOLD = len(unsorted)-1
# successful_comparisons = 0

# while True:

#     for i in range(0, len(unsorted)-1):
        
#         if unsorted[i] > unsorted[i + 1]:
#             temp = unsorted[i]
#             unsorted[i] = unsorted[i + 1]
#             unsorted[i + 1] = temp
#             print(i, unsorted)
#         else:
#             successful_comparisons = successful_comparisons + 1
#             print(successful_comparisons)
            
#     if SUCCESS_THRESHOLD == successful_comparisons:
#         break
#     else:
#         successful_comparisons = 0
            
 print("sorted:", unsorted)

        
#Add list 

# listy = [-1, 2, 1]

# total = 0
# for i in listy:
#     if i < 0:
#         total = total + (-1 * i)
#     else:
#         total = total + i
    
# print(total)


# import random

# n_flips = 0
# consecutive_heads = 0
# target = 5


# while consecutive_heads < target:
    
#     if random.randint(0,1) == 0:
#         consecutive_heads = consecutive_heads + 1
#         flips = flips + 
#     else:
#         consecutive_heads = 0
# print("Got", target, "consecutive heads in", n_flips, "flips")
    
# N = 23
# power_counter = 1

# while 2 ** power_counter < N:
#     if (2 ** (power_counter + 1) < N):
#         power_counter = power_counter + 1
#     else:
#         break
    
# print(power_counter)

# while 2 ** power_counter < N:
#     power_counter = power_counter + 1
    
# print(power_counter-1)