import nltk
nltk.download('stopwords')
def pPro(i,o):
	inF = open(i,"r").read()
	outF=open (o,"w+")
	SW = nltk.corpus.stopwords.words("english")
	outData=(' '.join([x for x in inF.split() if x not in SW]))
	print('\nThe standard Stop Words are:\n')
	print(SW)
	print('\nThe dataset after pre-processing\n')
	print(str(outData))
	outF.write(str(outData))
	outF.close()
