n = int(input())
nums = list(map(int, input().split()))

prime = 0
for i in nums:
    error = 0
    if i > 1:
        for j in range(2, i):   # 1과 자기자신 제외 숫자들 중 약수 있는지 확인
            if i % j == 0:
                error += 1
        if error == 0:
            prime += 1
print(prime)