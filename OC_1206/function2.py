#default parameter를 지정할 수 있다.
def add(a,b=2):
    return a+b

result = add(1,3)
print(result)

result=add(3)
print(result)
