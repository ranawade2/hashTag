#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################

from sets import Set



def search(tags_list, type):
	if type == "intersection":
		return intersection(tags_list)

	elif type == "union":
		return union(tags_list)

	elif type == "symmetricDifference":
		return symmetricDifference(tags_list)

	else:
		return

#Fetch values for Each tag and return List of values
def fetchByTag(tag):
	return
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
	#tags_list ===>> Li st of tags sent by user
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

#### Biased Searching that takes 2 list parameters Ex:--- [#aamir  & #khan] - [#bollywood | #actor] ####
def searchBiasedDifference(positive_tags_list, negetive_tags_list):
	#Taking Intersection of all Positive Items and Union of all Negetive Items and find biased DIfference
	positive_temp_set = Set(intersection(positive_tags_list))	
	negetive_temp_set = Set(union(negetive_tags_list))

	#finding biased diff of both 
	mainSet = positive_temp_set - negetive_temp_set

	return list(mainSet)



# ######### TEST CASES ########

# print intersection(["sameer","rahul","adi"])
# print union(["sameer","rahul","adi"])
# print searchBiasedDifference(["sameer","adi"], ["rahul","sample"])
# print symmetricDifference(["sameer","rahul","adi"])

# ######### TEST CASES ########
