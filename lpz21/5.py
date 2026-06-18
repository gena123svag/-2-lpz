def atm_withdraw(amount, denominations=[5000, 2000, 1000, 500, 200, 100]):
    result = {}
    for d in denominations:
        count = amount // d
        if count:
            result[d] = count
            amount -= count * d
    return result

amount = 12300
notes = atm_withdraw(amount)
print("Купюры:")
for val, cnt in notes.items():
    print(f"{val} руб. × {cnt}")