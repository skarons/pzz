# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия»
# добавить фразу «Министерства образования Ростовской области»,
# посчитать количество произведённых добавлений.
# Определить, сколько номеров телефонов заканчивается на «03» и «50».
# Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re

# Чтение файла
with open('hotline.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Добавление фразы после "Горячая линия"
new_text, count_additions = re.subn(
    r'Горячая линия',
    'Горячая линия Министерства образования Ростовской области',
    text
)

print(f'Количество произведённых добавлений: {count_additions}')

# Поиск телефонных номеров
phone_pattern = r'(?:\+?\d[\d\s\-\(\)]{5,}\d)'
phones = re.findall(phone_pattern, text)

# Подсчёт номеров, заканчивающихся на 03 и 50
count_03 = 0
count_50 = 0

for phone in phones:
    digits = re.sub(r'\D', '', phone)

    if digits.endswith('03'):
        count_03 += 1

    if digits.endswith('50'):
        count_50 += 1

print(f'Количество номеров, заканчивающихся на 03: {count_03}')
print(f'Количество номеров, заканчивающихся на 50: {count_50}')

# Поиск телефонов горячих линий, связанных с ЕГЭ/ГИА
ege_gia_pattern = (
    r'(?i)(?:ЕГЭ|ГИА).*?('
    r'(?:\+?\d[\d\s\-\(\)]{5,}\d)'
    r')'
)

ege_gia_phones = re.findall(
    ege_gia_pattern,
    text,
    flags=re.DOTALL
)

print('\nНомера телефонов горячих линий, связанных с ЕГЭ/ГИА:')

if ege_gia_phones:
    for phone in ege_gia_phones:
        print(phone.strip())
else:
    print('Не найдены.')

# Сохранение изменённого текста в новый файл
with open('hotline_result.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)

print('\nИзменённый текст сохранён в файл hotline_result.txt')
