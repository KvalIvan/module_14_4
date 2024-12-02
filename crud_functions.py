import sqlite3


def initiate_db():
    connection = sqlite3.connect('telegram_database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('telegram_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connection.commit()
    return all_products


def create_user():
    connection = sqlite3.connect('telegram_database.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        price = 100 * i
        cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
                       (f'title {i}', f'Описание {i}', price))
    connection.commit()
    connection.close()


initiate_db()
# create_user()
