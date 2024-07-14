n = int(input())

def fac(x):
    return x * fac(x-1) if x > 1 else 1
num = list(map(int, str(fac(n))))

idx = 0
for i in reversed(range(len(num))):
    if num[i] == 0:
        idx += 1
    else:
        break
print(idx)