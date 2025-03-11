import threading
import random

# Генерация набора из 10000 случайных чисел
numbers = [random.randint(1, 100000) for _ in range(10000)]

# Переменные для хранения результатов
max_value = None
min_value = None
sum_value = 0

# Блокировка для синхронизации доступа к общим ресурсам
lock = threading.Lock()

# Функция для нахождения максимума
def find_max(nums):
    global max_value
    local_max = max(nums)
    with lock:
        if max_value is None or local_max > max_value:
            max_value = local_max

# Функция для нахождения минимума
def find_min(nums):
    global min_value
    local_min = min(nums)
    with lock:
        if min_value is None or local_min < min_value:
            min_value = local_min

# Функция для нахождения суммы
def find_sum(nums):
    global sum_value
    local_sum = sum(nums)
    with lock:
        sum_value += local_sum

# Разделение набора чисел на части для обработки в потоках
def split_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]

# Количество потоков
num_threads = 4
chunks = split_list(numbers, num_threads)

# Создание и запуск потоков
threads = []
for chunk in chunks:
    t1 = threading.Thread(target=find_max, args=(chunk,))
    t2 = threading.Thread(target=find_min, args=(chunk,))
    t3 = threading.Thread(target=find_sum, args=(chunk,))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    t1.start()
    t2.start()
    t3.start()

# Ожидание завершения всех потоков
for t in threads:
    t.join()

# Вычисление среднего значения
average_value = sum_value / len(numbers)

# Вывод результатов
print(f"Максимум: {max_value}")
print(f"Минимум: {min_value}")
print(f"Среднее: {average_value}")