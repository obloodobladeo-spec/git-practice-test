import pymysql


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "0104",  # 본인 MySQL 비밀번호
    "database": "cafe_db",
    "charset": "utf8mb4",
}


class DB:
    def __init__(self, **config):
        self.config = config

    def _connect(self):
        return pymysql.connect(
            **self.config,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False,
        )

    # -------------------------
    # 메뉴 조회
    # -------------------------
    def get_menus_by_category(self, category):
        sql = """
            SELECT
                menu_id,
                product_name,
                price,
                category
            FROM menus
            WHERE category = %s
            ORDER BY menu_id
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, (category,))
                    return cursor.fetchall()
        except pymysql.MySQLError as error:
            raise RuntimeError(
                f"카테고리별 메뉴 조회 실패: {error}"
            ) from error

    def get_menu(self, menu_id):
        sql = """
            SELECT
                menu_id,
                product_name,
                price,
                category
            FROM menus
            WHERE menu_id = %s
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, (menu_id,))
                    return cursor.fetchone()
        except pymysql.MySQLError as error:
            raise RuntimeError(
                f"메뉴 조회 실패: {error}"
            ) from error

    # -------------------------
    # 메뉴 등록
    # -------------------------
    def insert_menu(self, product_name, price, category):
        sql = """
            INSERT INTO menus (
                product_name,
                price,
                category
            )
            VALUES (%s, %s, %s)
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        sql,
                        (product_name, price, category),
                    )
                    connection.commit()
                    return cursor.lastrowid

        except pymysql.err.IntegrityError as error:
            raise RuntimeError(
                "이미 등록된 메뉴명입니다."
            ) from error

        except pymysql.MySQLError as error:
            raise RuntimeError(
                f"메뉴 등록 실패: {error}"
            ) from error

    # -------------------------
    # 메뉴 수정
    # -------------------------
    def update_menu(
        self,
        menu_id,
        product_name,
        price,
        category,
    ):
        sql = """
            UPDATE menus
            SET
                product_name = %s,
                price = %s,
                category = %s
            WHERE menu_id = %s
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        sql,
                        (
                            product_name,
                            price,
                            category,
                            menu_id,
                        ),
                    )
                    connection.commit()
                    return cursor.rowcount

        except pymysql.err.IntegrityError as error:
            raise RuntimeError(
                "이미 등록된 메뉴명입니다."
            ) from error

        except pymysql.MySQLError as error:
            raise RuntimeError(
                f"메뉴 수정 실패: {error}"
            ) from error

    # -------------------------
    # 메뉴 삭제
    # -------------------------
    def delete_menu(self, menu_id):
        sql = """
            DELETE FROM menus
            WHERE menu_id = %s
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, (menu_id,))
                    connection.commit()
                    return cursor.rowcount

        except pymysql.err.IntegrityError as error:
            raise RuntimeError(
                "판매 기록에서 사용 중인 메뉴는 삭제할 수 없습니다."
            ) from error

        except pymysql.MySQLError as error:
            raise RuntimeError(
                f"메뉴 삭제 실패: {error}"
            ) from error
