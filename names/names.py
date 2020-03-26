import time
# from .binary_seach_tree import BinarySearchTree
from binary_search_tree import BinarySearchTree


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()



start_time = time.time()


tree = BinarySearchTree("JUST A PLACEHOLDER")

duplicates = []

for item_one in names_1:
    tree.insert(item_one)

for item_two in names_2:
    if tree.contains(item_two):
        duplicates.append(item_two)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime_binary_tree: {end_time - start_time} seconds")


start_time = time.time()

duplicates_two = []

names = set(names_1)

for item_two in names_2:
    if item_two in names:
        duplicates_two.append(item_two)


end_time = time.time()
print (f"{len(duplicates_two)} duplicates:\n\n{', '.join(duplicates_two)}\n\n")
print (f"runtime_python_set: {end_time - start_time} seconds")