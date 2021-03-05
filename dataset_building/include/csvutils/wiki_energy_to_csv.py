import csv
import json
from itertools import zip_longest

with open('./output_data/wiki_energy_data.json') as f:
    wiki_data = json.load(f)

wiki_url = [item.get('url') for item in wiki_data]
wiki_package = [item.get('package')
                          for item in wiki_data]
wiki_summary = [item.get('package_summary') for item in wiki_data]
wiki_details = [item.get('package_details')
                       for item in wiki_data]
wiki_tt = [item.get('package_tt') for item in wiki_data]
wiki_code = [item.get('package_code') for item in wiki_data]
wiki_id = []
wiki_battery = []
wiki_energy = []
wiki_sustain = []
wiki_power = []
wiki_green = []
wiki_summary_new = []
wiki_details_new = []
wiki_tt_new = []
wiki_code_new = []
collection_name = []
raw_contents = []

for i in range(len(wiki_url)):
    y = "W" + str(i)
    wiki_id.append(y)

for i in range(len(wiki_url)):
    collection_name.append("Wiki")

for summary in wiki_summary:
    summary = ''.join(summary)
    wiki_summary_new.append(summary)

for details in wiki_details:
    try:
        details = ''.join(details)
        wiki_details_new.append(details)
    except TypeError:
        details = ''
        wiki_details_new.append(details)

for tt in wiki_tt:
    try:
        tt = ''.join(tt)
        wiki_tt_new.append(tt)
    except TypeError:
        tt = ''
        wiki_tt_new.append(tt)

for code in wiki_code:
    try:
        code = ''.join(code)
        wiki_code_new.append(code)
    except TypeError:
        code = ''
        wiki_code_new.append(code)

# print(len(wiki_question_new))
# print(len(wiki_answer_new))
# print(len(wiki_question_code_new))
# print(len(wiki_answer_code_new))

for i in range(84):
    rcontents = wiki_summary_new[i] + '' + wiki_details_new[
        i] + '' + wiki_tt_new[i] + '' + wiki_code_new[i]
    raw_contents.append(rcontents)

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
for rc in raw_contents:
    for kword in keywords:
        #print(kword)
        if (kword in rc):
            a, b = rc.split(kword, 1)
            a = a[-45:]
            b = b[0:45]
            power_string = a + kword + b
            raw_contents_final.append(power_string)
            break # Only the first word
        #print(b)
    sum = 0
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
        sum += c
    if sum == 0:
        raw_contents_final.append('no_keyword_in_contents')
        
wiki_list = [wiki_id,
                      wiki_url,
                      collection_name,
                      wiki_package,
                      raw_contents_final
                      ]

print(len(wiki_url))
print(len(collection_name))
print(len(wiki_package))
print(len(raw_contents_final))

for k in keywords:
    print(wfreq.get(k))
    wiki_list.append(wfreq.get(k))

print(len(wfreq.get('battery')))

export_data = zip_longest(*wiki_list, fillvalue='')

with open('energy-term-datapoints.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(export_data)
myfile.close()
