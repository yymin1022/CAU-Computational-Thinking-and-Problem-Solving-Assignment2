import random

lottoList = []
lottoCount = []
lottoCountSort = []
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

print(lottoCount)

for k in range(6):
    for l in range(45):
        if k == 0:
            if lottoCount[l] > lottoCount[lottoMax[k] - 1]:
                lottoMax[k] = l + 1
        else:
            if lottoCount[l] > lottoCount[lottoMax[k] - 1] and lottoCount[l] <= lottoCount[lottoMax[k - 1] - 1]:
               if (l + 1) not in lottoMax:
                    lottoMax[k] = l + 1

print(lottoMax)