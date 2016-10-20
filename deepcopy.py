from copy import deepcopy

list1 = [1, 2, 9, [4, 8, 6, 7]]
list2 = deepcopy(list1)

print(id(list1))


print(id(list2))

print(id(list1[3]))
print(id(list2[3]))
