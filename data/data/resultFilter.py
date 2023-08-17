import json

result_file = "results.json"

# Open and read the JSON file
with open(result_file, 'r') as json_file:
    data_list = json.load(json_file)


unique_list=[]
unique_list_item=[]
for item in data_list:
    #print(len(unique_list))
    if item["actual"] in unique_list:
        #print("continue")
        continue
    else:
        unique_list.append(item["actual"])
        unique_list_item.append(item)

filtered_list=[]

for item in unique_list_item:
    if item["pred"][0]==item["actual"]:
        continue
    else:
        #print(item["pred"])
        filtered_list.append(item)

with open("/home/venkat/workspace/sanskritdiacritics-doctr/data/data/resultsFilteredPassed.json", "w") as myfinalresultfile:
        json.dump(unique_list_item, myfinalresultfile, indent=4, ensure_ascii=False)

with open("/home/venkat/workspace/sanskritdiacritics-doctr/data/data/resultsFilteredFailed.json", "w") as myfinalresultfile:
        json.dump(filtered_list, myfinalresultfile, indent=4, ensure_ascii=False)


