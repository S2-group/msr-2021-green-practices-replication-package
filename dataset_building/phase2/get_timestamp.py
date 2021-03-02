'''
Created on 4 de dez. de 2020

@author: michel
'''

import csv
from datetime import datetime
import get_date

## Getting the Dates
get_date.get_dp_date()

with open('./input_data/included-datapoints-date.csv', newline='') as csvfile:
    with open('./output_data/energy-datapoints.csv',  mode='w') as csvfileout:
        writer = csv.writer(csvfileout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        reader = csv.DictReader(csvfile)
        # Headers
        line = []
        line.append('ID')
        line.append('URL')
        line.append('Collection')
        line.append('Title')
        line.append('Contents')
        line.append('DateTime')
        line.append('Timestamp')
        writer.writerow(line)
        for row in reader:
            line = []
            line.append(row['ID'])
            line.append(row['URL'])
            line.append(row['Collection'])
            line.append(row['Title'])
            line.append(row['Contents'])
            line.append(row['DateTime'])
            date = row['DateTime']
            dtime = '0000-00-00 00:00:00'
            timestamp = '0'
            collection = row['Collection']
            if collection == 'Commits': 
                if date != '0000-00-00 00:00:00' and date != '0000-00-00 00:00':
                    dtime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                    #print('Commits', dtime)
                    timestamp = datetime.timestamp(dtime)
            elif collection in ['GitHubIssues', 'GitHubPRs', 'Repositories']:
                if date != 'NA':                
                    dtime = datetime.strptime(date, '%b %d, %Y')
                    #print(collection, dtime)
                    timestamp = datetime.timestamp(dtime)
            elif collection in ['ROSAnswers','ROSDiscourse','StackOverflow']:
                date_parts = date.split()
                if collection == 'ROSAnswers':
                    date = str(date_parts[0])+' '+str(date_parts[1])
                else:
                    date = str(date_parts[0])+' '+str(date_parts[1])+':00'
                #print(collection,date)
                dtime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                timestamp = datetime.timestamp(dtime)
            line.append(timestamp)
            print(timestamp)
            writer.writerow(line)
                
                
