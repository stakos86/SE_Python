text = [
    'admin:superpassword',
    'user:usual:/password2',
    'kulhacker:ku:ef:lpasw0rd',
    'stevieballmer:12345',
    'zippy:pfoejxt09,g2'
]


def list_to_dict(text):
    result_dict = {}

    for item in text:
        print(item)
        key, value = item.split(':', 1)

        result_dict[key] = value

    return result_dict



if __name__ == '__main__':
    print(list_to_dict(text))
