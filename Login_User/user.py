from files import read_file, FILENAME, write_file


def list_to_dict(text):
    result_dict = {}

    for item in text:
        print(item)
        key, value = item.split(':', 1)

        result_dict[key] = value

    return result_dict


# print(list_to_dict(text))


def user_request() -> None:
    users: list[str] = read_file(FILENAME)
    for _ in range(5):
        user_choice = input("Введите логин: ")
        if user_choice in users:
            print(f"Существует логин")
            break
        else:
            print("Не существует логин")
            print('Запомнить юзера? Y/N')
            question = input()
            if question == 'Y':
                users.append(user_choice)
                write_file(FILENAME, user_choice)
            if question == 'N':
                break
    else:
        print('что-то пошло не так')


if __name__ == "__main__":
    user_request()
