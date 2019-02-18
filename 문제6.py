scoreFile = open("SCORE.csv", "r")

listStudents = []
listSums = []

# CSV 파일로부터 각 학생의 성적을 읽어들이고
# 학번, 국어점수, 영어점수, 수학점수, 총점 의 데이터를
#listScore 리스트에 저장
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

    # 완성된 학생 한명의 listSCore 리스트를 listStudent 리스트의 element로 추가
    listStudents.append(listScore)

# 각 학생의 총점이 저장된 listSum 리스트를 내림차순으로 정렬
listSums.sort()
listSums.reverse()

# 정렬된 listSum 함수에 따라 각 학생의 석차를 지정
# 점수가 낮은 학생일수록 기본 석차값인 1로부터 1씩 증가시킴
for i in range(len(listSums)):
    for j in listStudents:
        if listSums[i] == j[4]:
            j[5] = i + 1
            
print("   번호    국어  영어  수학  총점   석차")
for k in listStudents:
    for l in range(6):
        print("%3d"%k[l], end="   ")
    print("")