import csv
import json
from itertools import zip_longest

with open('./output_data/ros-discourse_data.json') as f:
    rosd_data = json.load(f)

rosd_url = [item.get('url') for item in rosd_data]
rosd_tcontents = [item.get('thread_contents')
                  for item in rosd_data]
rosd_tdetails = [item.get('thread_details') for item in rosd_data]
rosd_title = [item.get('title') for item in rosd_data]
rosd_id = []
rosd_battery = []
rosd_energy = []
rosd_sustain = []
rosd_power = []
rosd_green = []
rosd_tcontents_new = []
rosd_tdetails_new = []

collection_name = []
raw_contents = []

for i in range(len(rosd_url)):
    y = "ROSD" + str(i)
    rosd_id.append(y)

for i in range(len(rosd_url)):
    collection_name.append("ROSDiscourse")

for contents in rosd_tcontents:
    contents = ''.join(contents)
    rosd_tcontents_new.append(contents)

for details in rosd_tdetails:
    try:
        details = ''.join(details)
        rosd_tdetails_new.append(details)
    except TypeError:
        details = ''
        rosd_tdetails_new.append(details)


# print(len(rosd_url))
# print(len(rosd_title))
# print(len(rosd_tcontents_new))
# print(len(rosd_tdetails_new))

for i in range(294):
    rcontents = rosd_tcontents_new[i] + '' + rosd_tdetails_new[i]
    raw_contents.append(rcontents)

# print(len(raw_contents))
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
            
rosd_list = [rosd_id,
             rosd_url,
             collection_name,
             rosd_title,
             raw_contents_final
             ]

for k in keywords:
    print(wfreq.get(k))
    rosd_list.append(wfreq.get(k))

print(len(rosd_id))
print(len(rosd_url))
print(len(collection_name))
print(len(rosd_title))
print(len(raw_contents_final))

export_data = zip_longest(*rosd_list, fillvalue='')

with open('energy-term-datapoints.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(export_data)
myfile.close()
