import textblob
from textblob import TextBlob
import stop_words
import polarity
from polarity import get_polarity
from graphs import Graph
unuseful=stop_words.unuseful
check=stop_words.check
useful=stop_words.useful
nouns=stop_words.nouns
import reviews1
neutral=reviews1.neutral
p=reviews1.positive
n=reviews1.negative
print ("***///WELCOME TO RATINGSHALA\\\\*******");
print ("process is started");
f=open("../stopwords.txt","r").read()
f=f.split(",")
re=["garden","health","music"]
zz=["HACKATHON_SUMMIT","PRAJA-SEVA","smart cities for happy future"]
j=1
def start(name):
	name="../"+name+"_result.txt"
	f = open(name,"r").read()
	f=f.split("\n")
	for string in f:
		#print string
		m=0
		#string=raw_input("Enter a sentence\n").lower();
		string2=string[string.find(" ")+1:]
		string1=TextBlob(string2)
		word=[]
		tag=[]
		noun=[]
		for i,j in string1.tags:
			m+=1
			if(i=="n't" or i=='no'):
				i="not"
			for  z in i:
				if (ord(z)>=ord("a") and ord(z)<=ord("z")) or (ord(z)>=ord("A") and ord(z)<=ord("Z")):
					continue
				else:
					index=i.find(z)
					n=i[:index]+i[index+1:]
					i=n
			if(i.lower() not in word) and m!=1:
				word.append(i.lower())
				tag.append(j)
			if(j in nouns) and (i not in useful) and (i.capitalize() not in noun) and m!=1 and i not in unuseful and i not in f:
				noun.append(i.capitalize())			
		if(len(noun)==0) and len(word)!=0:
			noun.append(word[0].capitalize())
		if(len(word)!=0):
			search(word,tag,string,noun)
def search(word,tag,string,noun):
	c=0
	words=[]
	for i in range(len(word)):
		if ((word[i] in useful) or (tag[i] in check)) or(word[i] in p) or (word[i] in n):
			if(len(word[i])>1) and (word[i] not in unuseful and word[i] not in neutral and i not in f):
				words.append(word[i])
				c=1
	if c==0:
		words.append(0)
	get_polarity(words,noun,string,word,tag)
	#print " is completed"
if __name__=="__main__":
	for i in re:
		start(i)		
		print "Area",j,"--> "+zz[j-1],"Reviews are catogorised"
		j=j+1
			
	Graph()
