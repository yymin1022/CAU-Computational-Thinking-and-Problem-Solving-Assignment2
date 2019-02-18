from math import sin, cos, pi

for i in range(20):
    linePrint = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    linePrint[(int(10 + 10 * sin(i * pi / 10)))] = "*"
    linePrint[(int(10 + 10 * cos(i * pi / 10)))] = "+"
    linePrint[10] = "|"
    for j in linePrint:
        print(j, end="")
    print("")