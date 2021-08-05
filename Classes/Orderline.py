from Classes.DB import DB

class Orderline:
    def __init__(self, OrderlineID, OrderNumber, ProductID, Quantityordered, Quantitysupplied):
        self.OrderlineID = OrderlineID
        self.OrderNumber = OrderNumber
        self.ProductID = ProductID
        self.Quantityordered = Quantityordered
        self.Quantitysupplied = Quantitysupplied

    def insert(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "INSERT INTO orderline (OrderlineID, OrderNumber, ProductID, Quantityordered, Quantitysupplied) "
        sql += "VALUES ( null , " + str(self.OrderNumber) + ", "
        sql += str(self.ProductID) + ", "
        sql += str(self.Quantityordered) + ","
        sql += str(self.Quantitysupplied) + ")"
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record inserted."

    def update(self, OrderNumber, ProductID, Quantityordered, Quantitysupplied):
        db = DB()
        cursor = db.connection.cursor()

        sql = "UPDATE orderline SET OrderNumber = " + str(OrderNumber) + ", "
        sql += "ProductID = " + str(ProductID) + ", "
        sql += "Quantityordered = " + str(Quantityordered) + ", "
        sql += "Quantitysupplied = " + str(Quantitysupplied) + " "
        sql += "WHERE OrderlineID = " + str(self.OrderlineID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) affected."

    def remove(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "DELETE FROM orderline WHERE OrderlineID = " + str(self.OrderlineID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) deleted."

