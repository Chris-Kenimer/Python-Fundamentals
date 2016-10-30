a = [2,4,10,16]
bList = []
def multiply(a):
    b = a *5
    bList.append(b)

for i in a:
    multiply(i)
print bList
