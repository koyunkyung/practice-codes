import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]
dp = [(0, arr[0])]

# 이진탐색으로 e가 들어갈 위치 찾기 (LIS는 항상 오름차순으로 정렬된 리스트임)
def binarySearch(e):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start+end) // 2
 
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    # start가 end보다 커질 경우 더 이상 찾을 수 없으므로 start가 e가 들어갈 위치가 됨      
    return start

for i in range(1, n):
    # arr[i]이 LIS의 마지막 값보다 크면 arr[i]를 LIS에 추가
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
        dp.append((len(LIS)-1, arr[i]))
    # arr[i]이 LIS의 마지막 값보다 작거나 같으면 이진 탐색을 통해 LIS에서 arr[i]가 들어갈 위치 찾기
    else:
        idx = binarySearch(arr[i])
        LIS[idx] = arr[i]
        dp.append((idx, arr[i]))

print(len(LIS))

# 역추적 알고리즘으로 정확한 LIS 수열 구성 알아내기
last_idx = len(LIS) - 1
res = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last_idx:
        res.append(dp[i][1])
        last_idx -= 1

print(*res[::-1])