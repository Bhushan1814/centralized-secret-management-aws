import configparser
import pymysql

cfg = configparser.ConfigParser()
cfg.read("config.ini")
db = cfg["database"]

conn = pymysql.connect(host=db["host"], user=db["user"],
                       password=db["password"], database=db["name"],
                       connect_timeout=5)
with conn.cursor() as cur:
    cur.execute("SELECT id, name FROM employees")
    for row in cur.fetchall():
        print(row)
conn.close()
print("[INSECURE] Connected using hardcoded credentials from config.ini")
