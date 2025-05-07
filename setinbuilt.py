#set removes duplicates


#add
# names = {'madhu','jaunty','vijay'}
# names.add('manoj')
# print(names)

#update
# numbers = {1,2,3,4,5}
# numbers.update([6,7,8])
# print(numbers)

#remove
# set = {2,5,7,8,9,10}
# set.remove(8)
# print(set)
# set.remove(4)

# discard
# set = {10,20,30}
# set.discard(20)
# print(set)
# set.discard(40) 

#pop
# num = {23,34,45,56,78,89,90}
# number = num.pop()
 
# print(num)
# num.pop()
# print(num)

# num.pop()
# print(num)
# print(type(num))
    
# l1 = [23,90,45,67,89,12,34,23]
# num = set(l1)
# print(num)

# for i in range(3):
#     num.pop()
#     print(num)

#clear
# num = {12,23,34,4,5,6,67,7,8}
# num.clear()
# print(num)

#union
# num_1 = {4,7,8,9,12,24}
# num_2 = {8,12,13,24,25,26}
# print(num_1.union(num_2))
# print(num_2.union(num_1))

#intersection
# x = {1,3,5,7,9}    #intersection prints common elements in both sets
# y = {2,3,4,5,6}
# print(x.intersection(y))


# x1 = {1,2,3,4,5}
# y1 = {1,2,3,4,5}
# print(x1.intersection(y1))

#Difference
# x2 ={20,30,40,55,66}
# y2 = {30,55,20,70,80}
# print(x2.difference(y2))   #prints elements in x2 that are not in y2
#print(y2.difference(x2))    # prints elements in y2 that are not in x2

#Symmetric Difference
# x3 = {62,25,74,47,85,58,96,59}   
# y4 = {43,92,78,25,85,74,62,26}
# print (x3.symmetric_difference(y4))     #prints elements that are in either x3 or y4 but not in both

x = {1,2,3,4,5}
y = {4,5,6,7,8}
print(x.symmetric_difference(y))     #prints elements that are in either x or y but not in both

#isisubset
# x1 = {1,2,3,4,5}
# y1 = {1,2}
# print(x1.issubset(y1))
# print(y1.issubset(x1))

#issuperset
# x2 = {1,2,3,4,5}
# y2 = {1,2,3}
# print(x2.issuperset(y2)) 




def sudoku
