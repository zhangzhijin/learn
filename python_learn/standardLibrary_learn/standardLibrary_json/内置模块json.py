import json,os
data={
  'name':'zzj',
  'id':'01'
}
json_str = json.dumps(data) #bian ma
print ("Python：", repr(data))
print ("JSON对象：", json_str)

json_p=json.loads(json_str)
print(json_p['name'])

# write json file
# f=open("./test.json",'w+')
# json.dump(data,f)

#read json file
# f=open("./内置模块JSON/test.json",'r+')
# data1=json.load(f)
# print(data1['name'])


