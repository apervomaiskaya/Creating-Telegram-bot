import sqlite3

# Создаем базу данных и таблицу для хранения фотографий
def create_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Создаем таблицу для хранения фотографий
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS photos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id TEXT NOT NULL,
            caption TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Укажите имя файла базы данных, соответствующее конфигурации
create_database('cats.db')
