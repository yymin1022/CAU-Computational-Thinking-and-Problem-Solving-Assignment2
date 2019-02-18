lastWordList = []
lastWord = ""

while 1:
    inputWord = input("단어를 입력하세요 ")

    if len(inputWord) > 5:
        print("단어가 길어요.")
        continue
    elif len(inputWord) < 5:
        print("단어가 짧아요.")
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

    lastWord = inputWord
    lastWordList.append(lastWord)
    break

while 1:
    print(lastWord, end=" ")
    inputWord = input("끝말잇기? ")
    if len(inputWord) > 5:
        print("단어가 길어요.")
        continue
    elif len(inputWord) < 5:
        print("단어가 짧아요.")
        continue
    elif inputWord[0] != lastWord[-1]:
        print("입력한 단어의 첫 글자가 이전 단어의 끝 글자와 다릅니다.")
        continue

    for i in lastWordList:
        if inputWord == i:
            print("이미 입력한 단어입니다.")
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