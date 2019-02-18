# 사용자로부터 문장을 입력받고 이를 공백으로 구분하여 리스트 형식으로 저장합니다.
inputStr = input("문장을 입력하세요 : ")
inputStrList = inputStr.split()

for i in inputStrList:
    # 주어진 자기소개 문장 형식은 "저는 홍길동입니다.", "저는 홍길동이라고 합니다"와 같은 형식이므로
    # split()으로 분리된 구절 중 "입니다" 또는 "이라고" 가 포함된 구절을 찾아
    # 해당 구절에서 "입니다" 또는 "이라고" 의 앞부분까지를 이름으로 간주하고 이를 slice하여 출력함
    if i.count("입니다"):
        print(i[:i.find("입니다")])
        break
    elif i.count("이라고"):
        print(i[:i.find("이라고")])
        break
