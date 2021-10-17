# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
seasons_name = {1:'весна',2:'лето',3:'осень',4: 'зима')
while True:
    month_n = input('Введите номер месяца :')
    if month_n.isdigit() and 0 < int(month_n) < 13:
        month_n = int(month_n)
        break
    print('ошибка ввода !!!')
if month_n in range(3,5):
    print(seasons_name.get(1))
elif month_n in range(6,8):
    print(seasons_name.get(2))
elif  month_n in range(9,11):
    print(seasons_name.get(3))
else:
    print(seasons_name.get(4))