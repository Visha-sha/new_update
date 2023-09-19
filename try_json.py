import json

json_file="json_try.json"

json_new=json.load(open(json_file))
#print(json_new["NAME"])

json_str=json.dumps(json_new)
#print(json_str)

json_new=json.loads(json_str)
print(json_new["STATUS"])





