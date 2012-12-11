import mysql.connector
cnx = mysql.connector.connect(user='testing123', password='123',
						host='127.0.0.1',
						database='dogtime_dev')
cnx.close()
