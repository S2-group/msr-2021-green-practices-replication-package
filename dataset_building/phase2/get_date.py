'''
Created on 4 de dez. de 2020

@author: michel
'''

import csv
from github import Github
import sys
import os.path

sys.path.insert(1, '../include/')

from mongodb import mongo_con
from helpers import ConfReader

def get_dp_date():
    
    if os.path.isfile('./input_data/included-datapoints-date.csv'):
        print("\033[1;30;46m File ./input_data/included-datapoints-date.csv already exist! Skipping get_date...\n")
        print("\033[0;30;47m ")
    else:
        ### Set your GitHub token
        cReader = ConfReader.ConfReader('../parameters.cfg')
        git_token = cReader.getConf('github', 'token')
        
        # MONGODB DRIVER
        client = mongo_con.con.mongoClient
        db = client.data_phase1
        
        with open('./input_data/included-datapoints.csv', newline='') as csvfile:
            with open('./input_data/included-datapoints-date.csv',  mode='w') as csvfileout:
                writer = csv.writer(csvfileout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                reader = csv.DictReader(csvfile)
                #header = ['DateTime']
                #writer.writerow(header)
                # Headers
                line = []
                line.append('ID')
                line.append('URL')
                line.append('Collection')
                line.append('Title')
                line.append('Contents')
                line.append('DateTime')
                writer.writerow(line)
                print("Getting the dates...")
                for row in reader:
                    line = []
                    line.append(row['ID'])
                    line.append(row['URL'])
                    line.append(row['Collection'])
                    line.append(row['Title'])
                    line.append(row['Contents'])
                    
                    col = row['Collection']
                    #print(row['Collection'])
                    collection = None
                
                    if col == 'ROSAnswers':
                        #print(url)
                        collection = db.ROSAnswers
                        url = row['URL']
                        title = row['Title']
                        qresult = collection.find(
                                    { 'url':
                                         { '$eq': url }
                                     })
                        for doc in qresult:
                            time = doc['time']
                            print('ROSAnswers',time)
                            line.append(time)
                            break
                    elif col == 'GitHubPRs':
                        collection = db.GitHubOpenPRs
                        url = row['URL']
                        if collection.count_documents({ 'url':
                                                        { '$eq': url }
                                                    }) == 0:
                            collection = db.GitHubClosedPRs
                            qresult = collection.find(
                                                    { 'url':
                                                        { '$eq': url }
                                                   })
                            for doc in qresult:
                                time = doc['posted_on']
                                print('GitHubPRs',time)
                                line.append(time)
                                break
                    elif col == 'GitHubIssues':
                        collection = db.GitHubOpenIssues
                        url = row['URL']
                        if collection.count_documents({ 'url':
                                                        { '$eq': url }
                                                    }) == 0:
                            collection = db.GitHubClosedIssues
                            qresult = collection.find(
                                                    { 'url':
                                                        { '$eq': url }
                                                    })
                            for doc in qresult:
                                time = doc['posted_on']
                                print('GitHubIssues',time)
                                line.append(time)
                                #print(time)     
                                break
                    elif col == 'Commits':
                        g = Github(git_token)
                        url= row['URL'].split('/')
                        project = url[len(url)-2]+'/'+url[len(url)-1]
                        try:
                            content = row['Contents']
                            contents = content.split('\'')
                            c = contents[len(contents)-2]
                            collection = db.Commits
                            if collection.count_documents(
                                                        { 'Commit Info': 
                                                         { '$regex': '.*'+c+'.*' 
                                                          }}) == 0:
                                date = '0000-00-00 00:00:00'
                            else:
                                qresult = collection.find(
                                                            { 'Commit Info': { '$regex': '.*'+c+'.*' }})
                                for doc in qresult:
                                    info = doc['Commit Info']
                                    commit_info = info.split(':')
                                    com = commit_info[0].split('\'')
                                    hash = com[1]
                                    date = ''
                                    try:
                                        repo = g.get_repo(project)
                                        commit = repo.get_commit(sha=hash)
                                        date = str(commit.commit.author.date)
                                    except:
                                        date = '0000-00-00 00:00:00'
                                    break
                        except:
                            date = '0000-00-00 00:00:00'
                        #print(date)
                        line.append(date)
                        print('Commits',date)
                    else:
                        time = '0000-00-00 00:00:00'
                        print('Other',time)
                        line.append(time)
                    writer.writerow(line)
get_dp_date()