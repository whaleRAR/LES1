"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. """

user_mounth = int(input("Введи номер месяца: "))
if user_mounth <= 12 and user_mounth >= 1:
    month_dict = {1: "январь",
                  2: "февраль",
                  3: "март",
                  4: "апрель",
                  5: "май",
                  6: "июнь",
                  7: "июль",
                  8: "август",
                  9: "сентябрь",
                  10: "октябрь",
                  11: "ноябрь",
                  12: "декабрь"}
else:
    print("!!!ошибка введи месяц от 1 до 12!!!")
month_season_list = ['зима', 'весна', 'лето', 'осень']
month_season_dict = {1: "зима",
                     2: "весна",
                     3: "лето",
                     4: "осень"}
if user_mounth == 12 or user_mounth == 2 or user_mounth == 1:
    print(month_season_dict.get(1))
    print(month_season_list[0])
elif user_mounth == 3 or user_mounth == 4 or user_mounth == 5:
    print(month_season_dict.get(2))
    print(month_season_list[1])
elif user_mounth == 6 or user_mounth == 7 or user_mounth == 8:
    print(month_season_dict.get(3))
    print(month_season_list[2])
elif user_mounth == 9 or user_mounth == 10 or user_mounth == 11:
    print(month_season_dict.get(4))
    print(month_season_list[3])

