# Практическое занятие № 14. Вариант 21. Задание 1.
# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу.
# Прототип: окно браузера с формой "Форма регистрации пользователя",
# содержащей поля: Ваше имя, Пароль, Возраст, Пол (Мужской/Женский),
# Ваши увлечения (Музыка/Видео/Рисование), Ваша страна, Ваш город,
# Кратко о себе, поле для решения примера, кнопки "Отменить ввод"
# и "Данные подтверждаю".

import tkinter as tk
from tkinter import ttk, messagebox
import random

# Создаем главное окно приложения
root = tk.Tk()
root.title('Обработка формы')
root.geometry('520x560')
root.resizable(False, False)
root.configure(bg='white')

# Заголовок формы
title_label = tk.Label(
    root,
    text='Форма регистрации пользователя',
    font=('Arial', 13, 'bold'),
    bg='white'
)
title_label.pack(pady=(15, 10))

# Основная рамка с границей, в которой расположены все элементы формы
main_frame = tk.Frame(root, bg='white', highlightbackground='gray',
                       highlightthickness=1)
main_frame.pack(padx=20, fill='both', expand=True)

# Поле "Ваше имя"
name_frame = tk.Frame(main_frame, bg='white')
name_frame.pack(fill='x', padx=15, pady=(15, 5))
tk.Label(name_frame, text='Ваше имя:', bg='white', width=15,
         anchor='w').pack(side='left')
name_entry = tk.Entry(name_frame, bg='#d9d9d9')
name_entry.pack(side='left', fill='x', expand=True)

# Поле "Пароль"
password_frame = tk.Frame(main_frame, bg='white')
password_frame.pack(fill='x', padx=15, pady=5)
tk.Label(password_frame, text='Пароль:', bg='white', width=15,
         anchor='w').pack(side='left')
password_entry = tk.Entry(password_frame, bg='#d9d9d9', show='*')
password_entry.pack(side='left', fill='x', expand=True)

# Поле "Возраст"
age_frame = tk.Frame(main_frame, bg='white')
age_frame.pack(fill='x', padx=15, pady=5)
tk.Label(age_frame, text='Возраст:', bg='white', width=15,
         anchor='w').pack(side='left')
age_entry = tk.Entry(age_frame, bg='#d9d9d9')
age_entry.pack(side='left', fill='x', expand=True)

# Поле "Пол" с переключателями (radiobutton)
gender_frame = tk.Frame(main_frame, bg='white')
gender_frame.pack(fill='x', padx=15, pady=5)
tk.Label(gender_frame, text='Пол:', bg='white', width=15,
         anchor='w').pack(side='left')
gender_var = tk.StringVar(value='')
tk.Radiobutton(gender_frame, text='Мужской', variable=gender_var,
               value='Мужской', bg='white').pack(side='left', padx=(0, 60))
tk.Radiobutton(gender_frame, text='Женский', variable=gender_var,
               value='Женский', bg='white').pack(side='left')

# Поле "Ваши увлечения" с флажками (checkbutton)
hobby_frame = tk.Frame(main_frame, bg='white')
hobby_frame.pack(fill='x', padx=15, pady=5)
tk.Label(hobby_frame, text='Ваши увлечения:', bg='white', width=15,
         anchor='w').pack(side='left')
music_var = tk.IntVar()
video_var = tk.IntVar()
draw_var = tk.IntVar()
tk.Checkbutton(hobby_frame, text='Музыка', variable=music_var,
               bg='white').pack(side='left')
tk.Checkbutton(hobby_frame, text='Видео', variable=video_var,
               bg='white').pack(side='left', padx=(15, 0))
tk.Checkbutton(hobby_frame, text='Рисование', variable=draw_var,
               bg='white').pack(side='left', padx=(15, 0))

# Поле "Ваша страна" с выпадающим списком (combobox)
country_frame = tk.Frame(main_frame, bg='white')
country_frame.pack(fill='x', padx=15, pady=5)
tk.Label(country_frame, text='Ваша страна:', bg='white', width=15,
         anchor='w').pack(side='left')
country_combo = ttk.Combobox(
    country_frame,
    values=['Россия', 'Беларусь', 'Казахстан', 'Армения'],
    state='readonly'
)
country_combo.pack(side='left', fill='x', expand=True)

# Поле "Ваш город" с выпадающим списком (combobox)
city_frame = tk.Frame(main_frame, bg='white')
city_frame.pack(fill='x', padx=15, pady=5)
tk.Label(city_frame, text='Ваш город:', bg='white', width=15,
         anchor='w').pack(side='left')
city_combo = ttk.Combobox(
    city_frame,
    values=['Ростов-на-Дону', 'Москва', 'Санкт-Петербург', 'Краснодар'],
    state='readonly'
)
city_combo.pack(side='left', fill='x', expand=True)

# Поле "Кратко о себе" - многострочное текстовое поле с текстом-подсказкой
about_frame = tk.Frame(main_frame, bg='white')
about_frame.pack(fill='x', padx=15, pady=5)
tk.Label(about_frame, text='Кратко о себе:', bg='white', width=15,
         anchor='w').pack(side='left', anchor='n')
about_text = tk.Text(about_frame, height=3, bg='#d9d9d9', fg='gray')
about_text.pack(side='left', fill='x', expand=True)
placeholder = 'краткая информация о ваших увлечениях'
about_text.insert('1.0', placeholder)


