from array import *
arr = array('i',[])
n = int(input("enter the length of array"))

for e in range(n):
    x = int(input("Enter the value"))
    arr.append(x)
print(arr)

val=int(input('enter the search value'))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
print(arr.index(val))

    else:
         print("nope")