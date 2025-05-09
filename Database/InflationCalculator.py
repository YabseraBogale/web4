import sqlite3

class inflation_calculator():

    def __init__(self):
        try:
            self.connection=sqlite3.Connection("database.db",check_same_thread=False)
            self.pointer=self.connection.cursor()
        except Exception as e:
            print(e)

    def calculator(self,amount,year_at,year_in,country):
        try:
            """
                Adjusted Amount = Initial Amount * (CPI in Target Year / CPI in Initial Year)

                Where:
                    Initial Amount: The amount of money you start with.
                    CPI in Initial Year: The price index value for the year you are starting from.
                    CPI in Target Year: The price index value for the year you want to adjust the money to.
                    Adjusted Amount: The equivalent value of the Initial Amount in the Target Year's currency value.
            """
            ###############                 amount*(year_at/year_in) ###################### country
            statment=f"""select Country_Name,({amount})*("{year_at}"/"{year_in}") from inflation_calculator where Country_Name="{country}" """
            self.pointer.execute(statment)
            result=self.pointer.fetchone()
            return result
        except Exception as e:
            return str(e)
        

print(inflation_calculator().calculator(150,"2010","1960","United States"))