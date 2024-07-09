T = int(input())
for i in range(T):
    ox = input()
    total = 0
    score = 0
    for x in ox:
        if x == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)