nums = []
for i in range(10):
    n = int(input())
    if n % 42 not in nums:
        nums.append(n %42)
print(len(nums))