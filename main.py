
# slicing
# x = 'computer'
# print(x[1:4])
# print(x[1:6:2])
# print(x[3:])
# print(x[2:4:8])


# adding/concatenating
# x = 'horse' + 'shoe'
# print(x)

# y = ['pig', 'cow'] + ['horse']
# b = ['apple', 'banana'] + ['watermelon', 'mersedes']
# print(y)
# print(b)

# z = ('Kevin', 'Niklas', 'Jenny') + ('Avaz', 'Avazjon')
# p = ('Islomov', 'Bahromov') + ('Karimov', 'Sultonov')
# print(z)
# print(p)

# multiplying - multiply a sequence using *

# x = 'bug' * 3
# x = 'Avazjon' * 4
# print(x)

# y = [8, 5] * 4
# y = [0, 4] * 10
# print(y)

# z = (2, 4) * 3
# z = ('Avaz', 7) * 5

# print(z)

# checking membership - test whether an item is or is not in a sequence / True or False 

# string
# x = 'bug'
# print ('u' in x )
# print('a' in x)
# print ('b' and 'g' in x)

# # list 
# y = ['pig', 'cow', 'horse']
# print('cow' not in y) 
# print('pig' in y)
# print('apple' in y)

# # tuple
# z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print('Niklas' in z)
# print('Niklas' not in z)


# iterating - iterating through the items in a sequence 

# item

# x = [7, 8, 3]
# for item in x:
#     print(item)

# y = [1, 3, 5, 7, 9]
# for item in y: 
#     print(item)

# z = (1, 2, 3, 4, 5)
# for item in z:
#     print(z)

# index & item 
# y = [7, 8 ,3 ]
# for index, item in enumerate(y):
#     print(index, item)
# b = {1, 2, 3, 4}
# for index, item in enumerate(b):
#     print(index, item)
# z =(2, 5, 7, 8)
# for i in range(len(z)):
#     print(z[i])

# number of items - count the number of items in a sequence

# x = 'apple'
# print(len(x))

# y = ['pig', 'cow', 'horse']
# print(len(y))

# minimum - find the minimum item in a sequence lexicographically. Alpha or numeric types, but cannot mix types.

# x = "bug"
# print(min(x))
 
# c = "banana"
# print(min(c))

# maximum - find the maximum item in a sequence lexicographically. Alpha or numeric types, but cannot mix types.

# x = "bug"
# print(max(x))


# sum - find the sum of items in a sequence. Entire sequence must be numeric.

# list 
# y = [2, 5 ,8, 12]
# print(sum(y))
# print(sum(y[-2:]))

# b = [5, 7, 4, 8]
# print(sum(b[-1:]))

# z = [1, 4, 6]
# print(sum(z[:-1]))

# sorting - returns a new list of items in sorted order. Does not change the original list.

# x  = 'bug'
# print(sorted(x))

# sorting - sort by second letter. / Add a key  parameter and a lambda function to return the second character. (the word key here is a defined parameter name, k is an arbitary variable name).
# z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print(sorted(z, key=lambda k: k[1]))

# f ={'Avaz', 'Abu', 'Kama', 'Bek'} 
# print(sorted(f, key=lambda k: k[2]))


# delete - delete an item from a list or dictionary by specifying its index or key.

# x = [1, 2, 3, 4, 5]
# del (x[2])
# print(x)

# h =[1, 2, 3, 4, 5]
# del(h[4])
# print(h)

# append - add an item to the end of a list.

# y = ['pig', 'cow', 'horse']
# y.append('sheep')
# print(y)

# a = [1, 2, 3]
# a.append(4)
# print(a)

# extend - append a sequence to a list

# x = [1, 3, 6, 9]
# y =[11, 17]

# x.extend(y)
# print(x)


# x = [1, 3, 6, 9]
# y = [11, 17]

# y.extend(x)
# print(y)


# insert - insert an intem at a given index

# x = [1, 2, 3, 4, 5, 6]
# x.insert(2, 111)
# print(x)

# y = [11, 22, 33, 44]
# y.insert(3, 111111)
# print(y)


# pop - pops last item off list and returns item

# x =[1, 2, 3, 4, 5, 6]
# x.pop() # pops of the 6
# print(x)
# print(x.pop())
 

# remove - remove first instance of an item

# x = [1, 2, 3, 4, 5, 6, 7]
# x.remove(3)
# x.remove(7)
# x.remove(1)
# print(x)


# reverse - reverse the order of the list. It is an in-place sort, meaning it changes the original list.

# x = [1, 2, 3, 4, 5]
# x.reverse()
# print(x)

# x = [5, 4, 3, 2, 1]
# x.reverse()
# print(x)


# count(item) - returns count of an item

# string 
# x = 'hippo'
# print(x.count('p'))

# # list 
# y = ['pig', 'cow', 'horse', 'cow']
# print(y.count('cow'))

# # tuple
# z = ('Kevin', 'Niklas', 'Jenny', 'Craig', 'Kevin', 'Kevin')
# print(z.count('Kevin'))

# index(item) - returns the index of the first occurence of an item.


# string 
# x = 'hippo'
# print(x.index('p'))

# # list 
# y = ['pig', 'cow', 'horse', 'cow']
# print(y.index('cow'))

# # tuple
# z = ('Kevin', 'Niklas', 'Jenny', 'Craig',)
# print(z.index('Kevin'))


# unpacking - unpack the n items of sequence into n variables 

# x = ['pig', 'cow', 'horse']
# a, b, c = x
# print(a, b, c)


# constructors - creating a new list 

# x = list()
# y = ['a', 25, 'dog', 8.43]
# tuple1 = (10, 20)
# z = list(tuple1)

# # list comperhension 
# a = [m for m  in range(8)]
# print(a)
# b = [i**2 for i in range(10) if i>4]
# print(b)

# sort - sort list in place.

# x = [5, 3, 8, 6]
# x.sort()
# print(x)


# b = ["Jek", 'Bek', 'Kek']
# b.sort()
# print(b)

# reverse sort - sort items descending.

# x = [5, 3, 8, 6]
# x.sort(reverse = True)
# print(x)

# b = [1, 4, 7, 9, 3]
# b.sort(reverse=True)
# print(b)


# TUPLES

# constructors - creating new tuples

x = ()
x = (1, 2, 3)
x = 1, 2, 3
x = 2,  # the comma tells Python it's a tuple
print(x, type(x))


list1 = [2, 4, 6]
x = tuple(list1)  
print(x, type(x))

# 
