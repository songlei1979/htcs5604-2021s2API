from Classes.DB import DB

class ProductCategory:
    def __init__(self, categoryID, categoryname):
        self.categoryID = categoryID
        self.categoryname = categoryname

    def insert(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "INSERT INTO productcategory (categoryID, categoryname) "
        sql += "VALUES (null, '"+self.categoryname+"')"
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount)+ " record inserted."

    def update(self, categoryname):
        db = DB()
        cursor = db.connection.cursor()

        sql = "UPDATE productcategory SET categoryname = '"+categoryname+"'"
        sql += " WHERE categoryID = " + str(self.categoryID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) affected."

    def remove(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "DELETE FROM productcategory WHERE categoryID = " + str(self.categoryID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) deleted."

