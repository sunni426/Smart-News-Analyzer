# Sunni Lin: EC530 Project 2 Phase 1

Project planning: https://docs.google.com/document/d/1bWQMwJF8acSlcFsaNRGe5-e_mNwvOdveBfMwQez6kpI/edit

Python SQLite tutorial: https://www.tutorialspoint.com/sqlite/sqlite_python.htm

Relational Database: SQLite (provide reasoning)
1) Users: A relational database is useful here. We store a table of users, identifiable by user_id as the primary key. Each record includes:
    - userID (primary key)
    - userName
    - 
2) Files: We store a table of files, connected to the Users table by the foreign key user_id (the primary key of the Users table). Each file records:
    - fileID (primary key)
    - userID (foreign key, link to Users table)
    - fileName
    - originalFile
    - textFile (readable by code: converted to text from original)
    - fileFormat
    - link (some sort of connection to the document analysis) -- perhaps common Drive link or just the fileID? does it make sense?






Document Database: MongoDB "Data is stored in collections that are analogous to MySQL tables. A collection is a group of documents (a set of key value pairs) and can consist of many documents in which data is stored in JSON format of key-value" https://www.knowi.com/blog/mongodb-vs-sql/ 
1) Documents: we store the different analyses results of each file (document) in this non-structured database to support non-linear relationships and hierarchical nature of syntax, semantics, sentiment, and other analyses results. Struture by the following:


paragraph --> sentiment for each
    - perhaps paragraph as a key-value pair
whole text --> keywords, summary

{
   _id: fileID(7df78ad8902c)
   fileName: 'Document1
   ', 
   fileDescription: 'MongoDB is no sql database',
   userID: 'tutorials point',
   url: 'http://www.tutorialspoint.com',
   keywords: ['mongodb', 'database', 'NoSQL'],
   syntax: [	
      {
         user:'user1',
         message: 'My first comment',
         dateCreated: new Date(2011,1,20,2,15),
         like: 0 
      },
      {
         user:'user2',
         message: 'My second comments',
         dateCreated: new Date(2011,1,25,7,45),
         like: 5a
      }
   ]
    sentiment: [	
      {
         user:'user1',
         message: 'My first comment',
         dateCreated: new Date(2011,1,20,2,15),
         like: 0 
      },
      {
         user:'user2',
         message: 'My second comments',
         dateCreated: new Date(2011,1,25,7,45),
         like: 5a
      }
   ]
    semantics: [	
      {
         user:'user1',
         message: 'My first comment',
         dateCreated: new Date(2011,1,20,2,15),
         like: 0 
      },
      {
         user:'user2',
         message: 'My second comments',
         dateCreated: new Date(2011,1,25,7,45),
         like: 5a
      }
   ]
}



{
   _id: ObjectId(7df78ad8902c)
   title: 'MongoDB Overview', 
   description: 'MongoDB is no sql database',
   by: 'tutorials point',
   url: 'http://www.tutorialspoint.com',
   tags: ['mongodb', 'database', 'NoSQL'],
   likes: 100, 
   comments: [	
      {
         user:'user1',
         message: 'My first comment',
         dateCreated: new Date(2011,1,20,2,15),
         like: 0 
      },
      {
         user:'user2',
         message: 'My second comments',
         dateCreated: new Date(2011,1,25,7,45),
         like: 5a
      }
   ]
}