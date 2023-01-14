
#Strings (very similar to lists in terms of what you can do with them)
s1 = "Hello World!"

#Indexing Strings
print(s1[0])

#Slicing Strings
print(s1[0:13])

#String comparison (Value in memory)
s2 = "Hello World!"
print(s1 == s2)

#STRINGS ARE IMMUTABLE!!!<---------------------
#s2[6] = "w" ERROR
#print (s2)

#Find method in a string
location = s2.find("Hello")
print(location)

#Splitting String based on character
csv = "Hello,World,!"
splitted_list = csv.split(",")
print(splitted_list)

#Joining a list of Strings
joined_list = "|".join(splitted_list)
print(joined_list)

#UPPER and LOWER Case
s1_upper = s1.upper()
print("upper", s1_upper)
s1_lower = s1.lower()
print("lower", s1_lower)

#Embed data in string using curly braces
val = 42
val2 = 66
embedded_s1 = "Embed val: {}".format(val)
print(embedded_s1)
#alt
embedded_s1 = f"Embed val and val2: {val} {val2}"
print(embedded_s1)

#Rounding Embedded numbers
PI = 3.14159265358979323846264
embedded_s1 = "Embed PI rounded 2 digits: {:.2f}".format(PI)
print(embedded_s1)

embedded_s1 = f"Embed PI rounded 4 digits {PI:.4f}"
print(embedded_s1)

#Formatting numbers in a loop
for i in range(0,20):
    print(f"{i:0>9.2f}")
    
#????
for i in range(0,20):
    print(f"{i:2>8}")

#help(str) <--------CODE TO SEE POSSIBLE COMMANDS FOR DATA TYPES
