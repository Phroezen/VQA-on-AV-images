import sys
import json
import spacy

nlp = spacy.load('en_core_web_sm')
denseInput = open('adjustedResults.json')
data = json.load(denseInput)
outputData = {}
outputData['predicates'] = []
outputData['boxes'] = []
index = 0
for caption in data['results'][2]['captions']:
	attribute1 = 'none'
	object1 = 'none'
	relation = 'none'
	attribute2 = 'none'
	object2 = 'none'
	caption_nlp = nlp(caption)
	for token in caption_nlp:
		if(token.tag_ == 'NN' or token.tag_ == 'NNS'):
			if(object1 == 'none'):
				object1 = token.text
				for child in token.children:
					if(child.tag_ == "JJ"):
						attribute1 = child.text
				if(token.head.tag_ == 'VBZ'):
					relation = token.head.text
				else:
					for child in token.children:
						if(child.tag_ == "VBN" or child.tag_ == "IN"):
							relation = child.text
							for addition in child.children:
								sum = 0
								detFlag = False
								for ends in addition.children:
									detFlag = (ends.tag_ == 'DT' or ends.tag_ == 'JJ')
									sum+=1
								if(sum > 0 and not (detFlag and sum == 1)):
									relation = relation + '_' + addition.text
						if(child.tag_ == "VBG"):
							relation = child.text
			else:
		 		object2 = token.text
		 		for child in token.children:
		 			if(child.tag_ == "JJ"):
		 				attribute2 = child.text
	predicateText = "property(" + str(relation) + ", attribute(" + str(attribute1) + ", " + str(object1) + "), attribute(" + str(attribute2) + ", " + str(object2) + "), box" + str(data['results'][2]['captionBoxes'][index][0]) + ", box" + str(data['results'][2]['captionBoxes'][index][1]) + ")"
	outputData['predicates'].append(predicateText)
	index += 1
index = 0
for box in data['results'][2]['boxes']:
	boxText = "property(box" + str(index) + ", " + str(data['results'][2]['boxes'][index][0]) + ", " + str(data['results'][2]['boxes'][index][1]) + ", " + str(data['results'][2]['boxes'][index][2]) + ", " + str(data['results'][2]['boxes'][index][3]) + ")"
	outputData['boxes'].append(boxText)
	index += 1
denseInput.close()
with open('predicates3.json', 'w') as outfile:
    json.dump(outputData, outfile)

# data = json.load(denseInput)
# caption_nlp = nlp("white clouds in blue sky")
# print("white clouds in blue sky")
# for token in caption_nlp:
# 	if(token.tag_ == 'NN'):
# 		if(object1 == None):
# 			object1 = token.text
# 			for child in token.children:
# 				if(child.tag_ == "JJ"):
# 					attribute1 = child.text
# 			if(token.head.tag_ == 'VBZ'):
# 				relation = token.head.text
# 			else:
# 				for child in token.children:
# 					if(child.tag_ == "VBN" or child.tag_ == "IN"):
# 						relation = child.text
# 						for addition in child.children:
# 							sum = 0
# 							for ends in addition.children:
# 								sum+=1
# 							if(sum > 0):
# 								relation = relation + '_' + addition.text
# 					if(child.tag_ == "VBG"):
# 						relation = child.text
# 		else:
# 	 		object2 = token.text
# 	 		for child in token.children:
# 	 			if(child.tag_ == "JJ"):
# 	 				attribute2 = child.text
# 	print (token.text, token.tag_, token.head.text, token.dep_)
# print(attribute1, object1, relation, attribute2, object2)
# denseInput.close()