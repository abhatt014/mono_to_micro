# check mysqldb conenction
import mysql.connector
def get_conn():
    try:
        return mysql.connector.connect(
            host="mysql_db",
            user="appuser",
            password="redhat",
            database="schooldb"
        )
    except mysql.connector.Error as e:
        print(f"DB issue- {e}") 
get_conn()        