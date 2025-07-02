import sys #Импорт модуля для работы с консолью

n = int(sys.argv[1]) #Ввод размера масства
m = int(sys.argv[2]) #Ввод размера шага

path = [] #Создание списка для сохранения пути
current_number = 1
visited = set() #Уже посещенные числа
while True:
    if current_number in visited: #Если число уже попадалось, то программа завершает цикл
        break
    visited.add(current_number)
    path.append(current_number)
    current_number = (current_number + m - 1) % n #Подсчет следующего числа
    if current_number == 0: #Переход на новый круг
        current_number = n

print("Final path is:", ''.join(str(num) for num in path))