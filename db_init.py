# run with db_del.py for each test run

import sqlite3

def main():

    news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
    news_cur = news_con.cursor() # to execute SQL statements, need DB cursor

    # create table user with columns for userID (primary key), username
    news_cur.execute("CREATE TABLE user(userID, username)")

    # create table files with columns for fileID (foreign key), userID (foreign key), amd other fields
    news_cur.execute("CREATE TABLE file(fileID, userID, filename, fileformat, filepath, lastmodified)")

    # create table syntax
    news_cur.execute("CREATE TABLE syntax(fileID, totpara, totchar, datecreated, summary, keyword1, keyword2, keyword3)")

    # create table sentiment, by paragraph
    news_cur.execute("CREATE TABLE sentiment(fileID, numpara, sentiment)")

    # create table semantic
    news_cur.execute("CREATE TABLE semantic(fileID, numpara, summary, keyword1, keyword2)")

if __name__ == "__main__":
    main()