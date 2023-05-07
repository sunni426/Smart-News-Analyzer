# Sunni Lin: EC530 Spring 2023 Final Project: News Analyzer

## FINAL PHASE: Full Module Implementation, Packaging, Containerization, Dockerization, and Pip Install
### Components:
1) RESTFUL APIs for Document Uploader, Document Analyzer, Feed Ingester, included with Google login authentication, documentation, error messages, and unit tests
    ** File Uploader
    ** NPL Analysis: uses the Natural Language Toolkit (NLTK) library and TextBlob library for sentiment analysis
    ** News Ingester: uses Python's feedparser library to parse any website that has RSS or Atom feeds and obtain data's title, summary, keywords, link etc
2) Database: Relational-based SQLite
3) Queueing and Multi-threading capacity for asynchronous handle
    - Used to support concurrent NLP analysis
4) GUI: Tkinter
    Four widgets - a label to display login status, and three buttons for "File Upload", "NLP Analysis", and "Feed Ingester". Initially, all three buttons are disabled. When the user clicks the "Log in!" button, the on_button_click function is called. If the login is successful, it updates the login label with "Login successful!" and enables all three buttons.
5) Packaging: Using Pip installer Support Flow of Packaging
    # To install:
        python setup.py sdist
        python setup.py install
        pip install -r requirements.txt dist/news_analyzer-1.0.tar.gz
    # How to test pip install was correctly done:
        1. Do pip list: Check if newsAnalyzer is in the list of installed packages
        2. Check environment and PATH
        3. Can use the package! Import news_analyzer and use its modules

** DEMO VIDEO: https://drive.google.com/file/d/1bJt3qZWxqWAssk1yy1ymVYLZqqgQhLx4/view?usp=sharing


## Workflow
0. Install package
1. Create database: If running this for the first time: python -m db_init
2. Entry point: activate Tkinter GUI: python -m gui
3. Start using the application!



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
2) To implement analysis results, initialize tables in SQLite
    - syntax
    - sentiment
    - semantic


### DB Implementation Schematic:

<img width="477" alt="db_structure" src="https://user-images.githubusercontent.com/85393645/226218750-db729dcb-bfe4-406a-b301-524ba9d1d901.png">


* Note: run unit tests sequentially for correct 
* Note: to start running unit tests (automated in actions script)
    Step 1: run "python -m db_del" to delete possibly existing database in path and start over
    Step 2: run "python -m db_init" to initialize database
    Step 3: run "pytests"
    
### Sample File Entry

<img width="349" alt="file_entry" src="https://user-images.githubusercontent.com/85393645/226230415-335cc4bd-d20a-45e4-a53f-8e98a7333f82.png">


### Sample Syntax Parser Entry

<img width="714" alt="syntax_entry" src="https://user-images.githubusercontent.com/85393645/226230390-84455f0b-24c0-4bc0-abbc-6059e5f62f41.png">


## Phase 4: Multi-threading & Queues
### Objective: To implement a threading structure to support asynchronous multi-tasking of the PDF and NLP analysis via queues, async calls, and callbacks.

### Design:
1) Implementing a general Thread class
2) Building a queue to process PDF analysis and NLP analysis
3) Building support in uploader, nlp, and news ingester modules (APIs) to multi-thread.

### Ideas & Design:
    - implement general News_Thread class: general class to take in requests (wih func and func arg)
    as arguments, create a thread (& keep up with thread id), which will run the actual func
    such as upload pdf. Upon thread completion, calls callback function
    - implement running queue (perhaps in a class or as a global variable)
    - callback functions with threads (callback, ex. can decrement threads_active)
    callback as means of communication between main & new threads. will send output etc back
    - PDF and NLP analyzer will have two individual running queues, of which files will be set as News_Thread (implemented class in threads_wrapper.py) objects to be multi-threaded. the queues will be passed into as part of the News_Thread init
    - each function takes in queue as parameter for News_Thread class to take in

### Results: 
*Multi-threaded implementation of NLP and PDF analyzer using a threading queue*
Please refer to **logger.log** for some logged multi-threading results.

    
### Architectural Design
**Relational Database: SQLite for 1) Users (Accounts), 2) File**
*This design choice is based on the straightforward relationship between users and files that we define: 1 user to many files. The users and files tables are linked by the userID key, and each table contains attributes that can be easily accessed via a query.*
1) Users: A relational database is useful here. We store a table of users, identifiable by user_id as the primary key. We have the following tables:
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
3) Syntax: analyze by whole document/file
    - fileID
    - number of paragraphs
    - number of words
    - date created
    - file summary
    - keyword 1
    - keyword 2
    - keyword 3
4) Semantic:analyze by paragraph
    - fileID
    - paragraph #
    - summary
    - keyword 1
    - keyword 2
5) Sentiment: analyze by paragraph
    - fileID
    - paragraph #
    - sentiment (positive, negative, or neutral)


## Supplementary/Notes
- Python SQLite tutorial: https://www.tutorialspoint.com/sqlite/sqlite_python.htm
- some SQL tables allow you to put JSON entries (but some not supported) so if you want multiple entries in a single record (ex. 1 paragraph, multiple keywords)
SQL: not that good for "search-for-field"
- Document Database: MongoDB "Data is stored in collections that are analogous to MySQL tables. A collection is a group of documents (a set of key value pairs) and can consist of many documents in which data is stored in JSON format of key-value" https://www.knowi.com/blog/mongodb-vs-sql/ 
- Azure Storage Blob is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that does not adhere to a particular data model or definition, such as text or binary data. https://azure.microsoft.com/en-us/products/storage/blobs 
- good correspondence between SQL & NoSQL DB! (& good MongoDB tutorial) https://medium.com/nerd-for-tech/all-basics-of-mongodb-in-10-minutes-baddaf6b6625 
- https://docs.python.org/3/library/sqlite3.html 
- https://github.com/mongodb-developer/pymongo-fastapi-crud 
- https://stackoverflow.com/questions/35160417/threading-queue-working-example 
- https://realpython.com/intro-to-python-threading/
- https://developers.google.com/calendar/api/quickstart/python
