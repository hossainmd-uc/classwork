#Week 3 Lecture 2

lst = [1, 7, 4, 2]

#doubles list size with same values
print(lst * 2)


import random
num_of_matches = 0

r = random.randint(0, 10)
for each in lst:
    if each == r:
        num_of_matches += 1
        
print("matches", num_of_matches)

#construct list of n duplicate items
count = [0] * 10


#concatenating lists
lst1 = ["apples", "oranges"]
lst2 = ["pears", "tangerine"]

lst3 = lst1 + lst2

print(lst3)

#pointers to same object in memory

animals = ["cats", "dogs"]
more_animals = animals

more_animals[1] = "tacos"

print(animals[1])

#reference equality of lists
print("id equal?", id(animals) == id(more_animals))
        
        
#.extend /.insert method
animals.extend(["cows", "wolves", "foxes"])

animals.insert(0, "lion")
print(animals)

#delete value in list

del animals[0]
print(animals)

#pop method - takes value out of list and returns it
x = animals.pop(0)
print(x)

#reverses a list
animals.reverse()
print(animals)

#reverse using slicing -- create a new list
animals1 = animals[::-1]
print(animals1)

#Tuples
#A tuple is immutable ( cannot change the value but you can only set them.)
tuple1 = (1, 8, 2)
print(tuple1[2])


#tuple syntax allows multiple variables to be created at once
a, b = 1, 9
print(a, b)

#You can unpaxk tuples in order but you need the same number of objects on both sides
t =(1, "dog", 166)

x, y, z = t
print(x, y, z)

#iterating through a tuple
coordinates = [("Chicago", 1, 4), ("New York", 8, 3), ("New Orleans", 9, 2)]
for city, lon, lad in coordinates: #use _ to omit
    print(city, lon, lad)
    
    
#Finding min value in a list
lst = [3, 5, 1, 7, 9, 2]
minn = lst[0]
idx = 0

for i, v in enumerate(lst):
    if v < minn:
        minn = v
        idx = i
        
print("index:", idx, "max:", minn)
    