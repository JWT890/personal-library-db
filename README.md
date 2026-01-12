# personal-library-db

Python script got from this link: https://learndataanalysis.org/source-code-import-multiple-csv-files-data-files-to-sql-server-with-python/ but enhanced some from Gemini to fit SQL Server  

Preqs: SQL Server and SQL Server Management Studio:  https://learn.microsoft.com/en-us/ssms/install/install  

Designed a database to manage and track my Goodreads book library with details such as authors, books, genres and reading progress. 

# Database Schema
Author:  
author_id (PK, INT, Idenity) - Unique Identifier  
first_name (VARCHAR, NOT NULL) - first name  
last_name (VARCHAR, NOT NULL), last name  
author_name (VARCHAR) - full name  

Books:  
book_id (PK, INT, Identity) Unqiue Identifier  
title (VARCHAR, NOT NULL) Book title  
author_id (INT, NOT NULL) References author table  
genre_id (INT, NOT NULL) References Genres table  
published_year (INT) Year of publication  
pages (INT) Number of pages  
isbn (VARCHAR) ISBN number  
format (VARCHAR) Book format (Paperback, Hardcover, etc)  
condition (VARCHAR) Physical condition  
date_acquired (DATE) when added  
status (VARCHAR) reading status  
date_started (VARCHAR) when started reading  
date_completed (VARCHAR) when finished reading  
rating (INT, CHECK: 0-5): rating of book (most finicky section since i had it first as rating of 1-10)  
review (TEXT) review  
notes (TEXT) personal notes  

Genres  
genre_id (PK, INT, Identity) - unique identifier  
name (VARCHAR, NOT NULL) Genre name  

Relationships:  
Books -> Authors (Many to one via author_id)  
Books -> Genres (Many to one via genre_id)  


