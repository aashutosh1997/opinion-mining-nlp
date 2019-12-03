import nltk
import ast
from nltk.tokenize import word_tokenize
def classify(i,o):
	inF = open(i,"r").read()
	outF=open (o,"w")
	words=ast.literal_eval(inF)
	outData={}
	for key,value in words.items():
		outData[key]=nltk.pos_tag(nltk.word_tokenize(value))
	for x,y in outData.items():
		print(x,' ',y)
	outF.write(str(outData))
	outF.close()

