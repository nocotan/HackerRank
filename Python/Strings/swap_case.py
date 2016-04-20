string = str(input())
ans = ""

for s in string:
    if(s.islower()):
        ans += s.upper()
    else:
        ans += s.lower()
        
print(ans)