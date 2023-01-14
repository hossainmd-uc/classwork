book = [[1,4,3,2,4], [1,6], [3,4], [], [0,2], [], [2]]

inverted = [[]] * len(book)

for ind_1, _ in enumerate (book):
    
    for ind_2, val_2 in enumerate (book):
        
        for each in val_2:
            
            if each == ind_1:
                print (each, "is equal to", ind_1, "at index", ind_2)
                if ind_2 not in inverted[ind_1]:
                    print(inverted)
                    inverted[ind_1].append(ind_2)
                    
                    
# print(inverted)