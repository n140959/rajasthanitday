import stop_words
import textblob
from textblob import TextBlob
ex=stop_words.exclamatory
noun=stop_words.nouns
def resultt(l,nouns,word,string,tag,words):
	s=TextBlob(string)
	textblob_polarity=s.sentiment.polarity
	c=0
	v=['VBN','VBR','VB','VBZ','VBG','VBD','VBP']
	j=['JJ','JJR','JJS','IN','RP','RB']
	polarity=1
	#print tag
	#print words
	sum_polarity=0	
	m=l.count(-1)
	if("other" in word and "not" in word):
		if(len(word)>word.index("not")+1 and [word.index("not")+1]=="other"):
			l[words.index("not")]=1
	if(c!=1):
		i=0
		while(i<len(l)):
			if (i<len(l)-1) and (tag[word.index(words[i])] in v) and (tag[word.index(words[i])+1] in j) and word[word.index(words[i])+1] in words :
				if(tag[word.index(words[i])] == u'VBZ' and word[i]=='is'):
					i=i+1
					continue;
				else:
					if(l[i]!=0) or (len(tag)==1 and l[0]==0):
						if(l[i+1]<0):
							polarity = polarity * l[i+1] *2
						elif(l[i]<0):
							polarity*=l[i]*2
						else:
							polarity*=l[i]
					sum_polarity*=l[i+1]*2
					i=i+2
			elif ((i<len(l)-1) and (tag[word.index(words[i])] in j) and (tag[word.index(words[i])+1] in j))  and word[word.index(words[i])+1] in words :
				if(l[i]!=0) or (len(tag)==1 and l[0]==0):
					if(l[i+1]<0):
						polarity = polarity * l[i+1] *2
					elif(l[i]<0):
						polarity*=l[i]*2
					else:
						polarity*=l[i]
				sum_polarity*=l[i+1]*2
				i=i+2
			else:
				if(l[i]!=0) or (len(tag)==1 and l[0]==0):	
					polarity = polarity * l[i]
				sum_polarity+=l[i]
				i=i+1
		if("but" in word and "not" in word) and word.index("but")<word.index("not"):
			polarity*=-1
			sum_polarity*=-1
		elif("not" in word and "if" in word and "then" in word):
			polarity*=-1
			sum_polarity*=-1
		#print words
		#print polarity,sum_polarity
		#print textblob_polarity,l
		if(l[0]==-2):#there are bottles in the class
			#print "Neutral"
			c=-2
		elif(len(l)==1 and l[0]==0):
			#print "Neutral"
			c=-2
		elif(textblob_polarity>=0.85):#Samsung is very good
			if(polarity<0):
				c=0
			else:
				c=1
		elif(len(l) == m): 
			if("not" in word and polarity>0) and textblob_polarity >=0:
				c=1
			elif(m%2==0):
				if(sum_polarity<=0 and textblob_polarity<0):
					if("not" in word):
						c=1
					else:
						c=0
				else:
					c=1
			else:
				if textblob_polarity<=0 or polarity<0:
					if(m%2==0):
						c=1
					else:
						c=0
				else:
					c=1
		elif(polarity==sum_polarity):
			if(polarity<0 and sum_polarity<0):
				c=0
			elif(textblob_polarity>=0) and "not" not in word:
				c=1
			elif(textblob_polarity>0):
				c=1
			else:
				c=0
		elif(polarity == 2 ):
			if(textblob_polarity>0.05) or (l.count(-1)==0):
				c=1
			elif(sum_polarity>=0) and (textblob_polarity>0.04):
				c=1
			else:
				c=0
		elif(polarity < 0 ) :
			if(sum_polarity >=2) and (textblob_polarity >=0):
				c=1
			elif(textblob_polarity>=0.4) and (sum_polarity>1):
				c=1
			elif(sum_polarity==-2 and textblob_polarity>=0.5):
				c=1
			else:
				c=0

		elif(sum_polarity >= 1 and polarity >=1) or (sum_polarity < 0 and polarity >= 1):
			if("not" not in word):
				m=l.count(-1)
				if(m%2==0 and m>=2 and textblob_polarity < 0.1) :
					c=0
				elif(textblob_polarity<=0 and sum_polarity<0):
					c=0
				else:
					c=1
			else:
				if len(l)==m+1 or textblob_polarity <0:
					c=0
				else:
					c=1
		elif(sum_polarity == 0 and polarity == 1 ):
			if (textblob_polarity >=0):
					c=1
			else:
				if(m==2 and "not" in word):
					c=1
				else:
					c=0
		
		elif(polarity < 0 or polarity == 1) and (textblob_polarity < 0):
			c=0
		elif(sum_polarity<0 and polarity>0):
			if(textblob_polarity>0):
				c=1
			else:
				c=0	
		elif(polarity==0 and sum_polarity!=0):
			if(textblob_polarity>=0):
				c=1
			else:
				c=0
		else:
			#print ('Neutral')
			c=-2
		f=open("result.txt","r").read()
		f=f.split("\n")
		if(c==0):
			f.append(string[:string.find(" ")]+" Negative")
		elif(c==1):
			f.append(string[:string.find(" ")]+" Positive")
		else:
			f.append(string[:string.find(" ")]+" Neutral")
		f1=open("result.txt","w")
		for i in f:
			f1.write(i+"\n")
		f1.close()