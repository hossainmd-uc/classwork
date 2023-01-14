##READING A FILE
f = open("data.txt")

emails = f.read()
# formatted_emails = emails.strip().split("\\")
# print(emails)

f.close()


#Temporary file open
formatted_emails = []
with open("data.txt") as data:
    # emails = data.read().split("\\")
    # print(emails)
    
    for line in data:
        each = (line.strip().split("\\"))
        formatted_emails.append(each)
        
##WRITING TO A FILE
with open("names.txt", "w") as n:
    n.write("Md Hossain\n")
    n.write("Rory Hollister\n")
    print("Louise", file=n)
    

# print(emails)
print(formatted_emails)
# for each in formatted_emails:
#     print(each)
    # id, _ = each.split("@")
    # print (id)