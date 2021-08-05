import mysql.connector

class DB:
    def __init__(self):
        self.connection = mysql.connector.connect(host='ro2padgkirvcf55m.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                             database='zog3zrnr5immqv2x',
                                             user='ljin5ogk653pw6mq',
                                             password='zlteqsqk66bzqcr5')
    def test_success(self):
        if self.connection.is_connected():
            return "connected"
        return "not connected"

