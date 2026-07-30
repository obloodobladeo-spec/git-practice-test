import pymysql


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "0104",
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
        )

    def get_all_sales(self):
        sql = """
            SELECT
                sale_id,
                sale_date,
                product_name,
                price,
                sales_quantity
            FROM sales
            ORDER BY sale_date DESC, sale_id DESC
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    return cursor.fetchall()
        except pymysql.MySQLError as error:
            raise RuntimeError(f"판매 정보 조회 실패: {error}") from error

    def insert_sale(self, sale_date, product_name, price, sales_quantity):
        sql = """
            INSERT INTO sales (
                sale_date,
                product_name,
                price,
                sales_quantity
            )
            VALUES (%s, %s, %s, %s)
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        sql,
                        (sale_date, product_name, price, sales_quantity),
                    )
                    connection.commit()
                    return cursor.lastrowid
        except pymysql.MySQLError as error:
            raise RuntimeError(f"판매 정보 등록 실패: {error}") from error

    def update_sale(
        self,
        sale_id,
        sale_date,
        product_name,
        price,
        sales_quantity,
    ):
        sql = """
            UPDATE sales
            SET
                sale_date = %s,
                product_name = %s,
                price = %s,
                sales_quantity = %s
            WHERE sale_id = %s
        """

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        sql,
                        (
                            sale_date,
                            product_name,
                            price,
                            sales_quantity,
                            sale_id,
                        ),
                    )
                    connection.commit()
                    return cursor.rowcount
        except pymysql.MySQLError as error:
            raise RuntimeError(f"판매 정보 수정 실패: {error}") from error

    def delete_sale(self, sale_id):
        sql = "DELETE FROM sales WHERE sale_id = %s"

        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, (sale_id,))
                    connection.commit()
                    return cursor.rowcount
        except pymysql.MySQLError as error:
            raise RuntimeError(f"판매 정보 삭제 실패: {error}") from error
