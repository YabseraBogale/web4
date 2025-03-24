import sqlite3

class Database():
    def __init__(self):
        
        try:
            self.connection=sqlite3.Connection("database.db",check_same_thread=False)
            self.pointer=self.connection.cursor()
        except Exception as e:
            print(e)

    def create_table_heee(self):

        try:
            statement="""
                    create table HEEE(
                        question text not null primary key,
                        choice_a text not null,
                        choice_b text not null,
                        choice_c text not null,
                        choice_d text not null,
                        answer text not null,
                        explanation text not null
                    )

            """
            self.pointer.execute(statement)
            self.connection.commit()
            return True
        
        except Exception as e:
            print(e)
            return False

    
    


