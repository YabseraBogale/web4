import sqlite3

class newletter():

    def __init__(self):
        try:
            self.connection=sqlite3.Connection("database.db",check_same_thread=False)
            self.pointer=self.connection.cursor()
        except Exception as e:
            print(e)
    
    def insert_into_newletter(self,email):

        try:
            statment="insert into newletter(email) values(?)"
            self.pointer.execute(statment,(email,))
            self.connection.commit()
            return True
        except Exception as e:
            return False