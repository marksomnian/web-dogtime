import sys, mysql.connector

userId = sys.argv[1]
startDateTime = sys.argv[2]
endDateTime = sys.argv[3]

print userId, startDateTime, endDateTime

cnx = mysql.connector.connect(user='testing123', password='123',
						host='127.0.0.1',
						database='dogtime_dev')
cnx.close()

