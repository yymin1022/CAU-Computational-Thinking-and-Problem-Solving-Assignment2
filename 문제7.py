# 수식을 입력받고 이를 +를 기준으로 split하여 splitedPlus 리스트에 저장
inputSusic = input("수식을 입력하세요 : ")
splitedPlus = inputSusic.split("+")
splitDone = []

# for문을 이용해 +를 기준으로 나눠진 수식 조각들을
# 다시 -를 기준으로 split하여 splitDone으로 저장
for a in splitedPlus :
    for b in a.split("-") :
        splitDone.append(b)

i = 0
# 입력된 수식에서 +와 -를 검색하고 이의 위치에 맞게 수식을 계산하여 result에 int 정수형으로 저장
result = int(splitDone[0])
for c in inputSusic :
    if c == "+" :
        i = i + 1
        result = result + int(splitDone[i])
    elif c == "-":
        i = i + 1
        result = result - int(splitDone[i])
    else:
        pass

print("결과는 %d"%result)