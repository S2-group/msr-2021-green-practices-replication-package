import csv
import json
from itertools import zip_longest
from collections import defaultdict
import re
from collections import Counter

with open('./output_data/commit_data_new.json') as f:
    commit_data = json.load(f)

commit_url = [item.get('URL') for item in commit_data]
commit_info = [item.get('Commit Info') for item in commit_data]
repo_name = [item.get('Repo Name') for item in commit_data]
commit_id = [item.get('ID') for item in commit_data]
collection_name = []
new_dicts = []
new_commit_url = []
new_commit_url1 = []
new_repo_name = []
new_repo_name1 = []
new_commit_id = []

#for ci in commit_info:
#    for i in ci:
#    for key in ci.keys():
#        ci[key] = ''.join(ci[key])

# power_keyword = 'power'
# battery_keyword = 'batter'
# energy_keyword = 'energy'
# sustain_keyword = 'sustainab'
# green_keyword = 'green'

# for ci in commit_info:
#     for i in ci:
#         for key in i.keys():
#             if(power_keyword in i[key]):
#                 a,b = i[key].split(power_keyword, 1)
#                 a = a[-45:]
#                 b = b[0:45]
#                 power_string = a + power_keyword + b
#                 i[key] = power_string
#             elif(battery_keyword in i[key]):
#                 a,b = i[key].split(battery_keyword, 1)
#                 a = a[-45:]
#                 b = b[0:45]
#                 battery_string = a + battery_keyword + b
#                 i[key] = battery_string
#             elif(energy_keyword in i[key]):
#                 a,b = i[key].split(energy_keyword, 1)
#                 a = a[-45:]
#                 b = b[0:45]
#                 energy_string = a + energy_keyword + b
#                 i[key] = energy_string
#             elif(sustain_keyword in i[key]):
#                 a,b = i[key].split(sustain_keyword, 1)
#                 a = a[-45:]
#                 b = b[0:45]
#                 sustain_string = a + sustain_keyword + b
#                 i[key] = sustain_string
#             elif(green_keyword in i[key]):
#                 a,b = i[key].split(green_keyword, 1)
#                 a = a[-45:]
#                 b = b[0:45]
#                 green_string = a + green_keyword + b
#                 i[key] = green_string
#             else:
#                 other_string = i[key][0:90]
#                 i[key] = other_string



# for ci in commit_info:
#     for i in ci:
#         for k, v in list(i.items()):
#             if (('power' not in v) and ('energy' not in v) and ('batter' not in v) and ('green' not in v)
#                 and ('sustainab' not in v)):
#                 del i[k]


for ci in commit_info:
    sci = ci.split(":")
    new_dicts.append(sci[1])

i = 0
for url in commit_url:
    new_commit_url.append([url] * len(commit_info[i][0]))
    i = i + 1

for url_list in new_commit_url:
    for url in url_list:
        new_commit_url1.append(url)
        
i = 0
for name in repo_name:
    new_repo_name.append([name] * len(commit_info[i][0]))
    i = i + 1

for name_list in new_repo_name:
    for name in name_list:
        new_repo_name1.append(name)

#for i in range(len(new_repo_name1)):
#    y = "C" + str(i)
#    commit_id.append(y)

for i in range(len(commit_id)):
    collection_name.append("Commits")

# print(len(new_dicts))
# print(len(new_commit_url1))
# print(len(new_repo_name1))
# print(len(collection_name))
# print(len(commit_id))

keywords = ['energy',
                 'battery',
                 'power',
                 'consum',
                 'efficien',
                 'drain',
                 'sleep',
                 'charg',
                 'volt',
                 'sustainab',
                 'green',
                 'wak',
                 'watt',
                 'joule',
                 'amper'
                ]
raw_contents_final = []
#raw_frequences = []
wfreq = {}
for rc in commit_info:
    for kword in keywords:
        #print(kword)
        if (kword in rc):
            a, b = rc.split(kword, 1)
            a = a[-45:]
            b = b[0:45]
            power_string = a + kword + b
            raw_contents_final.append(power_string)
            id = '' 
            for item in commit_data:
                if rc in item.get('Commit Info'):
                   id = item.get('ID') 
            new_commit_id.append(id)
            break # Only the first word
        #print(b)
    for kword in keywords:
        c = rc.count(kword)
        if kword not in wfreq.keys():
            #print(kword)
            wfreq[kword] = [ c ]
        else: 
            lst = wfreq.get(kword)
            #print(kword, lst)
            lst.append(c)
            wfreq[kword] = lst

commit_list = [new_commit_id,
               commit_url,
               collection_name,
               repo_name,
               raw_contents_final
              ]

for k in keywords:
    print(wfreq.get(k))
    commit_list.append(wfreq.get(k))

print(len(new_commit_id))
print(len(commit_url))
print(len(collection_name))
print(len(repo_name))
print(len(raw_contents_final))

export_data = zip_longest(*commit_list, fillvalue='')

with open('energy-term-datapoints.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(("ID", "URL", "Repo Name", "Collection", "Commit Info"))
    wr.writerows(export_data)
myfile.close()
