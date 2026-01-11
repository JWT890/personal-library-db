USE [personal-library];
GO

-- 1. Drop the table if it exists so you can start fresh
IF OBJECT_ID('dbo.goodreads_library_export', 'U') IS NOT NULL
    DROP TABLE dbo.goodreads_library_export;
GO

-- 2. Create the table structure
CREATE TABLE dbo.goodreads_library_export (
    [Book Id] INT PRIMARY KEY,         -- Unique ID for every book
    [Title] NVARCHAR(MAX),
    [Author] NVARCHAR(MAX),
    [Author l-f] NVARCHAR(MAX),
    [Additional Authors] NVARCHAR(MAX),
    [ISBN] NVARCHAR(100),              -- Stored as text to handle the ="..." format
    [ISBN13] NVARCHAR(100),
    [My Rating] INT,
    [Average Rating] FLOAT,
    [Publisher] NVARCHAR(MAX),
    [Binding] NVARCHAR(255),
    [Number of Pages] INT,
    [Year Published] INT,
    [Original Publication Year] FLOAT, -- Float handles empty cells better than INT
    [Date Read] NVARCHAR(100),
    [Date Added] NVARCHAR(100),
    [Bookshelves] NVARCHAR(MAX),
    [Bookshelves with positions] NVARCHAR(MAX),
    [Exclusive Shelf] NVARCHAR(255),
    [My Review] NVARCHAR(MAX),
    [Spoiler] NVARCHAR(MAX),
    [Private Notes] NVARCHAR(MAX),
    [Read Count] INT,
    [Owned Copies] INT
);
GO

-- 3. Verify the table was created
SELECT TOP 0 * FROM dbo.goodreads_library_export;