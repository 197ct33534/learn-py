import mysql.connector
import GuiDBConfig as guiConf

class MySQL():
    def connect(self):
       # connect by unpacking dictionary credentials
        conn = mysql.connector.connect(**guiConf.dbConfig)
    
        # create cursor 
        cursor = conn.cursor()    
            
        return conn, cursor
    def close(self, cursor, conn):
        cursor.close()
                
        # close connection to MySQL
        conn.close()    
    
    def showDBs(self):
        # connect to MySQL
        conn, cursor = self.connect()        
        
        # print results
        cursor.execute("SHOW DATABASES")
        print(cursor)
        print(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn)
    def createGuiDB(self):  
        # connect to MySQL
        conn, cursor = self.connect()
        
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MySQL.GUIDB))
        except mysql.connector.Error as err:
            print("Failed to create DB: {}".format(err))        

        # close cursor and connection
        self.close(cursor, conn) 
    def dropGuiDB(self): 
         # connect to MySQL
        conn, cursor = self.connect()
        try:
            cursor.execute(
                "DROP DATABASE {}".format(MySQL.GUIDB))
        except mysql.connector.Error as err:
            print("Failed to drop DB: {}".format(err))        

        # close cursor and connection
        self.close(cursor, conn)  
    def useGuiDB(self, cursor):
        cursor.execute("USE pythonnangcao")
    def createTables(self):
        # connect to MySQL
        conn, cursor = self.connect()
    
        self.useGuiDB(cursor)
        
        # create Table inside DB
        cursor.execute("CREATE TABLE Books (       \
              Book_ID INT NOT NULL AUTO_INCREMENT, \
              Book_Title VARCHAR(25) NOT NULL,     \
              Book_Page INT NOT NULL,              \
              PRIMARY KEY (Book_ID)                \
            ) ENGINE=InnoDB")
              # create second Table inside DB
        cursor.execute("CREATE TABLE Quotations ( \
                Quote_ID INT AUTO_INCREMENT,      \
                Quotation VARCHAR(250),           \
                Books_Book_ID INT,                \
                PRIMARY KEY (Quote_ID),           \
                FOREIGN KEY (Books_Book_ID)       \
                    REFERENCES Books(Book_ID)     \
                    ON DELETE CASCADE             \
            ) ENGINE=InnoDB")
        self.close(cursor, conn)   
    def dropTables(self):
          # connect to MySQL
        conn, cursor = self.connect()
    
        self.useGuiDB(cursor)
        
        cursor.execute("DROP TABLE quotations")
        cursor.execute("DROP TABLE books")   
    
        # close cursor and connection
        self.close(cursor, conn)    
  
    def showTables(self):
        # connect to MySQL
        conn, cursor = self.connect()
    
        # show Tables from guidb DB
        cursor.execute("SHOW TABLES FROM pythonnangcao") 
        print(cursor.fetchall())
        
        # close cursor and connection
        self.close(cursor, conn)       
    def insertBooks(self,title, page, bookQuote):
          # connect to MySQL
        conn, cursor = self.connect()
        
        self.useGuiDB(cursor)
        
        # insert data
        cursor.execute("INSERT INTO books (Book_Title, Book_Page) VALUES (%s,%s)", (title, page))

        # last inserted auto increment value   
        keyID = cursor.lastrowid 
        # print(keyID)
                
        cursor.execute("INSERT INTO quotations (Quotation, Books_Book_ID) VALUES (%s, %s)", \
                       (bookQuote, keyID))
                
        # commit transaction
        conn.commit ()

        # close cursor and connection
        self.close(cursor, conn)

    def insertBooksExample(self):
         # connect to MySQL
        conn, cursor = self.connect()
        
        self.useGuiDB(cursor)
        
        # insert hard-coded data
        cursor.execute("INSERT INTO books (Book_Title, Book_Page) VALUES ('Design Patterns', 17)")
        
        # last inserted auto increment value   
        keyID = cursor.lastrowid 
        print(keyID)
                
        cursor.execute("INSERT INTO quotations (Quotation, Books_Book_ID) VALUES (%s, %s)", \
                       ('Programming to an Interface, not an Implementation', keyID))
        
        # commit transaction
        conn.commit ()
    
        # close cursor and connection
        self.close(cursor, conn)   
    def showBooks(self):
         # connect to MySQL
        conn, cursor = self.connect()    
        
        self.useGuiDB(cursor)    
        
        # print results
        cursor.execute("SELECT * FROM Books")
        allBooks = cursor.fetchall()
        print(allBooks)

        # close cursor and connection
        self.close(cursor, conn)   
        
        return allBooks  
    def showColumns(self):
        # connect to MySQL
        conn, cursor = self.connect()   
        
        self.useGuiDB(cursor)      
         
        # execute command
        cursor.execute("SHOW COLUMNS FROM quotations")
        print(cursor.fetchall())
        
        print('\n Pretty Print:\n--------------') 
        from pprint import pprint
        # execute command
        cursor.execute("SHOW COLUMNS FROM quotations")
        pprint(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn)
    def showData(self):
         # connect to MySQL
        conn, cursor = self.connect()   
        
        self.useGuiDB(cursor)      
         
        # execute command
        cursor.execute("SELECT * FROM books")
        print(cursor.fetchall())

        cursor.execute("SELECT * FROM quotations")
        print(cursor.fetchall())
        
        # close cursor and connection
        self.close(cursor, conn)     


if __name__ == '__main__':       
    mySQL = MySQL()
    try:
        # mySQL.showDBs();
        # mySQL.showTables()
         mySQL.showBooks()
        # mySQL.insertBooks('Design Patterns', 7, 'Programming to an Interface, not an Implementation')
        #mySQL.insertBooks('xUnit Test Patterns', 31, 'Philosophy of Test Automation')
    
    except Exception as ex:
        print(ex)