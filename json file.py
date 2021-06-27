# json file is a file like a dictinory file using ##import json
import json
with open("data.txt",'r') as f:
    data=f.read()
with open('mydata.json','w')as file:
    json.dump(data,file)
    print('json file created')
