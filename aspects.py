import ast
def extractAsp(i,o):
	inF = open(i,"r").read()
	outF=open (o,"w")
	words=ast.literal_eval(inF)
	prevWord=''
	prevPos=''
	currWord=''
	aspects=[]
	Dict={}
	#Extracting Aspects
	for x,y in words.items():
		for word,pos in y:
			if(pos=='NN' or pos=='NNP'):
				if(prevPos=='NN' or prevPos=='NNP'):
					currWord= prevWord + ' ' + word
				else:
					aspects.append(prevWord.upper())
					currWord= word
			prevWord=currWord
			prevPos=pos
    #Eliminating aspect which has 1 or less count
	for z in aspects:
		if(aspects.count(z)>1):
			if(Dict.keys()!=z):
				Dict[z]=aspects.count(z)
	outputData=sorted(Dict.items(), key=lambda n: n[1],reverse = True)
	print(outputData)
	outF.write(str(outputData))
	outF.close()
