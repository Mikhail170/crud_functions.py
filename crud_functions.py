# import sqlite3
# connection = sqlite3.connect('database2.db')
# cursor = connection.cursor()
#
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Products
# (id INTEGER PRIMARY KEY,
# title TEXT NOT NULL,
# description TEXT NOT NULL,
# price INTEGER NOT NULL)
# ''')
#
#
# def add_products(product_id, title, description, price):
#     check_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
#     if check_product.fetchone() is None:
#         cursor.execute(f'Название: {title} | Описание: {description} | Цена: {price}', 0)
#
#
# connection.commit()
# connection.close()

import sqlite3


def initiate_db():
    connection = sqlite3.connect('database2.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY, 
                 title TEXT NOT NULL, 
                 description TEXT NOT NULL, 
                 price INTEGER NOT NULL)''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database2.db')
    c = connection.cursor()
    c.execute('SELECT * FROM Products')
    products = c.fetchall()
    connection.close()
    return products


def add_product(product_id, title, description, price):
    connection = sqlite3.connect('database2.db')
    c = connection.cursor()
    c.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
              (product_id, title, description, price))
    connection.commit()
    connection.close()


initiate_db()


products = [
    (1, 'Product 1', 'Description 1', 100),
    (2, 'Product 2', 'Description 2', 200),
    (3, 'Product 3', 'Description 3', 300),
    (4, 'Product 4', 'Description 4', 400),
]

for product in products:
    add_product(*product)
