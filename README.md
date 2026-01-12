# personal-library-db

Python script got from this link: https://learndataanalysis.org/source-code-import-multiple-csv-files-data-files-to-sql-server-with-python/ but enhanced some from Gemini to fit SQL Server  

Preqs: SQL Server and SQL Server Management Studio:  https://learn.microsoft.com/en-us/ssms/install/install  

Designed a database to manage and track my Goodreads book library with details such as authors, books, genres and reading progress. 

How to create a user in SSMS: https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-ver17  

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

# To download and use
git clone https://github.com/JWT890/personal-library-database.git and then cd personal-library-datbase  
To verify:  
USE [personal-library]  
GO  

SELECT TABLE_NAME  
FROM INFORMATION_SCHEMA.TABLES  
WHERE TABLE_TYPE = 'BASE TABLE';  

# Importing from Goodreads  
Go to Goodreads.com and go to my books and look for Import and export button:  
<img width="206" height="539" alt="image" src="https://github.com/user-attachments/assets/6f8bcef0-e376-41c3-94f1-7973e1a026df" />  
Click on it and find the export library button up top and click on it.  
After doing so, run the downloadble python script from above after creating a user account in SQL Server and run it. You will have to insert the datbase from the csv/excel file into the respective databases for author, book, and genre.  

# Sample Queries
View all with authors
SELECT b.title, a.author_name, b.published_year, b.rating, b.status  
FROM dbo.books b
INNER JOIN dbo.Authors a ON b.author_id = a.author_id  
ORDER BY b.title;  
<img width="774" height="873" alt="image" src="https://github.com/user-attachments/assets/fc07b1ba-0a4d-4767-ad5f-da5770d896e7" />  

Count all status books  
SELECT status, COUNT(*) as count  
FROM dbo.Books
GROUP BY status;
<img width="694" height="1017" alt="image" src="https://github.com/user-attachments/assets/72c46058-9d65-46f7-a14e-aa23fc967a5b" />  

*Note the Python import might have messed up a little bit becauses of duplicates but it is fine*




