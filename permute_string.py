# A Python program to print all
# permutations using library function
from itertools import permutations
#import pyenchant

# Get all permutations of inout string
def permute (string_x):
    perm = permutations(string_x)
    return perm

# convert each list items to strings
def to_string(list_x):
    string = ""
    for i in list(list_x):
        for y in i:
            string += y
    return string

def de_duplicate (list_x):
    ded_list = []
    for l in list_x:
        if l not in ded_list:
            ded_list.append(l)
    return ded_list

string_in = input()
strings = permute(string_in)
list_ = []
#d = pyenchant.Dict("en_US")
for j in strings:
    r = to_string(j)
    list_.append(r)
    #if d.check(r):
     #   print("The string "+r+" is in dictionary")
print("--------------------------------")
print(list_)
print("---------- De Duplicate the list")
ded_l = de_duplicate(list_)
print(ded_l)


