import sys, mysql.connector
dogWalker = sys.argv[1]
startWalkArg = sys.argv[2]
if (startWalkArg == 'true'):
    startWalk = True
else:
    startWalk = False

print dogWalker, startWalk

cnx = mysql.connector.connect(user='testing123', password='123',
						host='127.0.0.1',
						database='dogtime_dev')

cnx.close()
