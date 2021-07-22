s1=0
s2=990
s3=1390
Amount = int(input('Какое количество билетов Вы хотите приобрести \n'))
if Amount<=0:
    raise ValueError(f"Не может быть {Amount} посетителей")
Amount1 = int(input('Введите количество людей младше 18 лет: '))
if 0<Amount1 and Amount1>Amount:
    raise ValueError(f"Не может быть на {Amount1} человек, {Amount} билетов")
Amount2 = int(input('Введите количество людей от 18 до 25 лет: '))
if 0<Amount2 and (Amount1+Amount2)>Amount:
    raise ValueError(f"Не может быть на {Amount1+Amount2} человек, {Amount} билетов")
Amount3 = int(input('Введите количество людей старше 25 лет: '))
if Amount != (Amount1+Amount2+Amount3):
    raise ValueError("Общее количество людей не совпадает")
Total=(Amount1*s1+Amount2*s2+Amount3*s3)
if Amount>3:
    Total=Total*0.9
elif Amount<=3:
    Total=Total
print(f"Общая сумма =", Total, "рублей")



