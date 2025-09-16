myList=[1,2,3,6,8,9]
squaredlist=[]

# for item in myList:
#     squaredlist.append(item*item)

# this is done using list comprehensions in easy way

squaredlist=[i*i for i in myList]

print(squaredlist)    