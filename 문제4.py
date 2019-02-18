while 1:
    existWord = False
    inputWord = input("단어? ")
    dictFile = open("dict_test.TXT", "r")
    while 1:
        line = dictFile.readline()
        if not line: break
        lineWord = line.split()[0]
        if lineWord == inputWord:
            print(line.split()[2].strip())
            existWord = True
    dictFile.close()
    if existWord != True:
        print("사전에 존재하지 않는 단어입니다.")