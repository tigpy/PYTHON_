#creating sets
#set of integers 
my_set1 = {11,33,66,55,44,22}
print(my_set1)

#sets of mixed datarypes 
my_set2 = {101, "Aryan",(21,2,1994)}
print(my_set2)
#duplicate value are not allowed
my_set3 = {11,22,33,33,44,22}
print(my_set3)

#set cannot have mutable items
#my_set4 = {1, 2, [3, 4]}

#we can make set from a list
my_set5 = set([1,2,3,4])
print(my_set5)
print(type(my_set5))

#we can make list from a set
my_list1 = list({11,22,33,44})
print(my_list1)
print(type(my_list1))
#operation on sets
my_set1 = {11,22,44,66,55}
print(my_set1)

#'set' object does not support indexing

#my_set1[0]

#add an element
my_set1.add(55)
print(my_set1)

#add multiple elements
my_set1.update([88,99,22])
print(my_set1)

#add list and set
my_set1.update([100,102],{103,104,105})
print(my_set1)

#remove and discard
#initialize my_set
my_set1 = {11, 33, 44, 55, 66}
print(my_set1)

#discard an element which is not present, no error
my_set1.discard(4)
print(my_set1)

#remove an element which is not persent, error raised
#my_set1.remove(6)

#discard an element
my_set1.discard(44)
print(my_set1)
my_set1.remove(55)
print(my_set1)

#using pop()
#initialize my_set
my_set1 = {11, 33, 44, 55,66}
print(my_set1)

#pop an element
print(my_set1.pop())

#pop another element
print(my_set1.pop())
print(my_set1)

#clear my_set
my_set1.clear()
print(my_set1)

#set operations - union

