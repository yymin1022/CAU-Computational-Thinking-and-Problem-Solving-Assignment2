import random

lottoList = []
lottoCount = []
lottoMax = [0, 0, 0, 0, 0, 0]

def lotto_generator():
    lottoNum = []
    randNum = random.randrange(1, 46)
    for g in range(6):
        while randNum in lottoNum:
            randNum = random.randrange(1, 46)
        lottoNum.append(randNum)
        lottoCount[lottoNum[g]-1] = lottoCount[lottoNum[g]-1] + 1
    lottoList.append(lottoNum)

for i in range(45):
    lottoCount.append(0)

for j in range(1000):
    lotto_generator()
    
''' 이 부분은 문제가 많으니 다시 짤 것
for k in range(6):
    for l in range(45):
        if k == 0:
            if lottoCount[lottoMax[k] - 1] < lottoCount[l]:
                lottoMax[k] = l + 1
        else:
            if lottoCount[lottoMax[k] - 1] < lottoCount[l] and lottoCount[l] < lottoCount[lottoMax[k - 1] - 1]:
                lottoMax[k] = l + 1

'''
print(lottoMax)