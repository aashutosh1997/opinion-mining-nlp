import nltk
nltk.download('wordnet')
nltk.download('sentiwordnet')
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet
def orientation(i): 
    a=wordnet.synsets(i)
    if(len(a) != 0):
        word=a[0].name()
        b=sentiwordnet.senti_synset(word)
        if(b.pos_score()>b.neg_score()):
            return True
        elif(b.pos_score()<b.neg_score()):
            return False
	
