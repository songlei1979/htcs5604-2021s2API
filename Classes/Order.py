from Classes.DB import DB

class Order:
    def __init__(self, OrderNumber, OrderDate, OrderStatus, DeliveyDate, OutletID):
        self.OrderNumber = OrderNumber
        self.OrderDate = OrderDate
        self.OrderStatus = OrderStatus
        self.DeliveyDate = DeliveyDate
        self.OutletID = OutletID

    def insert(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "INSERT INTO orders (OrderNumber, OrderDate, OrderStatus, DeliveyDate, OutletID) "
        sql += "VALUES ("+str(self.OrderNumber)+", '"+self.OrderDate+"', "
        sql += "'"+self.OrderStatus+"', "
        sql += "'" + self.DeliveyDate + "', "
        sql += str(self.OutletID) + ")"
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount)+ " record inserted."

    def update(self, OrderDate, OrderStatus, DeliveyDate, OutletID):
        db = DB()
        cursor = db.connection.cursor()

        sql = "UPDATE orders SET OrderDate = '"+OrderDate+"', "
        sql += "OrderStatus = '"+OrderStatus+"', "
        sql += "DeliveyDate = '" + DeliveyDate + "', "
        sql += "OutletID = " + str(OutletID) + " "
        sql += "WHERE OrderNumber = " + str(self.OrderNumber)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) affected."

    def remove(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "DELETE FROM orders WHERE OrderNumber = " + str(self.OrderNumber)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) deleted."


