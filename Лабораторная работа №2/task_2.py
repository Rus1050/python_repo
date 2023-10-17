salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
i = 0
money_capital = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
for i in range(months):
    money_capital += salary - spend * (1 + increase) ** i
money_capital = abs(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
