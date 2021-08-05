from Classes.DB import DB


class Product:
    def __init__(self, ProductID, Productbarcord, Productname, Unitprice, Stocklevel, CategoryID):
        self.ProductID = ProductID
        self.Productbarcord = Productbarcord
        self.Productname = Productname
        self.Unitprice = Unitprice
        self.Stocklevel = Stocklevel
        self.CategoryID = CategoryID

    def insert(self):
        db = DB()
        cursor = db.connection.cursor()

        sql = "INSERT INTO product (ProductID, Productbarcord, Productname, Unitprice, Stocklevel, CategoryID) "
        sql += "VALUES (null, '"+self.Productbarcord+"', "
        sql += "'"+self.Productname+"', "
        sql += str(self.Unitprice) + ","
        sql += str(self.Stocklevel) + ", "
        sql += str(self.CategoryID) + ")"
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount)+ " record inserted."

    def update(self, Productbarcord, Productname, Unitprice, Stocklevel, CategoryID):
        db = DB()
        cursor = db.connection.cursor()

        sql = "UPDATE product SET Productbarcord = '"+Productbarcord+"', "
        sql += "Productname = '"+Productname+"', "
        sql += "Unitprice = " + str(Unitprice) + ", "
        sql += "Stocklevel = " + str(Stocklevel) + ", "
        sql += "CategoryID = " + str(CategoryID) + " "
        sql += " WHERE ProductID = " + str(self.ProductID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) affected."

    def remove(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "DELETE FROM product WHERE ProductID = " + str(self.ProductID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) deleted."


