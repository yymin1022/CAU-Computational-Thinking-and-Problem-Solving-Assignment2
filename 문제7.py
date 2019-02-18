susic = "1+133-321412"
splited_by_plus = susic.split("+")

splited_done = []

for a in splited_by_plus :
    for b in a.split("-") :
        splited_done.append(b)


i = 0
val = int(splited_done[0])
for a in susic :
    if a=="+" :
        i = i+1
        val =val+int(splited_done[i])
    elif a=="-":
        i = i + 1
        val = val - int(splited_done[i])
    else:
        pass

print(val)