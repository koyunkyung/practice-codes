T = int(input())
for _ in range(T):
    floor = int(input())
    num = int(input())
    ppl = [x for x in range(1, num+1)]

    for i in range(floor):
        for j in range(1, num):
            ppl[j] += ppl[j-1]
    print(ppl[-1])