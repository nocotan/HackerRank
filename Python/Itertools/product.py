from itertools import product


list_a = list(map(int, input().strip().split()))
list_b = list(map(int, input().strip().split()))
for i in list(product(list_a, list_b)):
    print(i, end=" ")
