n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for c in range(0, commands):
    command = input()
    try:
        command, number = command.split()
        getattr(s, command)(int(number))
    except:
        getattr(s, command)()

print(sum(s))
