import sys #Модуль для работы с консолью

#Проверка что при запуске был передан нужный файл
if len(sys.argv) < 2:
    print("Неверный ввод данных")
    exit(1)

#Считывание файла, исключение пробелов и переносов
file = open(sys.argv[1], 'r')
numbers = [int(line.strip()) for line in file if line.strip()]
file.close()

#Поиск среднего числа
numbers.sort()
median_num = numbers[len(numbers) // 2]

#Общий подсчет шагов через медиану
steps = 0
for num in numbers:
    steps += abs(num - median_num)
print(steps)
