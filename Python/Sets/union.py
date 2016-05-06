n_en = int(input())
s_en = set([int(x) for x in input().split()])
n_fre = int(input())
s_fre = set([int(x) for x in input().split()])

print(len(s_en.union(s_fre)))