def on_about_focus_in(event):
    """Убирает текст-подсказку при получении фокуса полем."""
    if about_text.get('1.0', 'end-1c') == placeholder:
        about_text.delete('1.0', 'end')
        about_text.config(fg='black')


def on_about_focus_out(event):
    """Возвращает текст-подсказку, если поле осталось пустым."""
    if about_text.get('1.0', 'end-1c') == '':
        about_text.insert('1.0', placeholder)
        about_text.config(fg='gray')


about_text.bind('<FocusIn>', on_about_focus_in)
about_text.bind('<FocusOut>', on_about_focus_out)

# Генерируем случайный простой пример для проверки пользователя
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
correct_answer = num1 + num2

example_label = tk.Label(
    main_frame,
    text=f'Решите пример, запишите результат в поле ниже: {num1} + {num2} = ?',
    bg='white',
    anchor='w'
)
example_label.pack(fill='x', padx=15, pady=(10, 5))

answer_entry = tk.Entry(main_frame, bg='#d9d9d9', width=15)
answer_entry.pack(anchor='w', padx=15, pady=(0, 15))


def clear_form():
    """Очищает все поля формы (кнопка "Отменить ввод")."""
    name_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    gender_var.set('')
    music_var.set(0)
    video_var.set(0)
    draw_var.set(0)
    country_combo.set('')
    city_combo.set('')
    about_text.delete('1.0', 'end')
    about_text.insert('1.0', placeholder)
    about_text.config(fg='gray')
    answer_entry.delete(0, 'end')


def submit_form():
    """Проверяет правильность решения примера и подтверждает данные."""
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Введите числовой ответ на пример.')
        return

    if user_answer == correct_answer:
        messagebox.showinfo('Успех', 'Данные успешно подтверждены!')
    else:
        messagebox.showerror('Ошибка', 'Неверный ответ на пример. '
                                        'Проверьте вычисления.')


# Кнопки "Отменить ввод" и "Данные подтверждаю"
buttons_frame = tk.Frame(main_frame, bg='white')
buttons_frame.pack(anchor='w', padx=15, pady=(0, 15))
tk.Button(buttons_frame, text='Отменить ввод',
          command=clear_form).pack(side='left', padx=(0, 10))
tk.Button(buttons_frame, text='Данные подтверждаю',
          command=submit_form).pack(side='left')

# Запускаем главный цикл обработки событий окна
root.mainloop()
# Практическое занятие № 14. Вариант 21. Задание 2.
# Разработать программу с применением пакета tk, взяв в качестве условия
# одну любую задачу из ПЗ №№ 1 - 9.
# Условие взятой задачи:
# Даны длины сторон прямоугольника (a и b), введенные пользователем.
# Вычислить площадь и периметр прямоугольника и вывести результат
# в графическом интерфейсе.

import tkinter as tk
from tkinter import messagebox

# Создаем главное окно приложения
root = tk.Tk()
root.title('Вычисление площади и периметра прямоугольника')
root.geometry('380x260')
root.resizable(False, False)

# Заголовок программы
title_label = tk.Label(
    root,
    text='Площадь и периметр прямоугольника',
    font=('Arial', 12, 'bold')
)
title_label.pack(pady=10)

# Поле для ввода длины стороны a
side_a_frame = tk.Frame(root)
side_a_frame.pack(pady=5, fill='x', padx=20)
tk.Label(side_a_frame, text='Сторона a:', width=12,
         anchor='w').pack(side='left')
side_a_entry = tk.Entry(side_a_frame)
side_a_entry.pack(side='left', fill='x', expand=True)

# Поле для ввода длины стороны b
side_b_frame = tk.Frame(root)
side_b_frame.pack(pady=5, fill='x', padx=20)
tk.Label(side_b_frame, text='Сторона b:', width=12,
         anchor='w').pack(side='left')
side_b_entry = tk.Entry(side_b_frame)
side_b_entry.pack(side='left', fill='x', expand=True)

# Метка для вывода результата вычислений
result_label = tk.Label(root, text='', font=('Arial', 10), fg='blue',
                         justify='left')
result_label.pack(pady=10)


def calculate():
    """Считывает стороны прямоугольника, вычисляет площадь и периметр,
    выводит результат на экран. Обрабатывает некорректный ввод."""
    try:
        a = float(side_a_entry.get())
        b = float(side_b_entry.get())
        if a <= 0 or b <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror('Ошибка',
                              'Введите положительные числа для сторон a и b.')
        return

    area = a * b
    perimeter = 2 * (a + b)
    result_label.config(
        text=f'Площадь: {area:.2f}\nПериметр: {perimeter:.2f}'
    )


def clear_fields():
    """Очищает поля ввода и результат."""
    side_a_entry.delete(0, 'end')
    side_b_entry.delete(0, 'end')
    result_label.config(text='')


# Кнопки "Вычислить" и "Очистить"
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)
tk.Button(buttons_frame, text='Вычислить',
          command=calculate).pack(side='left', padx=5)
tk.Button(buttons_frame, text='Очистить',
          command=clear_fields).pack(side='left', padx=5)

# Запускаем главный цикл обработки событий окна
root.mainloop()
