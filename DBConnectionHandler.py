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
	if databaseType == "mysql":
		import MySQLdb
		db = MySQLdb.connect(host=hostname,
						user=username,
						passwd=password,
						db=dbname)
		cur = db.cursor(MySQLdb.cursors.DictCursor)
		db.autocommit(autocommit)
		return cur
	
	## POSTGRESQL CONNECTION BLOCK ##																				#
	
	elif databaseType == "postgresql":
		import psycopg2
		db = MySQLdb.connect(host=hostname,
						user=username,
						password=password,
						database=dbname)
		cur = db.cursor(MySQLdb.cursors.DictCursor)
		db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
		return cur
	## SQLITE 3 CONNECTION BLOCK ##																					#

	elif databaseType=="sqlite3":
		import sqlite3
		db = sqlite3.connect(dbname)
		cur = db.cursor()
		return cur



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