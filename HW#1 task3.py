"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

print("давай преобразуем твоё число в формат n + nn + nnn")
num = int(input("Введи число"))
total = ( num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num)))
print("Сумма чисел n + nn + nnn", total)