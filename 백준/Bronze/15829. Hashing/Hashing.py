L = int(input())
words = str(input())

from string import ascii_lowercase
import math
alist = list(ascii_lowercase)
hash = 0
for i in range(len(words)):
    for k in range(len(alist)):
        if words[i] == alist[k]:
            idx = k+1
    r = math.pow(31, i)
    hash += idx * r
print(int(hash))