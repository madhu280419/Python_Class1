import sqlite3

# Connect to SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create a table for books

cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
            )
        ''')

#Insert a book into the table

cursor.execute("INSERT INTO BOOKS (title, author, year) VALUES (?, ?, ?)",
               ("Art of napping at work", "Jaunty", 2022))

cursor .execute("INSERT INTO BOOKS (title, author, year) VALUES (?, ?, ?)",
                ("How to loose friends", "Pranay", 2024))


#SELECT ALL BOOKS 

print("All books in the library: ")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)
    
#Update

cursor.execute("UPDATE books SET author = ? WHERE title = ?", ("Praveen", "How to loose friends"))

#select book by year

print("after update")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)
    
#delete 

cursor.execute("DELETE FROM books WHERE title = ?", ("How to loose friends",))

#select  after delete 
print("after delete a book")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)
    

