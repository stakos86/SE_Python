import random

from funcs import adding, subtracting, multiplying

OPERATIONS = {
    0: {"symbol": "+", "func": adding},
    1: {"symbol": "-", "func": subtracting},
    2: {"symbol": "*", "func": multiplying}
}


def generate_numbers(level: int) -> tuple[int, int]:
    if level == 1:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    elif level == 3:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
    else:
        raise ValueError("Уровень должен быть между 1 и 3")
    return a, b


def check_answer(sample: int, result: int) -> tuple[int, int]:
    pravilno = 0
    nepravilno = 0
    if sample == result:
        print("Правильно")
        pravilno += 1
    else:
        print("Неправильно")
        nepravilno += 1
    return pravilno, nepravilno


def question(index: int, limit: int, level: int) -> tuple[int, int]:
    pravilno = 0
    nepravilno = 0
    a, b = generate_numbers(level)
    choice: int = random.randint(0, 2)
    print(f"\n[{index + 1}/{limit}] {a} {OPERATIONS[choice]['symbol']} {b} = ", end="")
    result: int = int(input())
    pravilno, nepravilno = check_answer(result, OPERATIONS[choice]['func'](a, b))
    return pravilno, nepravilno


def session(limit: int, level: int) -> tuple[int, int]:
    pravilno = 0
    nepravilno = 0
    for i in range(limit):
        p, n = question(i, limit, level)
        pravilno += p
        nepravilno += n
    return pravilno, nepravilno


def calc_final_mark(pravilno: int, limit: int) -> None:
    if pravilno / limit == 1:
        print('Оценка 5')
    elif pravilno / limit >= 0.8:
        print('Оценка 4')
    elif pravilno / limit >= 0.6:
        print('Оценка 3')
    else:
        print('Оценка 2')


def main() -> None:
    name = input("Введите ваше имя: ")
    print(f"Добрый день, {name}\nДобро пожаловать в тренажёр счёта")

    level = int(
        input("Выберите уровень сложности (1 - однозначные числа, 2 - двузначные числа, 3 - трехзначные числа): "))
    limit = 10
    pravilno, nepravilno = session(limit, level)
    print('Правильно:', pravilno)
    print('Неправильно:', nepravilno)
    calc_final_mark(pravilno, limit)


if __name__ == '__main__':
    main()
