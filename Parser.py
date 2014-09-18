#####################################################################################################################
#											HASHTAG.py - HashTagging for dummies									#
#####################################################################################################################


#***************************************#

def parse_data_tags(data, tags_string):

	# data = userid
	# tags_string = "#tag1 #tag2 #tag3 #tag4"

	tags = tags_string.split(" ")

	tags = [tag.split("#")[1] for tag in tags]

	tags.sort()	

	# for CSV
	# tags_csv = ",".join(tags)

	print tags

	return data, tags

#***************************************#

def parse_tags1(data_tags_string):

	# data_tags_string = "Hello World #tag1 #tag2 #tag3 #tag4 Welcome Harish"

	tags = data_tags_string.split(" ")

	tags = [tag.split("#")[1] for tag in tags if tag[0] == "#"]

	tags.sort()	

	# for CSV
	# tags_csv = ",".join(tags)

	print tags

	return tags

#***************************************#

def parse_tags2(data_tags_string):

	# data_tags_string = "Hello World #tag1 #tag2 #tag3 #tag4 Welcome Harish"

	tags = data_tags_string.split("#")

	del tags[0]

	tags = [tag.split(" ")[0] for tag in tags]

	tags.sort()	

	# for CSV
	# tags_csv = ",".join(tags)

	print tags

	return tags

#***************************************#

parse_data_tags("ranawade2", "#java #cpp #py #php")

print 

parse_tags1("Hello World #ase #face #slac #blr Welcome Harish")

print

parse_tags2("Hello World #ase #face #slac #blr Welcome Harish")


