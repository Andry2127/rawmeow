import sqlite3

def create_table():
    try:
        sql_con = sqlite3.connect("pizzas.db")
        cursor = sql_con.cursor()

        with open("data/create_table.sql") as file:
            query = file.read()

        cursor.execute(query)
        sql_con.commit()
        cursor.close()

    except sqlite3.Error as error:
        print(f"Error: {error}")

    finally:
        if sql_con:
            sql_con.close()

def get_Pizzas():
    try:
        sql_con = sqlite3.connect("pizzas.db")
        cursor = sql_con.cursor()

        query = "SELECT * FROM Pizzas"

        cursor.execute(query)
        pizzas = cursor.fetchall()
        cursor.close()
        return pizzas
    

    except sqlite3.Error as error:
        print(f"Error: {error}")

    finally:
        if sql_con:
            sql_con.close()
create_table()