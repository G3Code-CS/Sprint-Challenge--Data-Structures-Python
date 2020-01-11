import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# duplicates = [x for x in names_1 for y in names_2 if x == y]
# Using Binary search tree
# Input the contents in names1 to the tree
# Loop names2 and traverse through binary search tree to see if it exists
# update duplicate if exists

binarySearchTree = BinarySearchTree(names_1[0])
for name in names_1:
    binarySearchTree.insert(name)

for name in names_2:
    if binarySearchTree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# For the stretch goal I am going to use Binary search. 
# Sort the first array and then loop the second array to find item in the first sorted array

def binary_search(arr, target):
    # arr.sort()
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1
