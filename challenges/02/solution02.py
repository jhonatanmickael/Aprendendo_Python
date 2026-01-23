# Author: jhonatanmickael
# Description: Merge Sorted Arrays (In-place)
# Challenge by: 'Labs One Bit Code'
# Date: 2026-01-23

list1 = [1, 3, 5, 0, 0, 0]
list2 = [2, 4, 6]

len_list1 = len(list1) 
len_list2 = len(list2) 

array = [x for x in range(len_list1 - len_list2, len_list1)]

for y, x in enumerate(array):
    list1[x] = list2[y]

list1.sort()

print(list1)


