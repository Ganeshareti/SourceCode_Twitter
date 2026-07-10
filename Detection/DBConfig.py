import mysql.connector


class DBConnection:

    @staticmethod
    def getConnection():
        try:
            # Connect without selecting a database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root"
            )

            cursor = conn.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS twitter_spam")

            # Select the database
            cursor.execute("USE twitter_spam")

            # Create register table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS register(
                    name VARCHAR(100),
                    username VARCHAR(100),
                    passwrd VARCHAR(100),
                    email VARCHAR(100),
                    mno VARCHAR(100)
                )
            """)

            conn.commit()

            print("Database and table are ready.")
            return conn

        except mysql.connector.Error as err:
            print("Database Error:", err)
            return None


if __name__ == "__main__":
    db = DBConnection.getConnection()
    if db:
        print("Connected Successfully")