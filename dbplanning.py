# {
#    _id: ObjectId(7df78ad8902c)
#    title: 'MongoDB Overview', 
#    description: 'MongoDB is no sql database',
#    by: 'tutorials point',
#    url: 'http://www.tutorialspoint.com',
#    tags: ['mongodb', 'database', 'NoSQL'],
#    likes: 100, 
#    comments: [	
#       {
#          user:'user1',
#          message: 'My first comment',
#          dateCreated: new Date(2011,1,20,2,15),
#          like: 0 
#       },
#       {
#          user:'user2',
#          message: 'My second comments',
#          dateCreated: new Date(2011,1,25,7,45),
#          like: 5a
#       }
#    ]
# }


import sqlite3

# implicitly creating users.db if not in cwd 
users_con = sqlite3.connect("users.db") # returns a Connection object, represents conntection to on-disk db
users_cur = users_con.cursor() # to execute SQL statements, need DB cursor

# create table movie with columns for title, release year, and review score
users_cur.execute("CREATE TABLE movie(title, year, score)")
# res = users_cur.execute("SELECT name FROM sqlite_master")
# res = users_cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# print(res.fetchone() is None)

# adding 2 rows of data supplied as SQL literals
# the INSERT statement implicitly opens a transaction --> needs to be COMMITTED before saving in DB
users_cur.execute("""
   INSERT INTO movie VALUES
      ('Monty Python and the Holy Grail', 1975, 9.2),
      ('And Now for Something Completely Different', 1971, 7.5)
""")
users_con.commit()

# verify
res = users_cur.execute("SELECT score FROM movie")
print(res.fetchall())

# insert 3 more rows
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

# ? placeholders bind data to the query. always use placeholders
users_cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
users_con.commit()

# verify new rows addition
for row in users_cur.execute("SELECT year, title FROM movie ORDER BY year"):
      print(row)

# verify db has been written to disk by calling close
users_con.close()
new_con = sqlite3.connect("users.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')