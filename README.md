# Sunni Lin: EC530 Project 2 Phases 1 & 2

## Phase 1 Project planning: 
https://docs.google.com/document/d/1bWQMwJF8acSlcFsaNRGe5-e_mNwvOdveBfMwQez6kpI/edit


## Phase 2: DB Design

Design Qs to consider --> us designing our use cases!
1) Should we analyze on the spot or not? (consider: storage etc)
    No, store in document-DB for quicker accessing next time.
2) Should we have many-to-many or 1-to-many relationships (between users and files)?
    only own
3) File system --> drive? path/storage location? ex. Azure --> block storage "organization structure"
4) Keywords by paragraph or whole text?
5) Entities in files: paragraph, whole text. & their individual attributes?

## Phase 3: DB Implementation
1) In sqlite, initialized database news with 2 tables: users and files
2) In MongoDB (?)

### DESIGN (subject to change upon implementation!)
**Relational Database: SQLite for 1) Users (Accounts), 2) File**
This design choice is based on the straightforward relationship between users and files that we define: 1 user to many files. The users and files tables are linked by the userID key, and each table contains attributes that can be easily accessed via a query.
1) Users: A relational database is useful here. We store a table of users, identifiable by user_id as the primary key. Each record includes:
    - userID (primary key)
    - userName
    - (some link to files)
2) Files: We store a table of files, connected to the Users table by the foreign key user_id (the primary key of the Users table). Each file records:
    - fileID (primary key)
    - userID (foreign key, link to Users table)
    - fileName
    - originalFile
    - textFile (readable by code: converted to text from original --> binary text file)
    - fileFormat (pdf, csv, jpeg etc.)
    - lastModified (timestamp)
    - link/path (some sort of connection to the document analysis, perhaps drive/cloud link)

**Document Database: MongoDB for 1) Documents (ie files)**
1) Documents: A document-based, non-structured NoSQL DB may be useful here to store the different analyses results of each file (document). With this, the DB can support non-linear relationships and hierarchical nature of syntax, semantics, sentiment, and other analyses results. Structure by the following:
    Some design choices:
        1. In collection, will have a document (with more fields) for syntax analysis and a document for content analysis
        2. Entities: whole text & paragraphs
        3. For whole text, have Keywords (up to 10), Summary, overallSentiment
        4. For paragraphs, have Keyword (just 1), sentiment (just 1)

{
   _id: fileID(7df78ad8902c)
   fileName: 'Document1', 
   fileDescription: 'Document 1 in user Sunni',
   userID: '012345',
   path: 'https://azure.microsoft.com/en-us/products/storage/blobs', <!-- path on drive/cloud -->
   keywords: ['mongodb', 'database', 'NoSQL'],
    <!-- syntax/overall -->
   overall: [	
        {
            numParagraphs:'user1',
            numLines: 'My first comment',
            numCharacters: 10
            dateCreated: new Date(2011,1,25,7,45)
            summary: 'whole-text summary'
        },
    ]
    <!-- organized by paragraph: sentiment & semantics analysis -->
    analysis: [	
        {
            paragraph: 1,
            sentiment: 'positive',
            keyword: 'database', <!-- only 1 keyword for each paragraph -->
            summary: 'mongodb is good'
        },
        {
            paragraph: 2,
            sentiment: 'negative',
            keyword: 'bad',
            summary: 'mongodb is bad'
        }
    ]
}





Other pending design choices/considerations:
- a status field?
- Want many:many (users:files)? If so, add PrimaryUser/Owner?
    if storing analysis results (ex. of a news article), may be a good option
- linking the SQLite and MongoDB content together


Supplementary/Notes
- Python SQLite tutorial: https://www.tutorialspoint.com/sqlite/sqlite_python.htm
- some SQL tables allow you to put JSON entries (but some not supported) so if you want multiple entries in a single record (ex. 1 paragraph, multiple keywords)
SQL: not that good for "search-for-field"
- Document Database: MongoDB "Data is stored in collections that are analogous to MySQL tables. A collection is a group of documents (a set of key value pairs) and can consist of many documents in which data is stored in JSON format of key-value" https://www.knowi.com/blog/mongodb-vs-sql/ 
- Azure Storage Blob is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that does not adhere to a particular data model or definition, such as text or binary data. https://azure.microsoft.com/en-us/products/storage/blobs 
- good correspondence between SQL & NoSQL DB! (& good MongoDB tutorial) https://medium.com/nerd-for-tech/all-basics-of-mongodb-in-10-minutes-baddaf6b6625 
- https://docs.python.org/3/library/sqlite3.html 