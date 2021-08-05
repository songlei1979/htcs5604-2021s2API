from Classes.DB import DB

class Outlet:
    def __init__(self, OutletID, OutletName, Streetaddress, Suburb, City, Postcode, ContactFirstName, ContactLastName, Emailaddress, PhoneNumber):
        self.OutletID = OutletID
        self.OutletName = OutletName
        self.Streetaddress = Streetaddress
        self.Suburb = Suburb
        self.City = City
        self.Postcode = Postcode
        self.ContactFirstName = ContactFirstName
        self.ContactLastName = ContactLastName
        self.Emailaddress = Emailaddress
        self.PhoneNumber = PhoneNumber

    def insert(self):
        db = DB()
        cursor = db.connection.cursor()

        sql = "INSERT INTO outlet (OutletID, OutletName, Streetaddress, Suburb, City, Postcode, ContactFirstName, ContactLastName, Emailaddress, PhoneNumber) "
        sql += "VALUES (null, '"+self.OutletName+"', "
        sql += "'" + self.Streetaddress+"', "
        sql += "'" + self.Suburb + "', "
        sql += "'" + self.City + "', "
        sql += "'" + self.Postcode + "', "
        sql += "'" + self.ContactFirstName + "', "
        sql += "'" + self.ContactLastName + "', "
        sql += "'" + self.Emailaddress + "', "
        sql += "'" + self.PhoneNumber + "')"
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount)+ " record inserted."

    def update(self, OutletName, Streetaddress, Suburb, City, Postcode, ContactFirstName, ContactLastName, Emailaddress, PhoneNumber):
        db = DB()
        cursor = db.connection.cursor()

        sql = "UPDATE outlet SET OutletName = '"+OutletName+"', "
        sql += "Streetaddress = '"+Streetaddress+"', "
        sql += "Suburb = '" + Suburb + "', "
        sql += "City = '" + City + "', "
        sql += "Postcode = '" + Postcode + "', "
        sql += "ContactFirstName = '" + ContactFirstName + "', "
        sql += "ContactLastName = '" + ContactLastName + "', "
        sql += "Emailaddress = '" + Emailaddress + "', "
        sql += "PhoneNumber = '" + PhoneNumber + "'"
        sql += " WHERE OutletID = " + str(self.OutletID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) affected."

    def remove(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "DELETE FROM outlet WHERE OutletID = " + str(self.OutletID)
        cursor.execute(sql)
        db.connection.commit()
        db.connection.close()
        return str(cursor.rowcount) + " record(s) deleted."

