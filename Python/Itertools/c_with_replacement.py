from itertools import combinations_with_replacement

s, k = input().split()

for el in sorted(list(combinations_with_replacement(sorted(s), int(k)))):
    print("".join(el))
