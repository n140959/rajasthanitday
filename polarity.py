import reviews1
positive=reviews1.positive
negative=reviews1.negative
neutral=reviews1.neutral
import textblob
from textblob import TextBlob
import result
from result import resultt
import ast
def get_polarity(words,noun,string,word,tag):
	f1=open("reviews.py","r").read()
	flag=0
	flag1=0
	f1=f1.split("\n")
	f2=str(f1)
	l=[]
	noun=noun[0]+"="
	if(noun not in f2):
		Dic_name={}
	else:
		index=f2.find(noun)
		index1=f2.find("}",index)
		var=f2[index+len(noun):index1+1]
		Dic_name=ast.literal_eval(var)
		del(f1[f1.index(f2[index:index1+1])])
	for i in words:
		if(i in Dic_name):
			l.append(Dic_name[i])
		else:
			flag=1
			if(i in positive):
				l.append(1)
				Dic_name[i]=1
			elif(i in negative):
				l.append(-1)
				Dic_name[i]=-1
			elif(i in neutral):
				l.append(0)
				Dic_name[i]=0
			else:
				flag=1
				flag1=1
				f=open("swm.txt","r").read()
				f=f.split("\n")
				k="\t"+str(i)+"#"
				Pos_score=-1
				Neg_score=-1
				for m in f:
					if(k in m):
						Pos_score=m[:m.find("\t")]
						Neg_score=m[m.find("\t")+1:m.find("\t",m.find("\t")+1)]
						break
				if(Pos_score==-1):
					ty=type(i)
					if(ty is not int):
						m=TextBlob(i)
						polar=m.polarity
					else:
						polar=0
					if(polar>0):
						polarity=1
						positive.append(i)
					elif(polar<=0):
						polarity=-1
						negative.append(i)
				elif(Pos_score>Neg_score):
					polarity=1
					positive.append(i)
				elif(Pos_score<Neg_score):
					polarity=-1
					negative.append(i)
				else:
					polarity=0
					neutral.append(i)
				Dic_name[i]=polarity
	if(flag==1):
		f1.append(noun+str(Dic_name))
		f=open("reviews.py","w")
		for i in f1:
			f.write(i+"\n")
		f.close()
	if(flag1==1):
		f=open("reviews1.py","w")
		f.write("positive="+str(positive)+"\n")
		f.write("negative="+str(negative)+"\n")
		f.write("neutral="+str(neutral)+"\n")
		f.close()
	if(len(l)==0):
		l.append(-2)
	resultt(l,noun,word,string,tag,words)