#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки
# типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка
# можно не запрашивать у пользователя, а указать явно, в программе.

var_list = [1, 2.354, 'try', True, (1, 2, 3, 't', 0), {1, 2, 3, 't', 0}, [1, 2, 3, 't', 0]]
for x in var_list:
    print(type(x))
