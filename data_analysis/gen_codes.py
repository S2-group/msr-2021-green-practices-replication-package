'''
Created on 4 de dez. de 2020

@author: michel
'''

import csv

with open('phase1/energy-terms-datapoints.csv', newline='') as csvfile:
    with open('../data_analysis/coding/initial-codes',  mode='w') as csvfileout:
        writer = csv.writer(csvfileout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        reader = csv.DictReader(csvfile)
        header = ['Codes']
        writer.writerow(header)
        for row in reader:
            codes = row['Codes - Michel'] # Change to your codes column.
            print(codes)
            code = codes.split('[')
            for c in codes:
                print(c)
            