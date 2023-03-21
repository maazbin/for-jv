# myList = ["Orange","Banana","Apple","Mango"]

# for i in range(1,len(myList)-1): # -> range(4)
#     print(myList[i])

import random
 
myList=[]
n = int(input('size of the list :'))
for i in range(n):
    myList.append(random.randint(3,9))

print(myList[-5:-1])
print(myList)

# for index , name in enumerate(myList):
#     print(myList[index])

    # (index,name)

    