phone_book = []
start_phone_book = []
PATH = 'phone_book.txt'


def get_pb():
    global phone_book
    return phone_book


def load_file():
    global phone_book, start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book = phone_book.copy()


def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)


def search_contact(search_name: str) -> list[dict]:
    global phone_book
    result_list = []
    for contact in phone_book:
        if search_name in contact["name"]:
            result_list.append(contact)
    return result_list


def edit_contact(index_to_delete: int, parameter_to_change: int, new_value: str):
    global phone_book
    if parameter_to_change == 1:
        phone_book[index_to_delete]['name'] = new_value
    if parameter_to_change == 2:
        phone_book[index_to_delete]['phone'] = new_value
    if parameter_to_change == 3:
        phone_book[index_to_delete]['comment'] = new_value


def delete_contact(search_name) -> bool:
    global phone_book
    for i in range(len(phone_book)):
        if search_name == phone_book[i]["name"]:
            del phone_book[i]
            print(phone_book)
            return True


def delete_contact_by_index(list_index: int):
    global phone_book
    del phone_book[list_index]


def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True
