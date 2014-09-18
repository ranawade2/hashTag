#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################


#***************************************#

def parse(tags_string):

	# tags_string = "#tag1 #tag2 #tag3 #tag4"

	tags = tags_string.split(" ")

	tags = [tag.split("#")[1] for tag in tags]

	tags.sort()	

	# for CSV
	# tags_csv = ",".join(tags)

	return tags

#***************************************#

parse("#ase #face #slac #blr")



