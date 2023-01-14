

keys = ["a", "b", "c"]
values = [1, 2, 3]

print(dict(zip(keys,values)))


with open("names.txt") as f:
    print(f.read())
    
    

import csv

instructors = []
with open("instructors.csv") as f:
    for row in csv.DictReader(f):
        instructors.append(row)
        
# print(instructors)

# with open("instructors-copy.csv", "w") as f:
#     writer = csv.writer(f)
#     for row in instructors:
#         writer.writerow(row)
        
        
import json

with open("instructors-dict.json", "w") as f:
    json.dump(instructors, f)
    
