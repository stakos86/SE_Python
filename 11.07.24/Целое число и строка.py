integer_input = input("Введите целое число: ")
integer_value = int(integer_input)
float_input = input("Введите вещественное число: ")
float_value = float(float_input)
string_input = input("Введите строку: ")
integer_type = type(integer_value)
float_type = type(float_value)
string_type = type(string_input)
print(f"Целое число: {integer_value}, его тип - {integer_type}")
print(f"Вещественное число: {float_value}, его тип - {float_type}")
print(f"Строка: {string_input}, ее тип - {string_type}")