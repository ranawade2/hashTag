#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################

from sets import Set

def fetchByTag(tag):
	#tag --> takes one tag at a time
	# Returns a SET of data (splitted CSV)



	######## DEFINE  LATER #########




def intersection(tags_list):

	mainSet = Set()

	#tags_list ===>> List of tags sent by user
	for tag in tags_list:
		tempSet = Set(fetchByTag(tag))
		#Create a tempSet obj with List as set input
		if len(mainSet) == 0:
			mainSet = tempSet
		else:
			mainSet = mainSet & tempSet
	return list(mainSet)