#Global variable
a = 2

def changeA():
    # Local variable
    a = 3
    return a
def changeGlobalA():
    global a
    a = 3

b=changeA()
print(a)
print(b)

changeGlobalA()
print(a)
