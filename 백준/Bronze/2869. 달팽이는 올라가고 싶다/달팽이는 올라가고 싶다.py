a, b, v = map(int, input().split())

import math
days = (v-a)/(a-b) + 1
print(math.ceil(days))