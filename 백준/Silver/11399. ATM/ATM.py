import sys
ppl = int(sys.stdin.readline())
time = sorted(list(map(int, sys.stdin.readline().split())))

result = []
result.append(time[0])
for i in range(1,ppl):
    result.append(time[i] + result[i-1])
print(sum(result))