import sys      #Модуль для работы с консолью
import json     #Модуль для работы с JSON файлами

def fill_values(test, values_map):
    test_id = test.get('id')  #Получаем id текущего теста
    if test_id in values_map:
        test['value'] = values_map[test_id]  #Записываем это значение в поле "value"
    else:
        test['value'] = ""  #Если значения нет, ставим пустую строку

    #Проверка, есть ли вложенные тесты (ключ 'values')
    if 'values' in test:
        for t in test['values']:
            fill_values(t, values_map)

def main():
    #Проверка, что при запуске передали ровно 3 аргумента (имена файлов)
    if len(sys.argv) != 4:
        print("Передано неверное количество файлов")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    f = open(values_file, 'r', encoding='utf-8')
    values_data = json.load(f)  #Загрузка данных из JSON в словарь
    f.close()

    #Словарь для поиска значений по id
    values_map = {}
    for item in values_data['values']:
        values_map[item['id']] = item['value']

    f = open(tests_file, 'r', encoding='utf-8')
    tests_data = json.load(f)  #Загрузка структуры тестов
    f.close()

    #Для каждого теста в корневом списке запускаем заполнение значений
    for test in tests_data['tests']:
        fill_values(test, values_map)  #Заполнение поля "value" через рекурсию

    f = open(report_file, 'w', encoding='utf-8')
    #Запись обновленных данных в JSON
    json.dump(tests_data, f, indent=2, ensure_ascii=False)
    f.close()

if __name__ == "__main__":
    main()