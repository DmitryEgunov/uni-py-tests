documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
    }

def search_by_number(document):
    number_doc = input('Введите номер документа :')
    for item in document:
        num = item['number']
        full_name = item['name']
        if number_doc == num:
            return (f'Владелец документа :{full_name}')
    if number_doc not in document:
        return 'Документ не найден в базе'

def shelf_search(shelf): 
    number_doc = input('Для поиска на полке ведите номер документа :')
    for key, val in shelf.items():
        if number_doc in val:
            return (f'Документ находится на полке :{key}')
    if number_doc not in val:
        return 'Документ не найден в базе'

def disp_list_docs(document):
    all_docs_list = []
    for item in document:
        type_doc = item['type']
        number_doc = item['number']
        name = item['name']
        all_docs_list.append(f'{type_doc} "{number_doc}" "{name}"')
    return all_docs_list

def add_doc(document, shelf):
    # print('Добавляем новый документ.')
    type_doc = input('Введите тип документа :')
    number_doc = input('Введите номер документа :')
    name = input('Введите имя владельца документа :')
    shelf_doc = input('На какую полку положить документ :')
    new_doc = {'type': type_doc, 'number': number_doc, 'name': name}
    document.append(new_doc)
    key = str(len(shelf))
    if shelf_doc <= key:
        shelf[shelf_doc].append(number_doc)
        return shelf_doc, new_doc

    if shelf_doc > key:
        return 'Такой полки не существует.'

def disp_list_shelf(document):
    for item in document:
        num_shelf = item
        data_shelf = document[item]
        print(f'{num_shelf}: {data_shelf}')

def deleting_doc(document, shelf):
    number_doc = str(input('Введите номер документа :'))
    i = 0
    for item in document:
        num = item['number']
        if number_doc == num:
                document.pop(i)
        i += 1
    if number_doc != num:
        return ('Документ не существует.')
            
    for item in shelf:   
        shelf_list = shelf[item]
        for num in shelf_list:
            if number_doc == num:
                j = shelf_list.index(num)
                shelf_list.pop(j)
                return ('')

def moving_doc(shelf):
    number_doc = str(input('Введите номер документа :'))
    shelf_doc = str(input('Введите целевую полку :'))
    len_shelf = str(len(shelf))
    all_docs = []
    for key, val in shelf.items():
        for item in val:
            if number_doc == item:
                all_docs.append(item)
                if shelf_doc <= len_shelf:
                    val.pop(val.index(item))
                    shelf[shelf_doc].append(number_doc)
                    return ('Документ перемещен.')
                if shelf_doc > len_shelf:
                    return ('Такой полки не существует.')
    if number_doc not in all_docs:
        return ('Документ не найден')

def add_shelf(shelf):
    num_shelf = str(input('Введите номер новой полки :'))
    len_shelf = str(len(shelf))
    if num_shelf not in shelf:
        shelf[num_shelf] = []
        return (f'Добавлена новая полка - {num_shelf}.')
    if num_shelf <= len_shelf:
        return ('Данная полка уже существует.')


def main():
    print("""Список команд : 
          1 - Поиск владельца документа по номеру 
          2 - Найти документ на полке 
          3 - Вывести на экран список всех документов 
          4 - Добавить документ 
          5 - Удалить документа
          6 - Переместить документ на другую полку
          7 - Добавить полку для документов
          q - Выход из программы""")
    print()
    while True:
        user_input = input('Введите номер команды :')
        if user_input == '1':
            print(search_by_number(documents))
            print()
        elif user_input == '2':
            print(shelf_search(directories))
            print()
        elif user_input == '3':
            print(disp_list_docs(documents))
            print()
        elif user_input == '4':
            add_doc(documents, directories)
            print()
            print(disp_list_docs(documents))
            print()
            print(disp_list_shelf(directories))
            print()
        elif user_input == '5':
            print(deleting_doc(documents, directories))
            print()
            print(disp_list_docs(documents))
            print()
            disp_list_shelf(directories)
            print()
        elif user_input == '6':
            print(moving_doc(directories))
            print()
            disp_list_shelf(directories)
            print()
        elif user_input == '7':
            print(add_shelf(directories))
            print()
            disp_list_shelf(directories)
            print()
        elif user_input == 'q':
            break

if __name__=='__main__':
    main()


