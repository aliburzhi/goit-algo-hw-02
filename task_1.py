# import Queue
#
# Створити чергу заявок
# queue = Queue()
#
# Функція generate_request():
# Створити нову заявку
# Додати заявку до черги
#
# Функція process_request():
# Якщо черга не пуста:
# Видалити заявку з черги
# Обробити заявку
# Інакше:
# Вивести повідомлення, що черга пуста
#
# Головний цикл програми:
# Поки користувач не вийде з програми:
# Виконати generate_request() для створення нових заявок
# Виконати process_request() для обробки заявок

from queue import Queue

queue = Queue()
request_counter = 0
menu = "1 — створити заявку\n2 — обробити заявку\n3 — вийти\nОберіть варіант: "

def generate_request():
    global request_counter
    request_counter += 1
    new_request = f"Заявка {request_counter}"
    queue.put(new_request)

    print(f"{new_request} була створена і додана в чергу!")

def process_request():
    if queue.empty():
        print("Черга порожня та заявок не має!")
        return
    resolving_request = queue.get()
    print(f"{resolving_request} була взята в обробку!")

def main():
    while True:
        user_input = input(menu)
        if user_input == "1":
            generate_request()
        elif user_input == "2":
            process_request()
        elif user_input == "3":
            print("Закриття програми!")
            break
        else: print("Невірний вибір")


if __name__ == "__main__":
    main()