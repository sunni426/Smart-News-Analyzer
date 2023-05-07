# run with db_del.py for each test run

import sqlite3

def main():

    news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
    news_cur = news_con.cursor() # to execute SQL statements, need DB cursor

    # create table user with columns for userID (primary key), username
    news_cur.execute("CREATE TABLE user(userID PRIMARY KEY, username, numfiles, fileIDs TEXT)")

    # create table files with columns for fileID (foreign key), userID (foreign key), amd other fields
    news_cur.execute("CREATE TABLE file(fileID PRIMARY KEY, userID, filename, fileformat, filepath, lastmodified, contents)")

    # create table syntax
    news_cur.execute("CREATE TABLE syntax(fileID PRIMARY KEY, totpara, totword, datecreated, keywords TEXT)")

    # create table semantic
    news_cur.execute("CREATE TABLE semantic(fileID, numpara PRIMARY KEY, summary, keywords TEXT)")

    # create table sentiment, by paragraph
    news_cur.execute("CREATE TABLE sentiment(fileID, numpara PRIMARY KEY, sentiment TEXT)")


if __name__ == "__main__":
    main()