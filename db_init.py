# run with db_del.py for each test run

import sqlite3

def main():

    news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
    news_cur = news_con.cursor() # to execute SQL statements, need DB cursor

    # these 2 create table commands --> just run once!

    # create table user with columns for userID (primary key), username
    news_cur.execute("CREATE TABLE user(userID, username)")
    # create table files with columns for fileID (foreign key), userID (foreign key), amd other fields
    news_cur.execute("CREATE TABLE file(fileID, userID, filename, fileformat, filepath, lastmodified)")

if __name__ == "__main__":
    main()