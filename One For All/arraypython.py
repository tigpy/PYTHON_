#defining and declaring an Array
arr = [10,20,30,40,50]
print(arr)
#Accessing Array elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])
print(arr[-2])

brands = ["coke","apple","google","microsoft","toyota"]
print(brands)
#Finding the length of the array 
num_brands = len(brands)
print(num_brands)
#Adding an elements to an array using append()
brands.append("intel")
print(brands)
#Removing elements from an Array
colors = ["violet","indigo","blue","green","yellow","orange","red"]
print(colors)

del colors[4]
print(colors)

colors.remove("blue")
print(colors)

colors.pop(3)
print(colors)
#Modifying elements of an array using indexing
fruits = ["apple","banana","mango","Grapes","orange"]
print(fruits)
fruits[1]="pineapple"
fruits[-1]="Guava"
print(fruits)
#Concatenating two aaray using the + operator
concat = [1,2,3]
concat + [4,5,6]
print(concat)
concat = concat + [4,5,6]
print(concat)
#Repeating elements in an array
repeat = ["a"]
repeat = repeat * 5
print(repeat)
#slicing an Array 
fruits = ["apple","banana","mango","grapes","orange"]
print(fruits)
print(fruits[1:4])
print(fruits[ : 3])
print(fruits[-4:])
print(fruits[-3:-1])
#Declaring and  defining multidimensional array
multd = [[1,2],[3,4],[5,6],[7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
#star pattern 
rows = 5
for i in range(rows, 0, -1):
    for j in range(rows-i):
        print(end=' ')
    for j in range(2*i-1):
        print('*', end='')
    print('')



