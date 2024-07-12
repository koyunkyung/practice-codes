import sys
words = []
for _ in range(int(sys.stdin.readline().strip())):
    words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort()
words.sort(key=len)
for k in words:
    print(k)