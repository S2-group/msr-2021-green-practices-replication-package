import csv
import json
from itertools import zip_longest
from collections import defaultdict
import re
from collections import Counter
def no_blank(fd):
    try:
        while True:
            line = next(fd)
            if len(line.strip()) != 0:
                yield line
    except:
        return

def return_longest_list(list1, list2, list3):
    if len(list1) == 0:
        print("List 1 is empty!")
    elif len(list2) == 0:
        print("List 2 is empty!")
    elif len(list3) == 0:
        print("List 3 is empty")
    if (len(list1) > len(list2) and len(list1) > len(list3)):
        return list1
    elif (len(list2) > len(list1) and len(list2) > len(list3)):
        return list2
    elif (len(list3) > len(list1) and len(list3) > len(list2)):
        return list3
    else:
        if (len(list1) != 0):
            return list1
        elif (len(list2) != 0):
            return list2
        elif (len(list3) != 0):
            return list3

columns = defaultdict(list)
with open('./output_data/Repos_all.csv') as f:
    reader = csv.DictReader(no_blank(f))
    for row in reader:
        for (k,v) in row.items(): 
            columns[k].append(v)

#while '' in columns['URL']:
#    columns['URL'].remove('')
with open('./input_data/git_repos_data.json') as f:
    repo_data = json.load(f)

repo_url = []
repo_name = [item.get('git_repo_name') for item in repo_data]
repo_name_new = []
repo_md_contents = [item.get('md_contents') for item in repo_data]
repo_md_file = [item.get('md_file_names') for item in repo_data]
repo_code_c = [item.get('code_comments_c++') for item in repo_data]
repo_code_p = [item.get('code_comments_python') for item in repo_data]
repo_id = []
collection_name = []
new_dicts_md = []
new_dicts_p = []
new_dicts_c = []
new_repo_url = []
new_repo_url1 = []
new_repo_name = []
new_repo_name1 = []

for name in repo_name:
    for url in columns['URL']:
        if url.endswith(name):
            repo_url.append(url)
            repo_name_new.append(name)
            break
print("repo_url",len(repo_url))
print("repo_name_new",len(repo_name_new))
#print("repo_name",len(repo_name))

#repo_name = repo_name_new
print("repo_name",len(repo_name))
# print(len(set(repo_name)))
d =  Counter(repo_name)
res = [k for k, v in d.items() if v > 1]
#print(res)

for mcontents in repo_md_contents:
    for key in mcontents.keys():
        mcontents[key] = ''.join(mcontents[key])
print("mdcontents",len(repo_md_contents))

for cpp in repo_code_c:
    for key in cpp.keys():
        cpp[key] = ''.join(cpp[key])

for py in repo_code_p:
    for key in py.keys():
        py[key] = ''.join(py[key])

# # consum_keyword = 'consum'
power_keyword = 'power'
battery_keyword = 'battery'
energy_keyword = 'energy'
sustain_keyword = 'sustainab'
green_keyword = 'green'

combo = [repo_md_contents, repo_code_c, repo_code_p]


