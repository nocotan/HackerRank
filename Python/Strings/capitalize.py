string = input().split(" ")

ans = ""
for s in string:
    ans += s.capitalize()
    ans += " "
    
print(ans.rstrip())