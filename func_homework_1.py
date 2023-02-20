def info_manager(docs, direct = None):
    while True:
        availible_operatioins = ['p', 'l', 's', 'a', 'x']
        print('Добро пожаловать в каталог!\nСписок доступных операций:')
        print(' p - вывод фамилии и имени по номеру документа.')
        print(' s - вывод полки, на которой хранится документ.')
        print(' l - вывод всех хранящихся документов.')
        print(' a - добавление пользователя в базу.')
        print(' x - выход из программы.')

        operation = input('Пожалуйста, выберите из списка доступную операцию:\n')
        if operation not in availible_operatioins:
            print(cls())
            print('Такая операция не доступна!')
            continue
        else:
            if operation == 'x':
                print('Удачного дня!')
                break
            if operation == 'p':
                print(cls())
                number = input('Введите номер документа:\n')
                name = get_people(docs, str(number))
                print(name) if name else print('Номер не найден!')
                approved = input('Желаете продолжить работу?(нажмите "y", либо любую конпку для выхода из программы):\n')
                if approved == 'y': continue
                else:
                    print('Удачного дня!')
                    break
            if operation == 's':
                print(cls())
                number = input('Введите номер документа:\n')
                dir_name = get_shelf(direct, str(number))
                print(f'Документ {number} хранится на полке № {dir_name}.') if dir_name else print('Номер не найден!')
                approved = input('Желаете продолжить работу?(нажмите "y", либо любую конпку для выхода из программы):\n')
                if approved == 'y': continue
                else:
                    print('Удачного дня!')
                    break
            if operation == 'l':
                print(cls())
                print('Список записей:')
                print(get_list(docs))
                approved = input('Желаете продолжить работу?(нажмите "y", либо любую конпку для выхода из программы):\n')
                if approved == 'y': continue
                else:
                    print('Удачного дня!')
                    break
            if operation == 'a':
                print(cls())
                new_user = [input('Пожалуйста, введите тип документа:\n'),
                            input('Пожалуйста, введите номер документа:\n'), input('Пожалуйста, введите имя:\n'),
                            input('Пожалуйста, укажите желаемую полку для хранения:\n')]
                temp_list = set_doc(docs, directories, new_user)

                if temp_list:
                    docs = temp_list[0]
                    direct = temp_list[1]
                    print('Новые данные успешно добавлены!')
                else:
                    print(f'Данные не были добавлены, полка {new_user[3]} не существует.')

                approved = input('Желаете продолжить работу?(нажмите "y", либо любую конпку для выхода из программы):\n')
                if approved == 'y': continue
                else:
                    print('Удачного дня!')
                    break


def cls():
    return '\n' * 70

def get_people(doc, number):
    name = ''
    for i in doc:
        if number in i['number']: name = i['name']
    return name if name else None
def get_shelf(direct, document):
    for i, j in direct.items():
        return i if document in j else None

def get_list(doc):
    input_string = ''
    for i in doc:
        input_string += '{} "{}" "{}"'.format(i['type'], i['number'],  i['name']) + '\n'
    return input_string

def set_doc(doc, direct, new_user):
    doc_type, doc_number, doc_name, direct_number = new_user[0], new_user[1], new_user[2], new_user[3]
    if direct_number in direct:
        doc.append({'type': doc_type, 'number': doc_number, 'name': doc_name})
        direct[direct_number].append(doc_number)
        return doc, direct
    else:
        return None

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

info_manager(documents, directories)

