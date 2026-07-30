import pymysql


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "0104",
    "database": "cafe_db",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}


class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        try:
            return pymysql.connect(**self.config)
        except pymysql.MySQLError as error:
            raise RuntimeError(f"데이터베이스 연결 실패: {error}") from error

    def get_all_menu(self):
        connection = None

        try:
            connection = self.connect()

            with connection.cursor() as cursor:
                sql = """
                    SELECT
                        menu_id,
                        product_name,
                        price,
                        stock
                    FROM menu
                    ORDER BY menu_id
                """

                cursor.execute(sql)
                return cursor.fetchall()

        except pymysql.MySQLError as error:
            raise RuntimeError(f"메뉴 조회 실패: {error}") from error

        finally:
            if connection is not None:
                connection.close()

    def insert_menu(self, product_name, price, stock):
        connection = None

        try:
            connection = self.connect()

            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO menu (
                        product_name,
                        price,
                        stock
                    )
                    VALUES (%s, %s, %s)
                """

                cursor.execute(
                    sql,
                    (product_name, price, stock),
                )

                new_menu_id = cursor.lastrowid

            connection.commit()
            return new_menu_id

        except pymysql.MySQLError as error:
            if connection is not None:
                connection.rollback()

            raise RuntimeError(f"메뉴 등록 실패: {error}") from error

        finally:
            if connection is not None:
                connection.close()

    def update_menu(self, menu_id, product_name, price, stock):
        connection = None

        try:
            connection = self.connect()

            with connection.cursor() as cursor:
                sql = """
                    UPDATE menu
                    SET
                        product_name = %s,
                        price = %s,
                        stock = %s
                    WHERE menu_id = %s
                """

                cursor.execute(
                    sql,
                    (product_name, price, stock, menu_id),
                )

                changed_rows = cursor.rowcount

            connection.commit()
            return changed_rows

        except pymysql.MySQLError as error:
            if connection is not None:
                connection.rollback()

            raise RuntimeError(f"메뉴 수정 실패: {error}") from error

        finally:
            if connection is not None:
                connection.close()

    def delete_menu(self, menu_id):
        connection = None

        try:
            connection = self.connect()

            with connection.cursor() as cursor:
                sql = """
                    DELETE FROM menu
                    WHERE menu_id = %s
                """

                cursor.execute(sql, (menu_id,))
                deleted_rows = cursor.rowcount

            connection.commit()
            return deleted_rows

        except pymysql.MySQLError as error:
            if connection is not None:
                connection.rollback()

            raise RuntimeError(f"메뉴 삭제 실패: {error}") from error

        finally:
            if connection is not None:
                connection.close()