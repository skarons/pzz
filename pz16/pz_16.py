# Практическое занятие № 16. Вариант 21.
# Из каждого блока заданий выполнена одна задача из своего варианта
# (суммарно 2 задачи).
#
# Блок заданий 1, задача 21:
# Создайте класс «Календарь», который имеет атрибуты год, месяц и день.
# Добавьте методы для определения дня недели, проверки на високосный год
# и определения количества дней в месяце.
#
# Блок заданий 2, задача 21:
# Создайте базовый класс "Животное" со свойствами "вид", "количество лап",
# "цвет шерсти". От этого класса унаследуйте класс "Собака" и добавьте
# в него свойства "кличка" и "порода".
#

import datetime


# --- Блок заданий 1, задача 21 ---

class Calendar:
    """Класс «Календарь» с атрибутами год, месяц, день и методами для
    определения дня недели, проверки високосного года и количества
    дней в месяце."""

    # Названия дней недели для удобного вывода результата
    weekday_names = (
        'понедельник', 'вторник', 'среда', 'четверг',
        'пятница', 'суббота', 'воскресенье'
    )

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_weekday(self):
        """Возвращает название дня недели для заданной даты."""
        try:
            date_obj = datetime.date(self.year, self.month, self.day)
            return self.weekday_names[date_obj.weekday()]
        except ValueError as error:
            return f'Некорректная дата: {error}'

    def is_leap_year(self):
        """Проверяет, является ли год високосным."""
        year = self.year
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self):
        """Возвращает количество дней в указанном месяце с учетом
        високосного года для февраля."""
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month < 1 or self.month > 12:
            return 'Некорректный номер месяца'
        if self.month == 2 and self.is_leap_year():
            return 29
        return days_per_month[self.month - 1]

    def __str__(self):
        return f'{self.day:02d}.{self.month:02d}.{self.year}'


# --- Блок заданий 2, задача 21 ---

class Animal:
    """Базовый класс «Животное» со свойствами вид, количество лап,
    цвет шерсти."""

    def __init__(self, species, legs_count, fur_color):
        self.species = species
        self.legs_count = legs_count
        self.fur_color = fur_color

    def get_info(self):
        """Возвращает строку с общей информацией о животном."""
        return (f'Вид: {self.species}, Количество лап: {self.legs_count}, '
                f'Цвет шерсти: {self.fur_color}')


class Dog(Animal):
    """Класс «Собака», наследуется от класса «Животное» и добавляет
    свойства кличка и порода."""

    def __init__(self, species, legs_count, fur_color, name, breed):
        super().__init__(species, legs_count, fur_color)
        self.name = name
        self.breed = breed

    def get_info(self):
        """Дополняет общую информацию о животном кличкой и породой."""
        base_info = super().get_info()
        return f'{base_info}, Кличка: {self.name}, Порода: {self.breed}'

    def bark(self):
        """Метод, имитирующий лай собаки."""
        return f'{self.name} говорит: Гав-гав!'


def main():
    """Демонстрирует работу классов Calendar, Animal и Dog на тестовых
    данных (тестовые запуски для всех реализуемых классов)."""

    print('=== Тестирование класса "Календарь" ===')
    dates = [
        Calendar(2026, 6, 24),   # текущая дата
        Calendar(2024, 2, 29),   # високосный год, последний день февраля
        Calendar(2026, 2, 29),   # некорректная дата (2026 - не високосный)
        Calendar(2000, 1, 1),
    ]

    for cal in dates:
        print(f'\nДата: {cal}')
        print('День недели:', cal.get_weekday())
        print('Високосный год:', 'да' if cal.is_leap_year() else 'нет')
        print('Дней в месяце:', cal.days_in_month())

    print('\n=== Тестирование классов "Животное" и "Собака" ===')

    generic_animal = Animal('Птица', 2, 'разноцветный')
    print('\nОбъект класса Animal:')
    print(generic_animal.get_info())

    dog1 = Dog('Млекопитающее', 4, 'рыжий', 'Бим', 'Дворняжка')
    dog2 = Dog('Млекопитающее', 4, 'черно-белый', 'Рекс', 'Овчарка')

    print('\nОбъекты класса Dog:')
    for dog in (dog1, dog2):
        print(dog.get_info())
        print(dog.bark())


if __name__ == '__main__':
    main()
