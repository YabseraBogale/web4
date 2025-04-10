import sqlite3
import os
from google import genai

class gemini():

    def __init__(self):

        try:
            self.connection=sqlite3.Connection("database.db",check_same_thread=False)
            self.pointer=self.connection.cursor()
            self.client=genai.Client(api_key=os.getenv("gemini"))

        except Exception as e:
            print(e)

    def ArticleGenarate(self,topic):
        try:
            if self.PrevoiusQuery(topic)==False:
                return self.GetQuery(topic)
            statment="Insert into Gemini(topic,response) values(?,?)"
            response = self.client.models.generate_content(model="gemini-2.0-flash", contents=str(topic).lower())
            self.pointer.execute(statment,(topic,response.text))
            self.connection.commit()
            return self.GetQuery(topic)
        except Exception as e:
            return str(e)
        
    def PrevoiusQuery(self,topic):
        try:
            statment="SELECT Count(topic) from Gemini where topic=?"
            self.pointer.execute(statment,(topic,))
            result=self.pointer.fetchone()
            if result[0]==1:
                return True
            else:
                return False
        except Exception as e:
            return str(e)
    
    def GetQuery(self,topic):
        try:
            statment="select response from Gemini where topic=?"
            self.pointer.execute(statment,(topic))
            result=self.pointer.fetchone()
            return result[0]
        except Exception as e:
            return str(e)
        
