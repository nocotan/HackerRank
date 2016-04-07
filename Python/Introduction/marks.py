n = int(input())
dic = {}
for i in range(0, n):
    line = input().split()
    name = line[0]
    a = float(line[1])
    b = float(line[2])
    c = float(line[3])
    ave = (a + b + c) / 3
    dic[name] = ave

key = str(input())
print("%.2f" % dic[key])