print("combo",len(combo))
for c in combo:
    for mcontents in c:
        for key in mcontents.keys():
            # if(consum_keyword in mcontents[key]):
            #     print('consum')
            #     a,b = mcontents[key].split(consum_keyword, 1)
            #     a = a[-45:]
            #     b = b[0:45]
            #     consum_string = a + consum_keyword + b
            #     mcontents[key] = consum_string
            if(power_keyword in mcontents[key]):
                a,b = mcontents[key].split(power_keyword, 1)
                a = a[-45:]
                b = b[0:45]
                power_string = a + power_keyword + b
                mcontents[key] = power_string
            elif(battery_keyword in mcontents[key]):
                a,b = mcontents[key].split(battery_keyword, 1)
                a = a[-45:]
                b = b[0:45]
                battery_string = a + battery_keyword + b
                mcontents[key] = battery_string
            elif(energy_keyword in mcontents[key]):
                a,b = mcontents[key].split(energy_keyword, 1)
                a = a[-45:]
                b = b[0:45]
                energy_string = a + energy_keyword + b
                mcontents[key] = energy_string
            elif(sustain_keyword in mcontents[key]):
                a,b = mcontents[key].split(sustain_keyword, 1)
                a = a[-45:]
                b = b[0:45]
                sustain_string = a + sustain_keyword + b
                mcontents[key] = sustain_string
            elif(green_keyword in mcontents[key]):
                a,b = mcontents[key].split(green_keyword, 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + green_keyword + b
                mcontents[key] = green_string
            elif('consum' in mcontents[key]):
                a,b = mcontents[key].split('consum', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'consum' + b
                mcontents[key] = green_string
            elif('efficien' in mcontents[key]):
                a,b = mcontents[key].split('efficien', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'efficien' + b
                mcontents[key] = green_string
            elif('drain' in mcontents[key]):
                a,b = mcontents[key].split('drain', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'drain' + b
                mcontents[key] = green_string
            elif('sleep' in mcontents[key]):
                a,b = mcontents[key].split('sleep', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'sleep' + b
                mcontents[key] = green_string
            elif('charg' in mcontents[key]):
                a,b = mcontents[key].split('charg', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'charg' + b
                mcontents[key] = green_string
            elif('volt' in mcontents[key]):
                a,b = mcontents[key].split('volt', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'volt' + b
                mcontents[key] = green_string
            elif('sustainab' in mcontents[key]):
                a,b = mcontents[key].split('sustainab', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'sustainab' + b
                mcontents[key] = green_string
            elif('wak' in mcontents[key]):
                a,b = mcontents[key].split('wak', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'wak' + b
                mcontents[key] = green_string
            elif('watt' in mcontents[key]):
                a,b = mcontents[key].split('watt', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'watt' + b
                mcontents[key] = green_string
            elif('joule' in mcontents[key]):
                a,b = mcontents[key].split('joule', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'joule' + b
                mcontents[key] = green_string
            elif('amper' in mcontents[key]):
                a,b = mcontents[key].split('amper', 1)
                a = a[-45:]
                b = b[0:45]
                green_string = a + 'amper' + b
                mcontents[key] = green_string
            else:
                other_string = mcontents[key][0:90]
                mcontents[key] = other_string

for cpp in repo_code_c:
    for k, v in list(cpp.items()):
        if (('energy' not in v) and ('battery' not in v) and ('power' not in v) and ('consum' not in v)
            and ('efficien' not in v) and ('drain' not in v) and ('sleep' not in v) and ('charg' not in v)
            and ('volt' not in v) and ('sustainab' not in v) and ('green' not in v) and ('wak' not in v)
            and ('watt' not in v) and ('joule' not in v) and ('amper' not in v)):
            del cpp[k]
for py in repo_code_p:
    for k, v in list(py.items()):
        if (('energy' not in v) and ('battery' not in v) and ('power' not in v) and ('consum' not in v)
            and ('efficien' not in v) and ('drain' not in v) and ('sleep' not in v) and ('charg' not in v)
            and ('volt' not in v) and ('sustainab' not in v) and ('green' not in v) and ('wak' not in v)
            and ('watt' not in v) and ('joule' not in v) and ('amper' not in v)):
            del py[k]

for md in repo_md_contents:
    for k, v in list(md.items()):
        if (('energy' not in v) and ('battery' not in v) and ('power' not in v) and ('consum' not in v)
            and ('efficien' not in v) and ('drain' not in v) and ('sleep' not in v) and ('charg' not in v)
            and ('volt' not in v) and ('sustainab' not in v) and ('green' not in v) and ('wak' not in v)
            and ('watt' not in v) and ('joule' not in v) and ('amper' not in v)):
            del md[k]

for c in repo_code_c:
    if (len(c.keys()) == 0):
        c['message'] = 'no data'
    for k, v in c.items():
        new_code_c = {}
        new_code_c[k] = v
        new_dicts_c.append(new_code_c)

if len(repo_code_c) == 0:
    print("repo_code_c is empty!")
else:
    print("repo_code_c",len(repo_code_c))
#print(new_dicts_c)

for p in repo_code_p:
    if (len(p.keys()) == 0):
        p['message'] = 'no data'
    for k, v in p.items():
        new_code_p = {}
        new_code_p[k] = v
        new_dicts_p.append(new_code_p)
#print(len(new_dicts_p))

if len(repo_code_p) == 0:
    print("repo_code_p is empty!")
else:
    print("repo_code_p",len(repo_code_p))

for m in repo_md_contents:
    if (len(m.keys()) == 0):
        m['message'] = 'no data'
    for k, v in m.items():
        new_md = {}
        new_md[k] = v
        new_dicts_md.append(new_md)
print("new_dicts_md",len(new_dicts_md))

if len(repo_md_contents) == 0:
    print("repo_md_contents is empty!")
else:
    print("repo_md_contents",len(repo_md_contents))

i = 0
print("repo_url",len(repo_url))
for url in repo_url:
    longest_list = return_longest_list(repo_code_p[i], repo_md_contents[i], repo_code_c[i])
    new_repo_url.append([url] * len(repo_code_p[i]))
    i = i + 1
print("longest_list",len(longest_list))
print("new_repo_url",len(new_repo_url))

for url_list in new_repo_url:
    for url in url_list:
        new_repo_url1.append(url)
print("new_repo_url1",len(new_repo_url1))

i = 0
for name in repo_name:
    longest_list = return_longest_list(repo_code_p[i], repo_md_contents[i], repo_code_c[i])
    new_repo_name.append([name] * len(repo_code_p[i]))
    i = i + 1
print("new_repo_name",len(new_repo_name))

for name_list in new_repo_name:
    for name in name_list:
        new_repo_name1.append(name)

print("new_repo_name1",len(new_repo_name1))

for i in range(len(new_repo_name1)):
    y = "REPO_P" + str(i)
    repo_id.append(y)
       
for i in range(len(new_repo_name1)):
    collection_name.append("Repositories")
        
print("repo_id",len(repo_id))
print("new_repo_url1",len(new_repo_url1))
print("new_repo_name1",len(new_repo_name1))
print("collection_name",len(collection_name))
print("new_dicts_md",len(new_dicts_md))
print("new_dicts_p",len(new_dicts_p))
print("new_dicts_c",len(new_dicts_c))

##### Ocurrencies
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

wfreq = {}
for rc in new_dicts_p:
    rc = str(rc)
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


repo_list = [repo_id,
             new_repo_url1,
             collection_name,
             new_repo_name1,
             new_dicts_p
             ]

for k in keywords:
    print(wfreq.get(k))
    repo_list.append(wfreq.get(k))
    
print(len(repo_id))
print(len(new_repo_url1))
print(len(collection_name))
print(len(new_repo_name1))
print(len(new_dicts_p))


export_data = zip_longest(*repo_list, fillvalue='')

with open('energy-term-datapoints.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(("ID", "URL", "Repo Name", "Collection", "Contents"))
    # wr.writerow(("ID", "URL", "Repo Name", "Collection", "MD Contents"))
    wr.writerows(export_data)
myfile.close()
