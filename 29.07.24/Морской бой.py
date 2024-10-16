import random


# Инициализация игрового поля
def init_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]


# Отображение игрового поля
def print_board(board):
    for row in board:
        print(" | ".join(row))


# Размещение корабля на поле
def place_ship(board, ship_size):
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - ship_size)
            if all(board[row][col + i] == '~' for i in range(ship_size)):
                for i in range(ship_size):
                    board[row][col + i] = 'S'
                placed = True
        else:
            row = random.randint(0, len(board) - ship_size)
            col = random.randint(0, len(board[0]) - 1)
            if all(board[row + i][col] == '~' for i in range(ship_size)):
                for i in range(ship_size):
                    board[row + i][col] = 'S'
                placed = True


# Проверка попадания или промаха
def check_hit(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'  # Обозначаем попадание
        return True
    else:
        board[row][col] = 'O'  # Обозначаем промах
        return False


# Подсчет оставшихся кораблей
def count_ships(board):
    return sum(row.count('S') for row in board)


# Основной цикл игры
def game_loop(player_boards):
    current_player = 0
    while True:
        print(f"\nХод игрока {current_player + 1}:")
        print_board(player_boards[current_player])

        try:
            row = int(input("Введите номер строки (от 0 до 9): "))
            col = int(input("Введите номер столбца (от 0 до 9): "))
            if row < 0 or row > 9 or col < 0 or col > 9:
                raise ValueError("Неверный ввод")
        except ValueError as e:
            print(e)
            continue

        hit = check_hit(player_boards[(current_player + 1) % 2], row, col)
        if hit:
            print("Попадание!")
        else:
            print("Промах.")

        if count_ships(player_boards[(current_player + 1) % 2]) == 0:
            print(f"\nИгрок {current_player + 1} выиграл!")
            break

        current_player = (current_player + 1) % len(player_boards)


# Главная функция
def main():
    board_size = 10
    player_boards = [init_board(board_size), init_board(board_size)]

    # Размещаем корабли для каждого игрока
    for board in player_boards:
        for size in [3, 2, 2]:  # Пример размещения кораблей разных размеров
            place_ship(board, size)

    game_loop(player_boards)


if __name__ == "__main__":
    main()
