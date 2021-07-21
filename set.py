 # set is not an ordered collections
set1= {10,20,30,40,50}
print(set1)

# different elements are allowed into set
set2 = {1.4,799,'and',00}
print(set2)

# duplicate values are removed
set3 = {10,20,30,40,50,20,30,'xyz','and','xyz','zyx'}
print(set3)

# indexing is not applicable in set-gives error
# s = {10,20,30,40}
# s[1]

# set allows to add and discard elements
set= {10,20,30,40,50}
set.add(60)
print(set)

set= {10,20,30,40,50}
set.discard(10)
print(set)