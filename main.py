s = str(input("Введите строку (на русском языке): "))
count = 0
count2 = 0
glasnie = set("ауоиэыяюеё")
soglasnie = set("бвгджзйклмнпрмтфхцчшщ")
for letter in s:
    if letter in glasnie:
        count += 1
    elif letter in soglasnie:
        count2 += 1
print(f"Длина строки:{len(s)}, количество гласных букв: {count}, количество согласных букв:{count2}")
