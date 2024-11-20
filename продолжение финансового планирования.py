salary = 5000
spend = 6000
months = 10
increase = 0.03

total_spend = 0
for _ in range(months):
    total_spend += spend
    spend *= (1 + increase)

money_capital = total_spend - (salary * months)

rounded_money_capital = int(money_capital // 1) + (1 if money_capital % 1 > 0 else 0)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: ", rounded_money_capital)
