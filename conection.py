import mysql.connector
from mysql.connector import Error



class Storage():
    def __init__(self):
        connection = mysql.connector.connect(host='localhost',
                                             database='db_sales',
                                             user='root',
                                             password='rootpassword')

    def update_sales(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='db_sales',
                                                 user='root',
                                                 password='rootpassword')

            sql_select_Query = "select * from sales"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()




        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
        return (records)

    def show_ranking_sales(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='db_sales',
                                                 user='root',
                                                 password='rootpassword')

            sql_select_Query = "select * from sales order by sale_value "
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()




        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
        return (records)

    def get_seller(self, name):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='db_sales',
                                                 user='root',
                                                 password='rootpassword')

            sql_select_Query = "select id from seller where name = '{}' ".format(name)
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            return records

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")


    def populate(self, produto, seller_name,costumer_name,sale_value):
        seller_name = str(seller_name)
        sale_value = str(sale_value)
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='db_sales',
                                                 user='root',
                                                 password='rootpassword')

            sql_select_query = "INSERT INTO sales (product,seller_id,costumer_name,sale_value)  VALUES(%s,%s,%s,%s)"#.format(produto, seller_name, costumer_name, sale_value)
            val = (produto, seller_name, costumer_name, sale_value)
            cursor = connection.cursor()
            cursor.execute(sql_select_query,val)

            connection.commit()




        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
        return ("registered.")


    def delete(self, sale_id):

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='db_sales',
                                                 user='root',
                                                 password='rootpassword')

            sql_select_query = "DELETE FROM sales WHERE id = %s"
            val = (sale_id)
            cursor = connection.cursor()
            cursor.execute(sql_select_query,val)

            connection.commit()




        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
        return ("Deleted.")




