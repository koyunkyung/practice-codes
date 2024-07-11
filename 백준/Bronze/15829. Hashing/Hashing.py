L = int(input())
words = list(input())
hash = 0

for i in range(L):
    hash += ((ord(words[i])-96) * (31 ** i))
print(hash % 1234567891)