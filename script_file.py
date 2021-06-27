########        Dictionayr comprehention        #################



##a=['name','age']
##b=['Rahul',23]
##
##d={a[i]:b[i] for i in range(2)}
##print(d)

##zip,enumerate,map,filter,  * ,  **
##
##a=[3,5,7,2,8,3,9]
##for i in enumerate(a):
##    print(i)
    
##a=['name','age']
##b=[['Rahul','vijay','vishal'],[20,21,22]]
##c={v:b[i] for i,v in enumerate(a)}
##print(c)

with open("data.txt",'r') as f:
    content=f.read()

print("content\n",content)
clist=content.split('\n')
print("clist\n",clist)

heading=clist[0].split(',')
print("heading\n",heading)
rows=[i.split(',') for i in clist[1:]]
print("rows\n",rows)

data=[ [row[i] for row in rows] for i,v in enumerate(heading) ]
print("data\n",data)

print('alldata')

alldata=list(zip(*rows))  #can use zip cause it directly attach each element parally 
print(alldata)

print("data")

data=list(zip(heading,alldata))
print(data)

print('new data')

data=dict(zip(heading,zip(*rows))) #args * used here
print(data)





