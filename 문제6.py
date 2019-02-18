scoreFile = open("SCORE.csv", "r")

listStudents = []
listSums = []

while True:
    listScore = [0, 0, 0, 0, 0, 1]
    currentLine = scoreFile.readline().replace("\n", "")
    if not currentLine: break
    listScore[0] = int(currentLine.split(",")[0])
    listScore[1] = int(currentLine.split(",")[1])
    listScore[2] = int(currentLine.split(",")[2])
    listScore[3] = int(currentLine.split(",")[3])
    listScore[4] = listScore[1] + listScore[2] + listScore[3]
    listSums.append(listScore[4])

    listStudents.append(listScore)

listSums.sort()
listSums.reverse()

for i in range(len(listSums)):
    for j in listStudents:
        if listSums[i] == j[4]:
            j[5] = i + 1

print(listStudents)