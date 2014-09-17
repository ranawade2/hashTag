#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################

##	IMPORT SECTION	##																								#

#####################################################################################################################
##	GLOBAL DECLARATION SECTION	##																					#

db=None

#####################################################################################################################
#
# Function Definition to start a database connection to an existing database(mysql,postgresql)
# or a new database(sqlite 3).
#
def startCon(hostname="",username="",password="",dbname="HashTagDB",autocommit=True,databaseType="sqlite3"):
	global db
	## MYSQL CONNECTION BLOCK ##																					#
	try:

		if databaseType == "mysql":
			import MySQLdb
			db = MySQLdb.connect(host=hostname,
							user=username,
							passwd=password,
							db=dbname)
			cur = db.cursor(MySQLdb.cursors.DictCursor)
			db.autocommit(autocommit)
			return cur
	except:
		return None
	## POSTGRESQL CONNECTION BLOCK ##																				#
	try:
		elif databaseType == "postgresql":
			import psycopg2
			db = MySQLdb.connect(host=hostname,
							user=username,
							password=password,
							database=dbname)
			cur = db.cursor(MySQLdb.cursors.DictCursor)
			db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
			return cur
	except:
		return None
	## SQLITE 3 CONNECTION BLOCK ##																					#
	try:
		elif databaseType=="sqlite3":
			import sqlite3
			db = sqlite3.connect(dbname)
			cur = db
			return cur
	except:
		return None



#
# Function Definition to close a database connection to a connected database.
#

def closeCon():
	global db
	try:
		db.close()
		return 0
	except:
		return -1