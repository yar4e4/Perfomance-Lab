import sys #Импорт модуля для работы с консолью
import math #Импорт модуля для использования математических инструментов

#Проверка на наличие двух файлов
if len(sys.argv) != 3:
    print("Формат ввода: python3 task2 circle.txt points.txt")
    sys.exit(1)

#Открытие первого файла и считывание центра и радиуса
file = open(sys.argv[1], "r")
line1 = file.readline().strip()
x_c, y_c = line1.split()
x_c = float(x_c)
y_c = float(y_c)
r = float(file.readline().strip())
file.close()

#Открытие второго файла и получение точек
file = open(sys.argv[2], "r")
points = []
for line in file:
    line = line.strip()
    if line != "":
        x, y = line.split()
        points.append( (float(x), float(y)) )
file.close()

#Проверка каждой точки
for p in points:
    x = p[0]
    y = p[1]
    dist = math.sqrt((x - x_c)**2 + (y - y_c)**2)
#Проверка местонахождения точки
    if abs(dist - r) < 0.000000000001:
        print(0)
    elif dist < r:
        print(1)
    else:
        print(2)