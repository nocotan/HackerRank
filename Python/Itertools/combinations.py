from itertools import combinations


s, k = input().split()
s = "".join(sorted(s))

for i in range(1, int(k) + 1):
    ls = list(combinations(s, i))
    for el in ls:
        print(''.join(el))
