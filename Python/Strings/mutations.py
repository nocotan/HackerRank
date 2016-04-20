string = str(input())
line = input().split(" ")

n = int(line[0])
s = line[1]

print(string[:n] + s + string[n+1:])