#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################

from sets import Set

#Fetch values for Each tag and return List of values
def fetchByTag(tag):
	#tag --> takes one tag at a time
	# Returns a SET of data (splitted CSV)
	######## DEFINE  LATER #########


# ############################################
# 	if tag == "rahul":
# 		return [1,2,3,4,5,6]
# 	elif tag == "sameer":
# 		return [1,2,3,10,20,30]
# 	elif tag == "sample":
# 		return [10]
# 	else:
# 		return [1,2,5,10,20,50]
# #########################################

def intersection(tags_list):
	mainSet = Set()
	#tags_list ===>> List of tags sent by user
	for tag in tags_list:
		tempSet = Set(fetchByTag(tag)) #function call to get List of Values of each Tag
		if len(mainSet) == 0:
			mainSet = tempSet
		else:
			mainSet = mainSet & tempSet
	return list(mainSet)


def union(tags_list):
	mainSet = Set()
	#tags_list ===>> List of tags sent by user
	for tag in tags_list:
		tempSet = Set(fetchByTag(tag)) #function call to get List of Values of each Tag
		if len(mainSet) == 0:
			mainSet = tempSet
		else:
			mainSet = mainSet | tempSet
	return list(mainSet)


def biasedDifference(positive_tags_list, negetive_tags_list):
	#Taking Intersection of all Positive Items and Union of all Negetive Items and find biased DIfference
	positive_temp_set = Set(intersection(positive_tags_list))	
	negetive_temp_set = Set(union(negetive_tags_list))

	#finding biased diff of both 
	mainSet = positive_temp_set - negetive_temp_set

	return list(mainSet)


def symmetricDifference(tags_list):
	mainSet = Set()
	#tags_list ===>> List of tags sent by user
	for tag in tags_list:
		tempSet = Set(fetchByTag(tag)) #function call to get List of Values of each Tag
		if len(mainSet) == 0:
			mainSet = tempSet
		else:
			mainSet = mainSet ^ tempSet
	return list(mainSet)



# ######### TEST CASES ########

# print intersection(["sameer","rahul","adi"])
# print union(["sameer","rahul","adi"])
# print biasedDifference(["sameer","adi"], ["rahul","sample	"])
# print symmetricDifference(["sameer","rahul","adi"])

# ######### TEST CASES ########
