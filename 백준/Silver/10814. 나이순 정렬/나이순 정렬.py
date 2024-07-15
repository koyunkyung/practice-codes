import sys
n = int(sys.stdin.readline())

ppl = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    ppl.append([int(age), name])
ppl.sort(key = lambda x: x[0])

for i in ppl:
    print(i[0], i[1])