# Практическое занятие № 15. Вариант 21.
# Приложение РАСПРЕДЕЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ОБЯЗАННОСТЕЙ для некоторой
# организации. БД должна содержать таблицу Обязанности со следующей
# структурой записи: ФИО работника, вид дополнительной работы,
# сумма оплаты, срок.
# Программа обеспечивает функционал по вводу данных в БД (10 позиций),
# их поиску, удалению и редактированию. При организации поиска, удаления
# и редактирования используется условие, предусмотрены по три SQL-запроса
# для каждой операции.

import sqlite3

# Имя файла базы данных
DB_NAME = 'duties.db'


def create_connection():
    """Создает соединение с базой данных и возвращает объект соединения
    и курсор. Обрабатывает возможные исключения при подключении."""
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        return connection, cursor
    except sqlite3.Error as error:
        print('Ошибка подключения к базе данных:', error)
        return None, None


def create_table(cursor):
    """Создает таблицу Обязанности, если она еще не существует."""
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS duties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                duty_type TEXT NOT NULL,
                payment REAL NOT NULL,
                deadline TEXT NOT NULL
            )
        ''')
    except sqlite3.Error as error:
        print('Ошибка создания таблицы:', error)


def clear_table(cursor):
    """Очищает таблицу перед повторным заполнением тестовыми данными,
    чтобы при повторном запуске ячейки не накапливались дубликаты."""
    try:
        cursor.execute('DELETE FROM duties')
    except sqlite3.Error as error:
        print('Ошибка очистки таблицы:', error)


def insert_duty(connection, cursor, full_name, duty_type, payment, deadline):
    """Добавляет одну запись в таблицу Обязанности."""
    try:
        cursor.execute(
            'INSERT INTO duties (full_name, duty_type, payment, deadline) '
            'VALUES (?, ?, ?, ?)',
            (full_name, duty_type, payment, deadline)
        )
        connection.commit()
    except sqlite3.Error as error:
        print('Ошибка добавления записи:', error)


def show_all(cursor):
    """Выводит на экран все записи таблицы Обязанности."""
    try:
        cursor.execute('SELECT * FROM duties')
        rows = cursor.fetchall()
        print('--- Все записи таблицы "Обязанности" ---')
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print('Ошибка чтения записей:', error)


# --- Функции поиска (3 SQL-запроса с условием) ---

def search_by_full_name(cursor, full_name):
    """Поиск записей по ФИО работника (точное совпадение)."""
    try:
        cursor.execute(
            'SELECT * FROM duties WHERE full_name = ?', (full_name,)
        )
        return cursor.fetchall()
    except sqlite3.Error as error:
        print('Ошибка поиска по ФИО:', error)
        return []


def search_by_duty_type(cursor, duty_type):
    """Поиск записей по виду дополнительной работы (частичное совпадение)."""
    try:
        cursor.execute(
            'SELECT * FROM duties WHERE duty_type LIKE ?',
            ('%' + duty_type + '%',)
        )
        return cursor.fetchall()
    except sqlite3.Error as error:
        print('Ошибка поиска по виду работы:', error)
        return []


def search_by_payment_more_than(cursor, payment):
    """Поиск записей, в которых сумма оплаты больше указанного значения."""
    try:
        cursor.execute(
            'SELECT * FROM duties WHERE payment > ?', (payment,)
        )
        return cursor.fetchall()
    except sqlite3.Error as error:
        print('Ошибка поиска по сумме оплаты:', error)
        return []


# --- Функции удаления (3 SQL-запроса с условием) ---

def delete_by_id(connection, cursor, record_id):
    """Удаляет запись по идентификатору."""
    try:
        cursor.execute('DELETE FROM duties WHERE id = ?', (record_id,))
        connection.commit()
        print(f'Удалено записей по id={record_id}:', cursor.rowcount)
    except sqlite3.Error as error:
        print('Ошибка удаления по id:', error)


def delete_by_full_name(connection, cursor, full_name):
    """Удаляет записи по ФИО работника."""
    try:
        cursor.execute('DELETE FROM duties WHERE full_name = ?', (full_name,))
        connection.commit()
        print(f'Удалено записей по ФИО "{full_name}":', cursor.rowcount)
    except sqlite3.Error as error:
        print('Ошибка удаления по ФИО:', error)


def delete_by_deadline_before(connection, cursor, deadline):
    """Удаляет записи, срок которых раньше указанной даты."""
    try:
        cursor.execute('DELETE FROM duties WHERE deadline < ?', (deadline,))
        connection.commit()
        print(f'Удалено записей со сроком раньше {deadline}:',
              cursor.rowcount)
    except sqlite3.Error as error:
        print('Ошибка удаления по сроку:', error)


# --- Функции редактирования (3 SQL-запроса с условием) ---

def update_payment_by_id(connection, cursor, record_id, new_payment):
    """Изменяет сумму оплаты для записи с указанным идентификатором."""
    try:
        cursor.execute(
            'UPDATE duties SET payment = ? WHERE id = ?',
            (new_payment, record_id)
        )
        connection.commit()
        print(f'Обновлена сумма оплаты для id={record_id}:',
              cursor.rowcount, 'запись(ей)')
    except sqlite3.Error as error:
        print('Ошибка редактирования суммы оплаты:', error)


def update_deadline_by_full_name(connection, cursor, full_name, new_deadline):
    """Изменяет срок выполнения для всех записей указанного работника."""
    try:
        cursor.execute(
            'UPDATE duties SET deadline = ? WHERE full_name = ?',
            (new_deadline, full_name)
        )
        connection.commit()
        print(f'Обновлен срок для работника "{full_name}":',
              cursor.rowcount, 'запись(ей)')
    except sqlite3.Error as error:
        print('Ошибка редактирования срока:', error)


def update_duty_type_by_id(connection, cursor, record_id, new_duty_type):
    """Изменяет вид дополнительной работы для записи с указанным id."""
    try:
        cursor.execute(
            'UPDATE duties SET duty_type = ? WHERE id = ?',
            (new_duty_type, record_id)
        )
        connection.commit()
        print(f'Обновлен вид работы для id={record_id}:',
              cursor.rowcount, 'запись(ей)')
    except sqlite3.Error as error:
        print('Ошибка редактирования вида работы:', error)


def main():
    """Основная функция программы: создает БД, заполняет тестовыми
    данными, демонстрирует поиск, удаление и редактирование записей."""
    connection, cursor = create_connection()
    if connection is None:
        return

    create_table(cursor)
    clear_table(cursor)

    # Заполняем таблицу 10 тестовыми записями
    test_data = [
        ('Иванов Иван Иванович', 'Кураторство группы', 5000.0, '2026-09-01'),
        ('Петров Петр Петрович', 'Организация мероприятий', 3000.0, '2026-08-15'),
        ('Сидорова Анна Сергеевна', 'Ведение кружка', 4500.0, '2026-10-01'),
        ('Кузнецов Олег Викторович', 'Контроль практики студентов', 6000.0, '2026-07-20'),
        ('Смирнова Елена Андреевна', 'Кураторство группы', 5200.0, '2026-09-10'),
        ('Васильев Дмитрий Игоревич', 'Организация олимпиад', 4000.0, '2026-11-05'),
        ('Морозова Ольга Павловна', 'Ведение кружка', 3800.0, '2026-08-25'),
        ('Никитин Сергей Алексеевич', 'Контроль практики студентов', 6200.0, '2026-07-30'),
        ('Федорова Мария Дмитриевна', 'Организация мероприятий', 3300.0, '2026-09-15'),
        ('Орлов Андрей Николаевич', 'Кураторство группы', 5100.0, '2026-10-20'),
    ]

    for record in test_data:
        insert_duty(connection, cursor, *record)

    show_all(cursor)

    # --- Демонстрация поиска ---
    print('\n--- Поиск по ФИО "Иванов Иван Иванович" ---')
    for row in search_by_full_name(cursor, 'Иванов Иван Иванович'):
        print(row)

    print('\n--- Поиск по виду работы, содержащему "Кураторство" ---')
    for row in search_by_duty_type(cursor, 'Кураторство'):
        print(row)

    print('\n--- Поиск записей с оплатой больше 5000 ---')
    for row in search_by_payment_more_than(cursor, 5000):
        print(row)

    # --- Демонстрация редактирования ---
    print('\n--- Редактирование ---')
    update_payment_by_id(connection, cursor, 1, 5500.0)
    update_deadline_by_full_name(connection, cursor,
                                  'Петров Петр Петрович', '2026-12-01')
    update_duty_type_by_id(connection, cursor, 3, 'Ведение секции')

    show_all(cursor)

    # --- Демонстрация удаления ---
    print('\n--- Удаление ---')
    delete_by_id(connection, cursor, 9)
    delete_by_full_name(connection, cursor, 'Орлов Андрей Николаевич')
    delete_by_deadline_before(connection, cursor, '2026-08-01')

    print('\n--- Итоговое состояние таблицы ---')
    show_all(cursor)

    connection.close()


if __name__ == '__main__':
    main()
