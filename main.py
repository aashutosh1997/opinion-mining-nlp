import prepro
import tokenize
import classifier
import aspects
import opinions

import subprocess
tmp = subprocess.call('clear',shell=True)

while True:
	example=int(input("Choose Example (1/2): "))
	if example== 1 or example== 2:
		break
	else:
		continue
_Addr='Data/Example'+str(example)+'/'
_Dataset=_Addr+'a.Dataset.txt'
_PreProcess=_Addr+'b.PreProcess.txt'
_Tokenize=_Addr+'c.Tokenize.txt'
_Pos=_Addr+'d.Pos.txt'
_Aspects=_Addr+'e.Aspects.txt'
_Opinions=_Addr+'f.Opinions.txt'
 
print("\t\tASPECT EXTRACTION SYSTEM")
n=0
while n!=6:
	n=int(input('\nList of functions:\n\t1. Preprocess Data\n\t2. Tokenize data\n\t3. Tag Parts of speech\n\t4. List Aspects\n\t5. List Opinion Words\n\t6. Exit\n\tChoice: '))
	if n==1:
		prepro.pPro(_Dataset,_PreProcess)
	elif n==2:
		tokenize.tokens(_Dataset,_Tokenize)
	elif n==3:
		classifier.classify(_Tokenize,_Pos)
	elif n==4:
		aspects.extractAsp(_Pos,_Aspects)
	elif n==5:
		opinions.opWords(_Pos,_Aspects,_Opinions)
	elif n==6:
		continue
	else:
		print('Invalid option!! Try Again.')
