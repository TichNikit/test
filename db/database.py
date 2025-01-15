import psycopg2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_table():
    connection = psycopg2.connect("postgresql://username:password@localhost/planes")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Planes(
    id SERIAL PRIMARY KEY,
    flightid INTEGER NOT NULL UNIQUE,
    reg TEXT NOT NULL
    )
    ''')
    connection.commit()
    cursor.close()
    logger.info("Таблица 'Planes' успешно создана или уже существует.")


def get_db_connection():
    return psycopg2.connect("postgresql://username:password@localhost/planes")


def create_table():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Planes(
            id SERIAL PRIMARY KEY,
            flightid INTEGER NOT NULL UNIQUE,
            reg TEXT NOT NULL
            )
            ''')
            connection.commit()
    logger.info("Таблица 'Planes' успешно создана или уже существует.")


def get_planes():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM Planes')
            planes = cursor.fetchall()
    logger.info(f"Извлечено {len(planes)} самолетов из базы данных.")
    return planes


def get_plane(plane_id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM Planes WHERE id=%s', (plane_id,))
            plane = cursor.fetchone()
    status = "найден" if plane else "не найден"
    logger.info(f"Самолет с id={plane_id} {status}.")
    return plane


def delete_plane(plane_id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM Planes WHERE id=%s', (plane_id,))
            connection.commit()
    logger.info(f"Самолет с id={plane_id} успешно удален.")


def delete_planes():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM Planes')
            connection.commit()
    logger.info("Все самолеты успешно удалены из базы данных.")


def post_plane(result):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            data = get_planes()
            existing_flightids = {row[1] for row in data}

            added_count = 0
            for flight in result:
                flightid = flight['flightid']
                registration = flight['extraInfo']['reg']
                if flightid not in existing_flightids:
                    cursor.execute("INSERT INTO Planes(flightid, reg) VALUES (%s, %s)", (flightid, registration))
                    added_count += 1

            connection.commit()
    logger.info(f"Добавлено {added_count} новых самолетов в базу данных.")

#
# list_ = asyncio.run(get_planes_data())
#
# post_plane(list_)
# print(get_planes())

# create_table()

# print(get_planes())
