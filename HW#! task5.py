"""Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или
убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

profit = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
if profit > costs:
    print("прибыль больше издержек")
elif profit < costs:
    print("прибыль меньше издержек")
elif profit == costs:
    print("прибыль равна издержкам")

rent = float( ( profit - costs ) / profit ) * 100
if profit > costs:
    print("рентабельность выручки: ", rent, "%")

number = int(input("Введите число сотрудников: "))
profit2 = float( ( profit - costs ) / number )
print("Прибыль фирмы в расчете на одного сотрудника: ", profit2)
