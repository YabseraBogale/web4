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

    def MakeArticleGenarate(self,topic):
        try:
            statment="Insert into Gemini(topic,response) values(?,?)"
            response = self.client.models.generate_content(model="gemini-2.0-flash", contents=str(topic).lower())
            self.pointer.execute(statment,(topic,response.text))
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)