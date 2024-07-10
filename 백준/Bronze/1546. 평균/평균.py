n = int(input())
rgrade = list(map(int, input().split()))

hgrade = []
for i in rgrade:
    h = (i/max(rgrade))*100
    hgrade.append(h)
print(sum(hgrade)/n)