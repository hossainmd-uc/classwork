
#Lists
import enum


lang = ["C", "C++", "Python", "Java"]

empty = []

#lists are mutable (can be changed)

lang[1] = "C#"

#Splicing
print(lang[1:4])
#Step Splicing
print(lang[0:4:2])

#Cloning
lang_clone= lang[:]
print(lang_clone)


#Iterating over a list
for each in lang:
    print(each)
    
#Discouraged
for i in range(0, len(lang)):
    print(i ,lang[i])
#Encouraged    
for count, value in enumerate(lang):
    print(count, value)
    
#Adding to a list
lang.append("Racket")

#--------------Exercises--------
prices = [100.00, 9.00, 126.00, 12.00, 99.00, 19.00]
discounted = []
discount = 10

for each in prices:
    discounted.append(each * (1 - discount / 100))
    
print(discounted)
    
