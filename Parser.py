#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################


#***************************************#

def parse(tags_string):

	# tags_string = "#tag1 #tag2 #tag3 #tag4"

	tags = tags_string.split(" ")

	tags_list = []

	for tag in tags:
		temp = tag.split("#")[1]

		tags_list.append(temp);

	# sort in alphabetical order
	tags_list.sort()

	# for CSV
	# tags_csv = ",".join(tags_list)

	return tags_list

#***************************************#

parse("#ase #face #slac #blr")



