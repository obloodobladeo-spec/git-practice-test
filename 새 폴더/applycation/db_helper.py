# db_helper.py
import pymysql

DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="0104",
    database="cafe",
    charset="utf8"
)

# class db를 만들어준다. 
class DB:
    def __init__(self, **config): 
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)

    # 로그인 검증 (설렉트를 통해서 웨어 조건으로 서치해서 한줄을 읽고 boolion을 반환해줌)
    # 여기가 부터 전체적으로 with문이 쓰이는데 with는 자동으로 닫기를 해주는 역할을 한다.
    def verify_user(self, username, password):
        sql = "SELECT COUNT(*) FROM users WHERE username=%s AND password=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username, password))
                count, = cur.fetchone()
                return count == 1 # (True, False를 반환 해줌)

    def fetch_members(self):
        sql = "SELECT ingredient_name, stock, unit, price FROM menus ORDER BY ingredient_id"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    def insert_members(self, ingredient_name, stock, unit, price):
        sql = "INSERT INTO menus (ingredient_name, stock, unit, price) VALUES (%s, %s, %s, %s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (ingredient_name, stock, unit, price))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False