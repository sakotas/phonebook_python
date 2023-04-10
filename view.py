import text_fields as txt


def main_menu() -> int:
    print('''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')

    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Введите число от 1 до 8')


def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def show_contacts(book: list[dict], message: str):
    if book:
        print('\n' + '-' * 63)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20} '
                  f'{contact.get("comment"):<20}')
        print('-' * 63 + '\n')

    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def confirm(message: str) -> bool:
    print()
    answer = input(message + ' y/n -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False


def search_name(case: int):
    if case == 5:
        return input(txt.search_case_5)
    if case == 7:
        return input(txt.search_case_7)
    if case == 6:
        return int(input(txt.search_case_6))


def deletion_success(is_deleted: bool):
    if is_deleted == True:
        print_info(txt.contact_deleted)
    else:
        print_info(txt.contact_not_found)


def ask_change_parameter() -> int:
    parameter = int(input(txt.contact_parameter_change))
    if 0 < parameter < 4:
        return parameter
    else:
        print_info(txt.invalid_parameter)
