import sqlite3

class heee():
    
    def __init__(self):
        try:
            self.connection=sqlite3.Connection("database.db",check_same_thread=False)
            self.pointer=self.connection.cursor()
        except Exception as e:
            print(e)
    def insert_into_heee(self,question,choice_a,choice_b,choice_c,choice_d,answer,explanation):
        try:
            statmemnt="Insert into HEEE(question,choice_a ,choice_b,choice_c,choice_d,answer,explanation) values(?,?,?,?,?,?,?);"
            self.pointer.execute(statmemnt,(question,choice_a,choice_b,choice_c,choice_d,answer,explanation,))
            self.connection.commit()
            return True
        except Exception as e:
            return False
    
    def get_random_100_question_heee(self):
        try:
            statment="SELECT * FROM HEEE ORDER BY RANDOM() LIMIT 100 OFFSET 1;"
            self.pointer.execute(statment)
            result=self.pointer.fetchall()
            return list(result)
        except Exception as e:
            return []
        
    def random_software_fact(self):
        try:
            statment="Select explanation FROM HEEE order by random() Limit 1 offset 1;"
            self.pointer.execute(statment)
            result=self.pointer.fetchall()
            return list(result)
        except Exception as e:
            return []
