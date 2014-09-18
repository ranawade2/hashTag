#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################
import DBConnectionHandler as dbcon

def UpdateTagValue(data,tagList):
	cur = dbcon.startCon(hostname="hashtags.db.10434227.hostedresource.com",username="hashtags",password="code4Db@ba",dbname="hashtags",autocommit=True,databaseType="mysql")
	booleanMap = checkIfTagsExists(cur,tagList)
	for (item,tag) in zip(booleanMap,tagList):
		print item,tag
		if item:
			cur.execute("SELECT data FROM tagStore WHERE tag=%s",(tag))
			commitdata = cur.fetchall()
			commitdata = commitdata[0]["data"]
			commitdata = lexiographicAdd(data,commitdata)
			cur.execute("UPDATE tagStore SET data='"+str(commitdata)+"' WHERE tag='"+str(tag)+"'")
			

		else:
			createTag(cur,tag,data)
			

# cur.execute("Insert INTO tagStore VALUES('java','2213,342,345345');")
# cur.execute("SELECT * FROM tagStore")
# print cur.fetchall()

def checkIfTagsExists(cur,tagList):
	booleanMap=[]
	for tag in tagList:
		cur.execute("SELECT * FROM tagStore WHERE tag=%s",tag)
		if cur.fetchall() ==():
			booleanMap.append(False)
		else:
			booleanMap.append(True)
	print booleanMap
	return booleanMap


def createTag(cur,tag,data):
	cur.execute("INSERT INTO tagStore (tag,data) VALUES (%s,%s)",(tag,data))

def lexiographicAdd(data,commitdata):
	Lcommitdata = commitdata.split(",")
	print Lcommitdata
	i=0
	for item in Lcommitdata:
		if(item > data):
			i = i+1
		else:
			break
	Lcommitdata.insert(i,data)
	print Lcommitdata
	commitdata = ",".join(Lcommitdata)
	return commitdata

UpdateTagValue("ndivandhya", ["python","java"])



