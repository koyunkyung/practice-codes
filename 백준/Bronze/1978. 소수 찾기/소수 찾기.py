n = int(input())
nums = list(map(int, input().split()))

prime = 0
for i in nums:
    if i == 1:
        pass
    else:
        ndiv = 0
        for j in range(1, i+1):
            if i % j == 0:
                ndiv += 1
        if ndiv == 2:
            prime += 1
print(prime)