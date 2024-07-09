a = int(input())
b = int(input())
c = int(input())
for i in range(10):
    prod = str(a*b*c)
    i = str(i)
    print(prod.count(i))