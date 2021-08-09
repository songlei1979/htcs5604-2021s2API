from Classes.DB import DB
from Classes.Order import Order
from Classes.Orderline import Orderline
from Classes.Outlet import Outlet
from Classes.Product import Product
from Classes.ProductCategory import ProductCategory


class DataShow:
    def products(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM product order by Productname"
        cursor.execute(sql)
        result = cursor.fetchall()
        products = []
        for p in result:
            product = Product(p[0], p[1], p[2], p[3], p[4], p[5])
            products.append(product.__dict__)
        return products

    def productsByCategory(self, categoryID):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM product where CategoryID = "+ str(categoryID) +" order by Productname"
        cursor.execute(sql)
        result = cursor.fetchall()
        products = []
        for p in result:
            product = Product(p[0], p[1], p[2], p[3], p[4], p[5])
            products.append(product.__dict__)
        return products

    def product(self, ProductID):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM product where ProductID = " + str(ProductID)
        cursor.execute(sql)
        result = cursor.fetchall()
        for p in result:
            product = Product(p[0], p[1], p[2], p[3], p[4], p[5])
            return product.__dict__

    def productCategories(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM productcategory"
        cursor.execute(sql)
        result = cursor.fetchall()
        categories = []
        for c in result:
            category = ProductCategory(c[0], c[1])
            categories.append(category.__dict__)
        return categories

    def productCategory(self, categoryID):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM productcategory where categoryID = "+str(categoryID)
        cursor.execute(sql)
        result = cursor.fetchall()
        for c in result:
            category = ProductCategory(c[0], c[1])
            return category.__dict__

    def outlets(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM outlet order by OutletName"
        cursor.execute(sql)
        result = cursor.fetchall()
        outlets = []
        for o in result:
            outlet = Outlet(o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7], o[8], o[9])
            outlets.append(outlet.__dict__)
        return outlets

    def outlet(self, OutletID):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM outlet where OutletID = " + str(OutletID)
        cursor.execute(sql)
        result = cursor.fetchall()
        for o in result:
            outlet = Outlet(o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7], o[8], o[9])
            return outlet.__dict__

    def orders(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM orders"
        cursor.execute(sql)
        result = cursor.fetchall()
        orders = []
        for o in result:
            order1 = Order(o[0], str(o[1]), o[2], str(o[3]), o[4])
            orders.append(order1.__dict__)
        return orders

    def order(self, OrderNumber):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM orders where OrderNumber = " + str(OrderNumber)
        cursor.execute(sql)
        result = cursor.fetchall()
        for o in result:
            order1 = Order(o[0], str(o[1]), o[2], str(o[3]), o[4])
            return order1.__dict__

    def orderlines(self):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM orderline"
        cursor.execute(sql)
        result = cursor.fetchall()
        orderlines = []
        for o in result:
            orderline = Orderline(o[0], o[1], o[2], o[3], o[4])
            orderlines.append(orderline.__dict__)
        return orderlines

    def orderline(self, OrderlineID):
        db = DB()
        cursor = db.connection.cursor()
        sql = "SELECT * FROM orderline where OrderlineID = " + str(OrderlineID)
        cursor.execute(sql)
        result = cursor.fetchall()
        for o in result:
            orderline = Orderline(o[0], o[1], o[2], o[3], o[4])
            return orderline.__dict__
