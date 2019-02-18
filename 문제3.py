import random

lottoList = [] # 1000회의 로또 진행 후 각 결과가 저장될 리스트
lottoCount = [] # 1부터 45까지의 값이 각각 나온 횟수가 저장될 리스트
lottoCountSort = [] # lottoCount 리스트가 Sort되어 저장될 리스트
lottoMax = [0, 0, 0, 0, 0, 0] # 가장 빈도가 높은 6개의 숫자가 저장될 리스트

def lotto_generator():
    lottoNum = []
    # 번호 추첨을 6번 반복
    for g in range(6):
        # 1부터 45 사이의 범위에서 정수 난수를 생성
        randNum = random.randrange(1, 46)
        # 이미 뽑힌 난수인지 확인하고, 중복된 경우 다시 난수 생성
        while randNum in lottoNum:
            randNum = random.randrange(1, 46)
        # 생성된 난수를 lottoNum 리스트에 append
        lottoNum.append(randNum)
        # 난수가 출현된 횟수를 1 증가시킴 : 생성된 난수에서 1을 뺀 값이 리스트의 index 값
        lottoCount[lottoNum[g]-1] = lottoCount[lottoNum[g]-1] + 1
    # 생성된 6개 번호가 저장된 리스트인 lottoNum을 lottoList 리스트에 element로 추가
    lottoList.append(lottoNum)

# 각 숫자가 출현된 빈도를 기록하기 위한 리스트인 lottoCount 리스트에 0을 45개 추가하여
# 이후에 숫자가 출현될 때 마다 1씩 더하도록 해줌
for i in range(45):
    lottoCount.append(0)

# 번호 1세트(6개)를 추첨하는 함수인 lotto_generator() 함수를 1000회 실행
for j in range(1000):
    lotto_generator()

# lottoCount 리스트에 저장된 각 숫자의 빈도를 출력
# index값에 1을 더하면 해당 숫자가 구해짐 : index 0에 저장된 값은 1이 출현한 횟수
for count in range(45):
    print("%d가 나온 횟수는 %d회 입니다."%((count+1), lottoCount[count]))

# lottoCount 리스트에서 가장 큰 값 6개를 추출하는 for문
# lottoCount에 저장된 값은 빈도 수 이므로
# 가장 큰 값의 index에 1을 더한 값을 lottoMax 리스트에 저장
for k in range(6):
    for l in range(45):
        if k == 0:
            if lottoCount[l] > lottoCount[lottoMax[k] - 1]:
                lottoMax[k] = l + 1
        else:
            if lottoCount[l] > lottoCount[lottoMax[k] - 1] and lottoCount[l] <= lottoCount[lottoMax[k - 1] - 1]:
               if (l + 1) not in lottoMax:
                    lottoMax[k] = l + 1

# lottoMax 리스트를 이 주의 추천 번호로 출력
print("이 주의 추천 로또 번호는", lottoMax, "입니다.")