'''
Created on 4 de dez. de 2020

@author: michel
'''

import csv
import sys
sys.path.insert(1, '../include/')
from mongodb import mongo_con
from github import Github

# MONGODB DRIVER
client = mongo_con.con.mongoClient
db = client.data_phase1

with open('./included.csv', newline='') as csvfile:
    with open('./included-date.csv',  mode='w') as csvfileout:
        writer = csv.writer(csvfileout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        reader = csv.DictReader(csvfile)
        #header = ['ID','URL','Collection','Title','Contents','DateTime']
        header = ['DateTime']
        writer.writerow(header)
        for row in reader:
            line = []
            line.append(row['ID'])
            line.append(row['URL'])
            line.append(row['Collection'])
            line.append(row['Title'])
            line.append(row['Contents'])
            #line = [i[1] for i in row]
            #print(line)
            #print(line)
            #print(line)
            col = row['Collection']
    #       prinzt(row['Collection'])
            collection = None
            '''
            if col == 'ROSAnswers':
                #print(url)
                collection = db.ROSAnswers
            
                url = row['URL']
                title = row['Title']
                qresult = collection.find(
                                    { 'url':
                                        { '$eq': url }
                                    })
            
            if col == 'GitHubPRs':
                #print(url)
                collection = db.GitHubOpenPRs
            
                url = row['URL']
                #title = row['Title']
                if collection.count_documents({ 'url':
                                        { '$eq': url }
                                    }) == 0:
                    collection = db.GitHubClosedPRs
                    
                qresult = collection.find(
                                    { 'url':
                                        { '$eq': url }
                                    })
                
            if col == 'GitHubIssues':
                #print(url)
                collection = db.GitHubOpenIssues
            
                url = row['URL']
                #title = row['Title']
                if collection.count_documents({ 'url':
                                        { '$eq': url }
                                    }) == 0:
                    collection = db.GitHubClosedIssues
                    
                qresult = collection.find(
                                    { 'url':
                                        { '$eq': url }
                                    })        
                for doc in qresult:
                    #time = doc['time']
                    time = doc['posted_on']
                    #line = line + ',' + time
                    line.append(time)
                    print(line)
                    #row.append(time)
                    writer.writerow(line)
                    #print(line)
                    break
            '''
            if col == 'Commits':
                # using username and password
                #g = Github("bsd.albonico", "bitobaum*")
                # or using an access token
                g = Github("daeb92ab6884a673fb319ac64e134acde3c7a371")
            
                url= row['URL'].split('/')
                project = url[len(url)-2]+'/'+url[len(url)-1]
                try:
                    repo = g.get_repo(project)
                    
                    content = row['Contents']
                    contents = content.split('\'')
                    c = contents[len(contents)-2]
                    print(c)
                    
                    collection = db.Commits
                    if collection.count_documents(
                                        { 'Commit Info': 
                                         { '$regex': '.*'+c+'.*' 
                                          }}) == 0:
                        date = '0000-00-00 00:00'
                        print(date)
                        writer.writerow([date])
                    else:
                        qresult = collection.find(
                                            { 'Commit Info': { '$regex': '.*'+c+'.*' }})
                        for doc in qresult:
                            #print(doc)
                            info = doc['Commit Info']
                            commit_info = info.split(':')
                            com = commit_info[0].split('\'')
                            hash = com[1]
                            date = ''
                            try:
                                commit = repo.get_commit(sha=hash)
                                date = str(commit.commit.author.date) 
                            except:
                                date = '0000-00-00 00:00'
                            #print(date)
                            #line.append(date)
                            print(date)
                            writer.writerow([date])
                            break
                except:
                    date = '0000-00-00 00:00'
                    print(date)
                    writer.writerow([date])
                    
                    