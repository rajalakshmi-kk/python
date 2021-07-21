import sys
sys.setrecursionlimit(1009)
print(sys.getrecursionlimit())
i = 0

def greet():
    global i
    i+=1
    print("Python", i)
    greet()

greet()