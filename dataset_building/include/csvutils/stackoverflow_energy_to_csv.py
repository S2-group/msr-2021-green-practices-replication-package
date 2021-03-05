import csv
import json
import numpy as np

from itertools import zip_longest
with open('./output_data/new_stackoverflow_data.json') as f:
    stackoverflow_data = json.load(f)

stackoverflow_url = [item.get('url') for item in stackoverflow_data]
stackoverflow_question = [item.get('post_content')
                          for item in stackoverflow_data]
stackoverflow_answer = [item.get('answer') for item in stackoverflow_data]
stackoverflow_qcode = [item.get('question_code')
                       for item in stackoverflow_data]
stackoverflow_acode = [item.get('answer_code') for item in stackoverflow_data]
stackoverflow_title = [item.get('title') for item in stackoverflow_data]
stackoverflow_id = []
stackoverflow_battery = []
stackoverflow_energy = []
stackoverflow_sustain = []
stackoverflow_power = []
stackoverflow_green = []
stackoverflow_question_new = []
stackoverflow_answer_new = []
stackoverflow_question_code_new = []
stackoverflow_answer_code_new = []
collection_name = []
raw_contents = []

for i in range(len(stackoverflow_url)):
    y = "SO" + str(i)
    stackoverflow_id.append(y)

for i in range(len(stackoverflow_url)):
    collection_name.append("StackOverflow")

for questions in stackoverflow_question:
    questions = ''.join(questions)
    stackoverflow_question_new.append(questions)

for answers in stackoverflow_answer:
    answers = ''.join(answers)
    stackoverflow_answer_new.append(answers)

for qcode in stackoverflow_qcode:
    try:
        qcode = ''.join(qcode)
        stackoverflow_question_code_new.append(qcode)
    except TypeError:
        qcode = ''
        stackoverflow_question_code_new.append(qcode)

for acode in stackoverflow_acode:
    try:
        acode = ''.join(acode)
        stackoverflow_answer_code_new.append(acode)
    except TypeError:
        acode = ''
        stackoverflow_answer_code_new.append(acode)

for i in range(60):
    rcontents = stackoverflow_question_new[i] + '' + stackoverflow_question_code_new[
        i] + '' + stackoverflow_answer_new[i] + '' + stackoverflow_answer_code_new[i]
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
        
      
stackoverflow_list = [stackoverflow_id,
                      stackoverflow_url,
                      stackoverflow_title,
                      raw_contents_final
                      ]
for k in keywords:
    print(wfreq.get(k))
    stackoverflow_list.append(wfreq.get(k))

print(len(stackoverflow_id))
print(len(stackoverflow_url))
print(len(stackoverflow_title))
print(len(raw_contents_final))

#print(stackoverflow_id)
#for kw in keywords:
#    print(wfreq[kw])

export_data = zip_longest(*stackoverflow_list, fillvalue='')

with open('energy-term-datapoints.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(export_data)
myfile.close()
