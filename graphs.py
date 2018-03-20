import matplotlib.pyplot as plt
def Graph():
	lables='positive','Negative','Neutral'
	f=open("result.txt","r").read()
	f=f.split("\n")
	count={}
	# TOTAL POLARITY GRAPH
	count.setdefault('Negative',0)
	count.setdefault('Positive',0)
	count.setdefault('Neutral',0)
	for i in f:
		if(i==''):
			continue
		index=str(i).find(" ")
		if(i[index+1:]=='Positive'):
			count['Positive']+=1
		elif(i[index+1:]=="Neutral"):
			count['Neutral']+=1
		else:
			count['Negative']+=1
	plt.title("Reviews Feed-Back Result")
	sizes=[count['Positive'],count['Negative'],count['Neutral']]
	colors=['green','Red','orange']
	explode=(0.1,0,0)
	plt.pie(sizes,labels=lables,colors=colors,autopct='%1.1d%%',shadow=True,startangle=160)
	plt.show()
