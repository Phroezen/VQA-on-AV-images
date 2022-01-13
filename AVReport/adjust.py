import sys
import json

denseInput = open('predicates3.json')
data = json.load(denseInput)
outputData = data
index = 0
predFile = open('carPredicates.txt', 'w', encoding="utf-8")
for i in outputData["predicates"]:
	predFile.write(i + ".\n")
for i in outputData["boxes"]:
	predFile.write(i + ".\n")
predFile.close()
denseInput.close()