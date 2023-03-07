
def degree(x,y):
    x = x*y

a = int(input('A = '))
b = int(input('B = '))

result = a
for i in range(1, b):
    degree(result, a)

print(result)


def sumIt(sum,b,index=0):
    sum = sum + 1
    index = index + 1
    if index == b:
        return sum
    else:
        return sumIt(sum,b,index)

a = 2
b = 2

print(sumIt(a,b))
