import ori
import ast
import re
import nltk
from nltk import word_tokenize
def opWords(iR, iA, o):
	outData={}
	knownOri={}
	nWords = {"aren't", "ain't","can't", "couldn't","didn't","doesn't","don't","hadn't", "hasn't", "isn't", "never", "nothing", "nowhere", "noone", "none", "not", "shouldn't", "won't", "wouldn't" }       
	inRev = open(iR,"r").read()
	inAsp = open(iA,"r").read()
	outAsp=open (o,"w")
	posList=ast.literal_eval(inRev)
	aspList=ast.literal_eval(inAsp)
	print("Aspect\t\t\t\tPositive\tNegative")
	for x,y in aspList:
		aTokens= word_tokenize(x)
		count=0
		for m,n in posList.items():
			flag=True
			nS=False
			for t in aTokens:
				if(t in str(n).upper()):
					flag = flag and True
				else:
					flag = False
					break
			if(flag):
				for u in nWords:
					if(not nS):
						if u.upper() in str(n).upper():
							nS=nS or True
				outData.setdefault(x,[0,0,0])
				for word,tag in n:
					if(tag=='JJ' or tag=='JJR' or tag=='JJS'or tag== 'RB' or tag== 'RBR'or tag== 'RBS'):
						count+=1
						if(word not in knownOri):
							orien=ori.orientation(word)
							knownOri[word]=orien
						else:
							orien=knownOri[word]
						if(nS and orien is not None):
							orien= not orien
						if(orien==True):
							outData[x][0]+=1
						elif(orien==False):
							outData[x][1]+=1
						elif(orien is None):
							outData[x][2]+=1
		if(count>0):
			outData[x][0]=round((float(outData[x][0])/float(count))*100,2)
			outData[x][1]=round((float(outData[x][1])/float(count))*100,2)
			outData[x][2]=round((float(outData[x][2])/float(count))*100,2)
			T="\t\t\t\t"
			if len(str(x))>7 and len(str(x))<=15:
				T="\t\t\t"
			elif len(str(x))>15:
				T="\t\t"
			print(str(x)+T+str(outData[x][0])+"\t\t"+str(outData[x][1]))
	outAsp.write(str(outData))
	outAsp.close();
