n = int(input())

for i in range(n):
    string = input()
    s1 = ""
    s2 = ""
    count = 0
    for c in list(string):
        if count % 2 == 0:
            s1 += c
        else:
            s2 += c
        count += 1

    print("%s %s" % (s1, s2))
