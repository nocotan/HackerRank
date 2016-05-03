from itertools import permutations


s, k = input().split()

for el in sorted(list(permutations(s, int(k)))):
    print("".join(el))
