import csv
import json
from itertools import zip_longest

with open('./output_data/ros-answers_data.json') as f:
    rosa_data = json.load(f)

rosa_url = [item.get('url') for item in rosa_data]
rosa_contents = [item.get('post_content')
                 for item in rosa_data]
rosa_answer = [item.get('answer') for item in rosa_data]
rosa_qdetails = [item.get('question_details') for item in rosa_data]
rosa_adetails = [item.get('answer_details') for item in rosa_data]
rosa_qcode = [item.get('question_code') for item in rosa_data]
rosa_acode = [item.get('answer_code') for item in rosa_data]
rosa_title = [item.get('title') for item in rosa_data]
rosa_id = []
rosa_battery = []
rosa_energy = []
rosa_sustain = []
rosa_power = []
rosa_green = []
rosa_contents_new = []
rosa_answer_new = []
rosa_qdetails_new = []
rosa_adetails_new = []
rosa_qcode_new = []
rosa_acode_new = []

collection_name = []
raw_contents = []

for i in range(len(rosa_url)):
    y = "ROSA" + str(i)
    rosa_id.append(y)

for i in range(len(rosa_url)):
    collection_name.append("ROSAnswers")

for contents in rosa_contents:
    try:
        contents = ''.join(contents)
        rosa_contents_new.append(contents)
    except TypeError:
        contents = ''
        rosa_contents_new.append(contents)

for answer in rosa_answer:
    try:
        answer = ''.join(answer)
        rosa_answer_new.append(answer)
    except TypeError:
        answer = ''
        rosa_answer_new.append(answer)

for qdetails in rosa_qdetails:
    try:
        qdetails = ''.join(qdetails)
        rosa_qdetails_new.append(qetails)
    except TypeError:
        qetails = ''
        rosa_qdetails_new.append(qetails)

for adetails in rosa_adetails:
    try:
        adetails = ''.join(adetails)
        rosa_adetails_new.append(aetails)
    except TypeError:
        aetails = ''
        rosa_adetails_new.append(aetails)

for acode in rosa_acode:
    try:
        acode = ''.join(acode)
        rosa_acode_new.append(acode)
    except TypeError:
        acode = ''
        rosa_acode_new.append(acode)

for qcode in rosa_qcode:
    try:
        qcode = ''.join(qcode)
        rosa_qcode_new.append(qcode)
    except TypeError:
        qcode = ''
        rosa_qcode_new.append(qcode)

for i in range(len(rosa_contents_new)):
    rcontents = rosa_contents_new[
        i] + '' + rosa_qdetails_new[i] + '' + rosa_qcode_new[i] + '' + rosa_answer_new[i] + '' + rosa_adetails_new[i] + '' + rosa_acode_new[i]
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
    sum=0
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
        sum+=c
    if sum == 0:
        raw_contents_final.append('no_keyword_in_contents')

rosa_list = [rosa_id,
             rosa_url,
             collection_name,
             rosa_title,
             raw_contents_final]

for k in keywords:
    print(wfreq.get(k))
    rosa_list.append(wfreq.get(k))

print(len(rosa_id))
print(len(rosa_url))
print(len(collection_name))
print(len(rosa_title))
print(len(raw_contents_final))

export_data = zip_longest(*rosa_list, fillvalue='')

with open('energy-term-datapoints.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(export_data)
myfile.close()
