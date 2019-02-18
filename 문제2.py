from math import sin, cos, pi

for i in range(20):
    # 21개의 index를 갖는 리스트 선언
    linePrint = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", " "]
    # sin 값과 cos 값을 계산해 각 값의 범위가 0 ~ 20 사이가 되도록 식 조절 후
    # 계산된 값을 int 정수형으로 변환해 해당 index의 리스트에 저장
    linePrint[(int(10 + 10 * sin(i * pi / 10)))] = "*"
    linePrint[(int(10 + 10 * cos(i * pi / 10)))] = "+"
    # 21개의 index 중 중앙값인 index 10 값에 기준선을 출력하도록 지정
    linePrint[10] = "|"
    # 리스트의 각 요소를 출력하도록 for 반복문 이용
    for j in linePrint:
        print(j, end="")
    print("")