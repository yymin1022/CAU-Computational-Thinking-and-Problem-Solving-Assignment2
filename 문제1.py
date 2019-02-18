inputStr = input("문장을 입력하세요 : ")
inputStrList = inputStr.split()

for i in inputStrList:
    if i.count("입니다"):
        print(i[:i.find("입니다")])
        break
    elif i.count("이라고"):
        print(i[:i.find("이라고")])
        break
