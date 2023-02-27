#Compulsory Task
#A program that can be used by a bookstore clerk

#Import statement to allow us to use SQLite with Python
import sqlite3  
   
#Using a try/except/finally clause to catch any exception in the code
try:

    # Creates a file called ebookstore with a SQLite3 DB
    db = sqlite3.connect('ebookstore_db')

    #Getting a cursor object
    cursor = db.cursor()

    #Creating a table called books with id, title, author and quantity columns
    cursor.execute('''
CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT,
Author TEXT, Qty INTEGER)
''')
    #Using the commit function to save changes to the database
    db.commit()
    
    #Function for printing the menu
    def display_menu():
        print('''\tWelcome to ebookstore menu
    \t 1. Enter Books
    \t 2. Update Books
    \t 3. Delete Books
    \t 4. Search Books
    \t 0. Exit''')

    #Function which takes values and adds a new record of books  
    def insert_book(i,t,a,q):
        cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
    VALUES(?,?,?,?)''', (i,t,a,q))
        print(f'Book: {i} added')
        
    #Using the cursor again to execute a SQL statement
    cursor = db.cursor()
    #Creating variables for records which we want to insert into the table
    id_1 = 3001
    title_1 = 'A Tale of Two Cities'

    author_1 = 'Charles Dickens'
    qty_1 = 30
    
    id_2 = 3002
    title_2 = "Harry Potter and the Philosopher's Stone"

    author_2 = 'J.K. Rowling'
    qty_2 = 40
    
    id_3 = 3003
    title_3 = 'The Lion, the Witch and the Wardrobe'

    author_3 = 'C.S. Lewis'
    qty_3 = 25
    
    id_4 = 3004
    title_4 = 'The Lord of the Rings'

    author_4 = 'J.R.R Tolkien'
    qty_4 = 37
    
    id_5 = 3005
    title_5 = 'Alice in Wonderland'

    author_5 = 'Lewis Carroll'
    qty_5 = 12

    #Insert book 1
    #Calling the function 
    insert_book(id_1,title_1,author_1,qty_1)
    
    #Insert book 2
    insert_book(id_2,title_2,author_2,qty_2)
    
    #Insert book 3
    insert_book(id_3,title_3,author_3,qty_3)
    
    #Insert book 4
    insert_book(id_4,title_4,author_4,qty_4)
    
    # Insert book 5
    insert_book(id_5,title_5,author_5,qty_5)

    #Using the commit function to save changes to the database
    db.commit()

    display_menu()
    while True:
        user_selection = int(input("Enter a number from the menu options above (0-4): "))
        if user_selection == 1:
            id_user = input("Enter the ID: ")
            title_user = input("Enter the title: ")
            author_user = input("Enter the author: ")
            qty_user = input("Enter the quantity: ")
            insert_book(id_user,title_user,author_user,qty_user)
            db.commit()

        elif user_selection == 2:
            id_user_upd = input("\n Enter the book ID: \n")
            user_update = input('''What do you want to update: 
            t - Title
            a - Author
            q - Quantity
            : ''')

            if user_update == "t":
                title_user_upd = input("\n Enter the updated title: \n")
                #updating the title
                cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''', (title_user_upd, id_user_upd))
                print(f'\n {id_user_upd} books title is now updated to: {title_user_upd} \n')
                db.commit()

            #updating the author
            elif user_update == "a":
                author_user_upd = input("\n Enter the updated author: \n")
                #Updating the author in the database
                cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''', (author_user_upd, id_user_upd))
                print(f'\n {id_user_upd} books author is now updated to: {author_user_upd} \n')
                db.commit()

            #updating the quantity
            elif user_update == "q":
                qty_user_upd = input("\n Enter the updated quantity: \n")
                #updating the quantity of books in the databse
                cursor.execute('''\n UPDATE books SET Qty = ? WHERE id = ? \n''', (qty_user_upd, id_user_upd))
                print(f'\n {id_user_upd} books quantity is now updated to: {qty_user_upd} \n')
                db.commit()

            else:
                print("\n Your user selection is invalid")
        
        #Delete books as per user id selection   
        elif user_selection == 3:
            id_delete = int(input("Enter the ID number for book you would like to delete: "))
            cursor.execute('''DELETE FROM books WHERE id = ? ''', (id_delete,))
            print('books %d deleted' %id_delete)
            db.commit()

        #Search for books
        elif user_selection == 4:
            id_selection = input("Enter the book id of the book: ")
            cursor.execute('''SELECT Title, Author, Qty FROM books WHERE id=?''', (id_selection,))
            books = cursor.fetchone()
            print(f'\n Data retrieved about books with id {id_selection}\n')
            print(books)
            db.commit()

        elif user_selection == 0:
            print('\n Goodbye!!!')
            exit()
                      
            db.commit()

        else:
            print("Your user selection is invalid")

# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    # Close the db connection
    db.close()

    
        
