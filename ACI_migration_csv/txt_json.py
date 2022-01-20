
  
import json 
import csv 
input_file = csv.DictReader(open("data.csv",encoding="utf-8-sig"))
for data in input_file:
    print(json.dumps(data, indent = 4))
 
  
