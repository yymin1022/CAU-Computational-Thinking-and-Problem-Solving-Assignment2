lastWordList = []
lastWord = ""

# 첫번째 시작 단어를 입력받음
while 1:
    inputWord = input("단어를 입력하세요 ")

    # 단어의 길이가 5가 아닌 경우 경고문 출력
    if len(inputWord) > 5:
        print("단어가 길어요.")
        continue
    elif len(inputWord) < 5:
        print("단어가 짧아요.")
        continue

    dataFile = open("dict_test.TXT", "r")
    existWord = False
    isNoun = False
    # 사전에 존재하는 단어인지, 명사인지의 여부를 확인하는 반복문
    while True:
        line = dataFile.readline()
        if not line: break
        if line.split()[0] == inputWord:
            existWord = True
            if line.split(":")[1].find("n.") != -1:
                isNoun = True
    dataFile.close()

    if existWord == False:
        print("사전에 존재하지 않는 단어입니다.")
        continue

    if isNoun == False:
        print("명사가 아닙니다.")
        continue

    # 모든 조건에 부합하는 단어인 경우 첫번쨰 단어로 지정
    # 입력된 단어들을 기록하는 lastWordList에 저장하고
    # 다음 단어와의 이어지는지 여부 확인을 위해 lastWord String 변수에 저장
    lastWord = inputWord
    lastWordList.append(lastWord)
    break

while 1:
    # 첫 단어 입력때와 같은 알고리즘이나,
    # 이전 단어의 끝 글자와 입력한 단어의 첫 글자가 일치하는 지 여부,
    # 이전에 입력된 적이 없는 단어인지 여부를
    # 확인하는 조건문이 추가됨
    print(lastWord, end=" ")
    inputWord = input("끝말잇기? ")
    if len(inputWord) > 5:
        print("단어가 길어요.")
        continue
    elif len(inputWord) < 5:
        print("단어가 짧아요.")
        continue

    isUsed = False
    for i in lastWordList:
        if inputWord == i:
            isUsed = True
            continue

    if isUsed:
         print("이미 입력한 단어입니다.")
         continue

    if inputWord[0] != lastWord[-1]:
        print("입력한 단어의 첫 글자가 이전 단어의 끝 글자와 다릅니다.")
        continue
        
    dataFile = open("dict_test.TXT", "r")
    existWord = False
    isNoun = False
    while True:
        line = dataFile.readline()
        if not line: break
        if line.split()[0] == inputWord:
            existWord = True
            if line.split()[2][0] == "n":
                isNoun = True
    dataFile.close()

    if existWord == False:
        print("사전에 존재하지 않는 단어입니다.")
        continue

    if isNoun == False:
        print("명사가 아닙니다.")
        continue

    lastWordList.append(inputWord)
    lastWord = inputWord