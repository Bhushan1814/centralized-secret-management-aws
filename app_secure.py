import json
import os
import boto3
import pymysql
from botocore.exceptions import ClientError

SECRET_NAME = os.environ.get("SECRET_NAME", "prod/myapp/db")
REGION = os.environ.get("AWS_REGION", "ap-south-1")


def get_db_secret():
    client = boto3.client("secretsmanager", region_name=REGION)
    try:
        resp = client.get_secret_value(SecretId=SECRET_NAME)
    except ClientError as e:
        print(f"Failed to fetch secret: {e.response['Error']['Code']}")
        raise
    return json.loads(resp["SecretString"])


def main():
    s = get_db_secret()
    print(f"[SECURE] Secret retrieved for user: {s['username']} (password not logged)")

    conn = pymysql.connect(host=s["host"], user=s["username"],
                           password=s["password"], database=s["dbname"],
                           port=int(s.get("port", 3306)), connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("SELECT id, name FROM employees")
        for row in cur.fetchall():
            print(row)
    conn.close()
    print("[SECURE] Connected to DB using credentials from Secrets Manager")


if __name__ == "__main__":
    main()
