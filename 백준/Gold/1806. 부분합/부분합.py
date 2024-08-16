# 투포인터 알고리즘 (두 포인터 모두 앞에서 시작하되 속도가 다르게 움직이는 방식)
n, s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_length = 1e9

while True:
    if sum >= s:
        min_length = min(min_length, right-left)
        sum -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        sum += nums[right]
        right += 1

if min_length == 1e9:
    print(0)
else:
    print(min_length)