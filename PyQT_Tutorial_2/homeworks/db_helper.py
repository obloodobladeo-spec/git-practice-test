# db_helper.py
import pymysql

DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="0104",
    database="sampledb",
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

    # 회원가입 기능
    def rgt_user(self, username, password):
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)" # 내림차 순으로 id, email조회
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (username, password))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False

    # 멤버 전체 조회 (내림차 순으로 id, name, email조회하고 값으로 반환해주는 함수)
    def fetch_members(self):
        sql = "SELECT id, name, email FROM members ORDER BY id" # 내림차 순으로 id, email조회
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()  # [(id, name, email), ...] 리스트 인가? 아마 조회 데이터 묶음으로 리스트 형태가 아닌 

    # 멤버 추가 (INSERT를 통해서 mysql의 가져온 데이터에 직접 데이터를 삽입해줌, True반환)
    # 데이터를 추가, 제거 등의 수정하는 경우 에러상황을 대비해야 한다.(rollback)
    def insert_member(self, name, email):
        sql = "INSERT INTO members (name, email) VALUES (%s, %s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, email))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False

    # 맴버 제거
    def delete_member(self, id):
        placeholders = ",".join(["%s"] * len(id))

        sql = f"DELETE FROM members WHERE id in ({placeholders})"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (id))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False