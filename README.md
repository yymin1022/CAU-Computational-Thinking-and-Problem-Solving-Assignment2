﻿# 컴퓨팅적 사고와 문제해결 : 과제 2
## 중앙대학교 소프트웨어학부 19학번 유용민(391040342)
## 이 자료를 이용해 자신의 과제로 변형하여 제출하는 일이 없도록 해주시기 바랍니다.

> 문제 1 : 자기소개서 이름 추출 / [소스코드 열기](문제1.py)
![Code_Preview](/Images/문제1.jpg)
![Code_Preview](/Images/결과1.png)
문제에서 입력되는 문장은 “저는 홍길동이라고 합니다..”, “저는 심청입니다”와
같은 형태로 제한되어 있습니다.
이에 따라 먼저 입력된 문장을 공백 단위로 쪼갠 뒤 각 부분에 “입니다” 또는
“이라고”가 포함되는지의 여부를 확인합니다.
“입니다” 또는 “이라고”가 포함된 경우에는 해당 부분에서 “입니다”와 “이라고”의
앞 까지를 slice 하여 이를 이름으로 출력합니다.

> 문제 2 : 사인코사인 그래프 그리기 / [소스코드 열기](문제2.py)
![Code_Preview](/Images/문제2.jpg)
![Code_Preview](/Images/결과2.png)
21 개의 칸으로 이루어진 리스트에 0 부터 360 도 까지의 사인 값, 코사인 값을
일정한 간격으로 20 개 구해 리스트의 요소로 저장합니다.
리스트의 11 번째 요소로는 |를 저장해주어 그래프의 기준선이 되도록 합니다.

> 문제 3 : 로또 번호 생성기 / [소스코드 열기](문제3.py)
![Code_Preview](/Images/문제3.jpg)
![Code_Preview](/Images/결과3.png)
lotto_generator() 함수는 실행될 때 마다 1~45 사이의 범위에서 6 개의 난수를
중복되지 않도록 생성해 이를 리스트로 저장합니다.
이 함수를 1000 번 실행하면 lottoList 리스트에 1000 개의 로또번호 세트가
저장됩니다.
이후에는 각 숫자가 출현한 횟수를 구해 lottoCount 리스트에 저장하고, 이
리스트에서 가장 많이 출현한 6 개의 수를 구해 이 주의 추천 번호로
출력해줍니다.

> 문제 4 : 전자사전 만들기 / [소스코드 열기](문제4.py)
![Code_Preview](/Images/문제4.jpg)
![Code_Preview](/Images/결과4.png)
먼저 단어를 입력 받은 뒤 해당 단어가 사전에 존재하는지 확인합니다. 확인된
이후에는 해당 단어의 뜻 부분을 출력해줍니다

> 문제 5 : 끝말 잇기 / [소스코드 열기](문제5.py)
![Code_Preview](/Images/문제5.jpg)
![Code_Preview](/Images/결과5.png)
입력된 단어를 시작으로 끝말잇기를 진행합니다.
사전에 존재하는 단어인지, 명사인지, 5 글자인지의 여부를 확인한 후 다음 단어를
입력 받도록 합니다.
두번째 단어부터는 이전에 입력된 기록이 없는 단어인지를 추가로 확인하는
조건문이 있습니다.

> 문제 6 : 성적 처리하기 / [소스코드 열기](문제6.py)
![Code_Preview](/Images/문제6.jpg)
![Code_Preview](/Images/결과6.png)
CSV 파일을 읽어 들이고 이를 ,(Comma)에 따라 잘라낸 뒤 리스트화 하고, 총점에
따라 석차를 지정해주는 코드입니다.

> 문제 7 : 수식 계산기 / [소스코드 열기](문제7.py)
![Code_Preview](/Images/문제7.jpg)
![Code_Preview](/Images/결과7.png)
수식을 입력 받고 이를 +와 -에 따라 split 한 뒤 순서에 맞게 수식을 계산하는
코드입니다.
