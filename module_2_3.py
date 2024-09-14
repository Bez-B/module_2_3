my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

print('Вариат решения 1')  # В даном  варианте не требуется оператор continue
x = 0
while x < len(my_list) - 1:
    if my_list[x] < 0:
        break
    elif my_list[x] > 0:
        print(my_list[x])
    x += 1

print()  # Для большего удобства чтения результата
print('Вариант решения 2')  # С использованием оператора continue

x = 0
while x < len(my_list) - 1:
    if my_list[x] > 0:
        print(my_list[x])
    elif my_list[x] == 0:
        x += 1
        continue
    elif my_list[x] < 0:
        break
    x += 1
# Конец задания
