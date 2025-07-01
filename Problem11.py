s = input()
res = ' '
for ch in s:
    if ch not in res:
        res += ch + str(s.count(ch))
print(res)
    
    