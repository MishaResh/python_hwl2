# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
m_lst = [8, 7, 5, 5, 4]
while True:
    try:
        n_num = input("Введите натуральное число : ")
        if n_num.isdigit and 0 < int(n_num):
            n_num = int(n_num)
        break
    except:
        print('ошибка ввода !!!')
if m_lst.count(n_num) != 0:
    m_lst.insert(m_lst.index(n_num) + 1, n_num)
elif m_lst.count(n_num) == 0 and n_num > m_lst[0]:
    m_lst.insert(0, n_num)
elif m_lst.count(n_num) == 0 and n_num < m_lst[len(m_lst) - 1]:
    m_lst.append(n_num)
else:
    for i in range(1, len(m_lst) - 1):
        if n_num > m_lst[i]:
            m_lst.insert(i, n_num)
            break
        elif m_lst[i + 1] < n_num < m_lst[i]:
            m_lst.insert(i + 1, n_num)
            break
print(m_lst)
