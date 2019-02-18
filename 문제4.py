while 1:
    #단어가 사전 내에 존재하는지 여부를 체크하기 위한 boolean 변수
    existWord = False
    inputWord = input("단어? ")
    dictFile = open("dict_test.TXT", "r")
    while 1:
        # 입력된 단어가 사전 내에 존재하는 지 확인하는 반복문
        # 사전을 모두 탐색한 뒤에는 break하여 반복문 종료
        line = dictFile.readline()
        if not line: break
        # 사전이 "영어 : 품사&뜻" 형식으로 저장되어 있으므로
        # :을 기준으로 사전의 각 줄을 split하면
        # index값이 0인 부분에 영단어+공백, 1인 부분에 공백+품사&뜻 이 저장됨
        # rstrip()과 lstrip()함수로 각각의 오른쪽 또는 왼쪽의 공백을 제거하고
        # 입력된 단어와 읽어낸 사전 줄의 영단어가 일치하는 경우
        # 해당하는 단어의 뜻 부분을 출력함
        lineWord = line.split(":")[0].rstrip()
        if lineWord == inputWord:
            print(line.replace(" : ", " "))
            existWord = True
    dictFile.close()
    if existWord != True:
        print("사전에 존재하지 않는 단어입니다.")