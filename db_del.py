import sqlite3

def main():

    try:
        sqliteConnection = sqlite3.connect('news.db')
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sql_update_query = """DROP TABLE user"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        # print("User table deleted successfully")

        sql_update_query = """DROP TABLE file"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        # print("File table deleted successfully")

        sql_update_query = """DROP TABLE syntax"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        # print("Syntax table deleted successfully")

        sql_update_query = """DROP TABLE semantic"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        # print("Semantic table deleted successfully")

        sql_update_query = """DROP TABLE sentiment"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        # print("Semantic table deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("sqlite connection is closed")

if __name__ == "__main__":
    main()