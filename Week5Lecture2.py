#Dictionary

# d = {"A": 'Geeks', "A+": 'For', "A-": 'Geeks'}
# print(d.keys())

# del d["A"]
# print(d.keys())

# #You can iterate much faster over a dictionary
# print(d.items())
# for k,v in d.items():
#     print(k,v)
    
# hw1 = {"Name": 'Homework 1', "Date": '2022/9/27'}
# hw2 = {"Name": 'Homework 2', "Date": '2022/10/07'}
# hw3 = {"Name": 'Homework 3', "Date": '2022/10/14'}

# hws = [hw1, hw2, hw3]

# for hw in hws:
#     print(hw["Name"], "is due on", hw["Date"])
    
    
import csv
    
# with open("instructors.csv") as f:
    
#     reader = csv.DictReader(f)

    
#     for row in reader:
#         # print(row)
#         print("{} {}'s email is {}".format(row["fname"], row["lname"], row["email"]))
        
        
import json

l = ["baz", {"foo": 1.0, "bar": 2.0}]

print(json.dumps(l, sort_keys= True, indent = 4))

dict1 = json.loads('[{"foo": 22, "bar": 66}]')
print(dict1)
        
with open("random.json") as r:
    random = json.load(r)
    # print(json.dumps(r, sort_keys= True, indent = 4))
    print(random)