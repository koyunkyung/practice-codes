S = list(input())
from string import ascii_lowercase
list = list(ascii_lowercase)

for i in list:
    if i in S:
        print(S.index(i), end=" ")
    else:
        print(-1, end=" ")