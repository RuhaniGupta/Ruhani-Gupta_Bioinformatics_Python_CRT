Cartoons=["Chota bheem","oggy","tom & jerry","Doremon"]
print(Cartoons)
print("After appending:")
Cartoons.append('Shinchan')
print(Cartoons)
Cartoons.insert(0,'Benten')
print(Cartoons)
Cartoons.pop()
print(Cartoons)
Cartoons.pop(0)
print(Cartoons)

#
Cartoons=["Chota bheem","oggy","tom & jerry","Doremon"]
print(Cartoons)
Cartoons.remove('oggy')
print(Cartoons)
print(Cartoons.index('tom & jerry'))
Cartoons.reverse()
print(Cartoons)

#Reverse a list without using reverse function.
Num=[11,22,33,44,55,66,77,88,99]
print(Num[0:])
print(Num[1:4+1])
print(Num[::1])
print(Num[::2])
print(Num[::1])

#reverse a list using extend function.
Prog_lang=['C','C++','Java','Python','Go-Lang']
print(Prog_lang)
Front_End=['HTML','CSS','JAVASCRIPT','REACT JS']
print(Front_End)
Prog_lang.extend(Front_End)
print(Prog_lang)
print(Prog_lang.count('HTML'))
