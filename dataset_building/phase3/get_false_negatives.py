import ssl
import json
import sys

sys.path.insert(1, '../include/')
from mongodb import mongo_con

ssl._create_default_https_context = ssl._create_unverified_context

def get_energy_pr(collection, k):
    original_energy_list = []
    counter_list = []
    counter = 0
    
    energy_query = {}
    
    #### File Names
    '''
    if 'repo' == k:
        with open('../../phase1_data_collection/git_scraper/data/git_repos_data.json') as f:
            d = json.load(f)
            md_file_names = []
            code_comments_md = [item.get(ck) for item in d]
            for dictionary in code_comments_md:
                for file_name in dictionary:
                    md_file_names.append(file_name)
                    
            for name in md_file_names:
                energy_query = collection.find(
                    { '$nor': [ { ck+"."+name: {'$regex': '.*energy.*'}},
                                { ck+"."+name: {'$regex': '.*battery.*'}},
                                { ck+"."+name: {'$regex': '.*power.*'}},
                                { ck+"."+name: {'$regex': '.*consum.*'}},
                                { ck+"."+name: {'$regex': '.*efficien.*'}},
                                { ck+"."+name: {'$regex': '.*drain.*'}},
                                { ck+"."+name: {'$regex': '.*sleep.*'}},
                                { ck+"."+name: {'$regex': '.*charg.*'}},
                                { ck+"."+name: {'$regex': '.*volt.*'}},
                                { ck+"."+name: {'$regex': '.*sustainab.*'}},
                                { ck+"."+name: {'$regex': '.*green.*'}},
                                { ck+"."+name: {'$regex': '.*wak.*'}},
                                { ck+"."+name: {'$regex': '.*joule.*'}},
                                { ck+"."+name: {'$regex': '.*amper.*'}}
                                 ] }
                )
                for document in energy_query:
                    original_energy_list.append(document)
                    counter = counter + 1
                counter_list.append(counter)                   
    else:
        '''
    if 'wiki' == k:
            energy_query = collection.find(
                    { '$and': [ { '$nor': [ { 'package_details': {'$regex': '.*energy.*'}},
                                { 'package_details': {'$regex': '.*battery.*'}},
                                { 'package_details': {'$regex': '.*power.*'}},
                                { 'package_details': {'$regex': '.*consum.*'}},
                                { 'package_details': {'$regex': '.*efficien.*'}},
                                { 'package_details': {'$regex': '.*drain.*'}},
                                { 'package_details': {'$regex': '.*sleep.*'}},
                                { 'package_details': {'$regex': '.*charg.*'}},
                                { 'package_details': {'$regex': '.*volt.*'}},
                                { 'package_details': {'$regex': '.*sustainab.*'}},
                                { 'package_details': {'$regex': '.*green.*'}},
                                { 'package_details': {'$regex': '.*wak.*'}},
                                { 'package_details': {'$regex': '.*joule.*'}},
                                { 'package_details': {'$regex': '.*amper.*'}}
                            ] },
                                { '$nor': [ { 'pakcage_summary': {'$regex': '.*energy.*'}},
                                { 'pakcage_summary': {'$regex': '.*battery.*'}},
                                { 'pakcage_summary': {'$regex': '.*power.*'}},
                                { 'pakcage_summary': {'$regex': '.*consum.*'}},
                                { 'pakcage_summary': {'$regex': '.*efficien.*'}},
                                { 'pakcage_summary': {'$regex': '.*drain.*'}},
                                { 'pakcage_summary': {'$regex': '.*sleep.*'}},
                                { 'pakcage_summary': {'$regex': '.*charg.*'}},
                                { 'pakcage_summary': {'$regex': '.*volt.*'}},
                                { 'pakcage_summary': {'$regex': '.*sustainab.*'}},
                                { 'pakcage_summary': {'$regex': '.*green.*'}},
                                { 'pakcage_summary': {'$regex': '.*wak.*'}},
                                { 'pakcage_summary': {'$regex': '.*joule.*'}},
                                { 'pakcage_summary': {'$regex': '.*amper.*'}}
                            ] }
                                   
                        ]}           
                    )
                        
    elif 'rosanswers' == k:
            energy_query = collection.find(
                    { '$and': [ { '$nor': [ { 'title': {'$regex': '.*energy.*'}},
                                { 'title': {'$regex': '.*battery.*'}},
                                { 'title': {'$regex': '.*power.*'}},
                                { 'title': {'$regex': '.*consum.*'}},
                                { 'title': {'$regex': '.*efficien.*'}},
                                { 'title': {'$regex': '.*drain.*'}},
                                { 'title': {'$regex': '.*sleep.*'}},
                                { 'title': {'$regex': '.*charg.*'}},
                                { 'title': {'$regex': '.*volt.*'}},
                                { 'title': {'$regex': '.*sustainab.*'}},
                                { 'title': {'$regex': '.*green.*'}},
                                { 'title': {'$regex': '.*wak.*'}},
                                { 'title': {'$regex': '.*joule.*'}},
                                { 'title': {'$regex': '.*amper.*'}}
                            ] },
                                { '$nor': [ { 'post_content': {'$regex': '.*energy.*'}},
                                { 'post_content': {'$regex': '.*battery.*'}},
                                { 'post_content': {'$regex': '.*power.*'}},
                                { 'post_content': {'$regex': '.*consum.*'}},
                                { 'post_content': {'$regex': '.*efficien.*'}},
                                { 'post_content': {'$regex': '.*drain.*'}},
                                { 'post_content': {'$regex': '.*sleep.*'}},
                                { 'post_content': {'$regex': '.*charg.*'}},
                                { 'post_content': {'$regex': '.*volt.*'}},
                                { 'post_content': {'$regex': '.*sustainab.*'}},
                                { 'post_content': {'$regex': '.*green.*'}},
                                { 'post_content': {'$regex': '.*wak.*'}},
                                { 'post_content': {'$regex': '.*joule.*'}},
                                { 'post_content': {'$regex': '.*amper.*'}}
                            ] }
                                   
                        ]}           
                    )
            
    elif 'stackoverflow' == k:
            print("Hey there!")
            energy_query = collection.find(
                    { '$and': [ { '$nor': [ { 'title': {'$regex': '.*energy.*'}},
                                { 'title': {'$regex': '.*battery.*'}},
                                { 'title': {'$regex': '.*power.*'}},
                                { 'title': {'$regex': '.*consum.*'}},
                                { 'title': {'$regex': '.*efficien.*'}},
                                { 'title': {'$regex': '.*drain.*'}},
                                { 'title': {'$regex': '.*sleep.*'}},
                                { 'title': {'$regex': '.*charg.*'}},
                                { 'title': {'$regex': '.*volt.*'}},
                                { 'title': {'$regex': '.*sustainab.*'}},
                                { 'title': {'$regex': '.*green.*'}},
                                { 'title': {'$regex': '.*wak.*'}},
                                { 'title': {'$regex': '.*joule.*'}},
                                { 'title': {'$regex': '.*amper.*'}}
                            ] },
                                { '$nor': [ { 'post_content': {'$regex': '.*energy.*'}},
                                { 'post_content': {'$regex': '.*battery.*'}},
                                { 'post_content': {'$regex': '.*power.*'}},
                                { 'post_content': {'$regex': '.*consum.*'}},
                                { 'post_content': {'$regex': '.*efficien.*'}},
                                { 'post_content': {'$regex': '.*drain.*'}},
                                { 'post_content': {'$regex': '.*sleep.*'}},
                                { 'post_content': {'$regex': '.*charg.*'}},
                                { 'post_content': {'$regex': '.*volt.*'}},
                                { 'post_content': {'$regex': '.*sustainab.*'}},
                                { 'post_content': {'$regex': '.*green.*'}},
                                { 'post_content': {'$regex': '.*wak.*'}},
                                { 'post_content': {'$regex': '.*joule.*'}},
                                { 'post_content': {'$regex': '.*amper.*'}}
                            ] }
                                   
                        ]}           
                    )
            
    elif 'bitbucket' == k:
            energy_query = collection.find(
                    { '$and': [ { '$nor': [ { 'pr_title': {'$regex': '.*energy.*'}},
                                { 'pr_title': {'$regex': '.*battery.*'}},
                                { 'pr_title': {'$regex': '.*power.*'}},
                                { 'pr_title': {'$regex': '.*consum.*'}},
                                { 'pr_title': {'$regex': '.*efficien.*'}},
                                { 'pr_title': {'$regex': '.*drain.*'}},
                                { 'pr_title': {'$regex': '.*sleep.*'}},
                                { 'pr_title': {'$regex': '.*charg.*'}},
                                { 'pr_title': {'$regex': '.*volt.*'}},
                                { 'pr_title': {'$regex': '.*sustainab.*'}},
                                { 'pr_title': {'$regex': '.*green.*'}},
                                { 'pr_title': {'$regex': '.*wak.*'}},
                                { 'pr_title': {'$regex': '.*joule.*'}},
                                { 'pr_title': {'$regex': '.*amper.*'}}
                            ] },
                                { '$nor': [ { 'pr_contents': {'$regex': '.*energy.*'}},
                                { 'pr_contents': {'$regex': '.*battery.*'}},
                                { 'pr_contents': {'$regex': '.*power.*'}},
                                { 'pr_contents': {'$regex': '.*consum.*'}},
                                { 'pr_contents': {'$regex': '.*efficien.*'}},
                                { 'pr_contents': {'$regex': '.*drain.*'}},
                                { 'pr_contents': {'$regex': '.*sleep.*'}},
                                { 'pr_contents': {'$regex': '.*charg.*'}},
                                { 'pr_contents': {'$regex': '.*volt.*'}},
                                { 'pr_contents': {'$regex': '.*sustainab.*'}},
                                { 'pr_contents': {'$regex': '.*green.*'}},
                                { 'pr_contents': {'$regex': '.*wak.*'}},
                                { 'pr_contents': {'$regex': '.*joule.*'}},
                                { 'pr_contents': {'$regex': '.*amper.*'}}
                            ] }
                                   
                        ]})    
                      
    elif 'rosdiscurse' == k:
            energy_query = collection.find(
                    { '$and': [ { '$nor': [ { 'title': {'$regex': '.*energy.*'}},
                                { 'title': {'$regex': '.*battery.*'}},
                                { 'title': {'$regex': '.*power.*'}},
                                { 'title': {'$regex': '.*consum.*'}},
                                { 'title': {'$regex': '.*efficien.*'}},
                                { 'title': {'$regex': '.*drain.*'}},
                                { 'title': {'$regex': '.*sleep.*'}},
                                { 'title': {'$regex': '.*charg.*'}},
                                { 'title': {'$regex': '.*volt.*'}},
                                { 'title': {'$regex': '.*sustainab.*'}},
                                { 'title': {'$regex': '.*green.*'}},
                                { 'title': {'$regex': '.*wak.*'}},
                                { 'title': {'$regex': '.*joule.*'}},
                                { 'title': {'$regex': '.*amper.*'}}
                            ] },
                                { '$nor': [ { 'thread_contents': {'$regex': '.*energy.*'}},
                                { 'thread_contents': {'$regex': '.*battery.*'}},
                                { 'thread_contents': {'$regex': '.*power.*'}},
                                { 'thread_contents': {'$regex': '.*consum.*'}},
                                { 'thread_contents': {'$regex': '.*efficien.*'}},
                                { 'thread_contents': {'$regex': '.*drain.*'}},
                                { 'thread_contents': {'$regex': '.*sleep.*'}},
                                { 'thread_contents': {'$regex': '.*charg.*'}},
                                { 'thread_contents': {'$regex': '.*volt.*'}},
                                { 'thread_contents': {'$regex': '.*sustainab.*'}},
                                { 'thread_contents': {'$regex': '.*green.*'}},
                                { 'thread_contents': {'$regex': '.*wak.*'}},
                                { 'thread_contents': {'$regex': '.*joule.*'}},
                                { 'thread_contents': {'$regex': '.*amper.*'}}
                            ] }
                                   
                        ]}           
                    )
        
    elif 'prsgit' == k:
            energy_query = collection.find(
                    { '$and': [ { '$nor': [ { 'pr_title': {'$regex': '.*energy.*'}},
                                { 'pr_title': {'$regex': '.*battery.*'}},
                                { 'pr_title': {'$regex': '.*power.*'}},
                                { 'pr_title': {'$regex': '.*consum.*'}},
                                { 'pr_title': {'$regex': '.*efficien.*'}},
                                { 'pr_title': {'$regex': '.*drain.*'}},
                                { 'pr_title': {'$regex': '.*sleep.*'}},
                                { 'pr_title': {'$regex': '.*charg.*'}},
                                { 'pr_title': {'$regex': '.*volt.*'}},
                                { 'pr_title': {'$regex': '.*sustainab.*'}},
                                { 'pr_title': {'$regex': '.*green.*'}},
                                { 'pr_title': {'$regex': '.*wak.*'}},
                                { 'pr_title': {'$regex': '.*joule.*'}},
                                { 'pr_title': {'$regex': '.*amper.*'}}
                            ] },
                                { '$nor': [ { 'pr_contents': {'$regex': '.*energy.*'}},
                                { 'pr_contents': {'$regex': '.*battery.*'}},
                                { 'pr_contents': {'$regex': '.*power.*'}},
                                { 'pr_contents': {'$regex': '.*consum.*'}},
                                { 'pr_contents': {'$regex': '.*efficien.*'}},
                                { 'pr_contents': {'$regex': '.*drain.*'}},
                                { 'pr_contents': {'$regex': '.*sleep.*'}},
                                { 'pr_contents': {'$regex': '.*charg.*'}},
                                { 'pr_contents': {'$regex': '.*volt.*'}},
                                { 'pr_contents': {'$regex': '.*sustainab.*'}},
                                { 'pr_contents': {'$regex': '.*green.*'}},
                                { 'pr_contents': {'$regex': '.*wak.*'}},
                                { 'pr_contents': {'$regex': '.*joule.*'}},
                                { 'pr_contents': {'$regex': '.*amper.*'}}
                            ] }
                                   
                        ]})
            
    elif 'issues' == k:
            energy_query = collection.find(
                    { '$and': [ { '$nor': [ { 'issue_title': {'$regex': '.*energy.*'}},
                                { 'issue_title': {'$regex': '.*battery.*'}},
                                { 'issue_title': {'$regex': '.*power.*'}},
                                { 'issue_title': {'$regex': '.*consum.*'}},
                                { 'issue_title': {'$regex': '.*efficien.*'}},
                                { 'issue_title': {'$regex': '.*drain.*'}},
                                { 'issue_title': {'$regex': '.*sleep.*'}},
                                { 'issue_title': {'$regex': '.*charg.*'}},
                                { 'issue_title': {'$regex': '.*volt.*'}},
                                { 'issue_title': {'$regex': '.*sustainab.*'}},
                                { 'issue_title': {'$regex': '.*green.*'}},
                                { 'issue_title': {'$regex': '.*wak.*'}},
                                { 'issue_title': {'$regex': '.*joule.*'}},
                                { 'issue_title': {'$regex': '.*amper.*'}}
                            ] },
                                { '$nor': [ { 'issue_contents': {'$regex': '.*energy.*'}},
                                { 'issue_contents': {'$regex': '.*battery.*'}},
                                { 'issue_contents': {'$regex': '.*power.*'}},
                                { 'issue_contents': {'$regex': '.*consum.*'}},
                                { 'issue_contents': {'$regex': '.*efficien.*'}},
                                { 'issue_contents': {'$regex': '.*drain.*'}},
                                { 'issue_contents': {'$regex': '.*sleep.*'}},
                                { 'issue_contents': {'$regex': '.*charg.*'}},
                                { 'issue_contents': {'$regex': '.*volt.*'}},
                                { 'issue_contents': {'$regex': '.*sustainab.*'}},
                                { 'issue_contents': {'$regex': '.*green.*'}},
                                { 'issue_contents': {'$regex': '.*wak.*'}},
                                { 'issue_contents': {'$regex': '.*joule.*'}},
                                { 'issue_contents': {'$regex': '.*amper.*'}}
                            ] }
                                   
                        ]})
            
    elif 'commit' == k:
            energy_query = collection.find(
                    { '$nor': [ { 'Commit Info': {'$regex': '.*energy.*'}},
                                { 'Commit Info': {'$regex': '.*battery.*'}},
                                { 'Commit Info': {'$regex': '.*power.*'}},
                                { 'Commit Info': {'$regex': '.*consum.*'}},
                                { 'Commit Info': {'$regex': '.*efficien.*'}},
                                { 'Commit Info': {'$regex': '.*drain.*'}},
                                { 'Commit Info': {'$regex': '.*sleep.*'}},
                                { 'Commit Info': {'$regex': '.*charg.*'}},
                                { 'Commit Info': {'$regex': '.*volt.*'}},
                                { 'Commit Info': {'$regex': '.*sustainab.*'}},
                                { 'Commit Info': {'$regex': '.*green.*'}},
                                { 'Commit Info': {'$regex': '.*wak.*'}},
                                { 'Commit Info': {'$regex': '.*joule.*'}},
                                { 'Commit Info': {'$regex': '.*amper.*'}}
                            ] }
                        )
            
    for document in energy_query:
            original_energy_list.append(document)
            counter = counter + 1
            counter_list.append(counter)
            if counter >= 60:
                break


    new_energy_list = [i for n, i in enumerate(original_energy_list) if i not in original_energy_list[n + 1:]]
    return original_energy_list, new_energy_list, counter_list

############################
####### MAIN PROGRAM #######
############################

# MONGODB DRIVER
client = mongo_con.con.mongoClient
db = client.data_phase1


# REGEX KEYWORDS
regex_keyword = ['.*energy.*',
                 '.*battery.*',
                 '.*power.*',
                 '.*consum.*',
                 '.*efficien.*',
                 '.*drain.*',
                 '.*sleep.*',
                 '.*charg.*',
                 '.*volt.*',
                 '.*sustainab.*',
                 '.*green.*',
                 '.*wak.*',
                 '.*watt.*',
                 '.*joule.*',
                 '.*amper.*'
                ]

# BitBucket
#collection_key = ['pr_title', 'pr_contents', 'pr_comments']

# GET CLOSED/OPEN PR ENERGY DOCUMENTS
cols = {}
keys = {}
fname = {}

# BitBucket
cols["bitbucket"] = [db.BitBucketPR]
keys["bitbucket"] = ['pr_title', 
                     'pr_contents', 
                     'pr_comments']
fname["bitbucket"] = 'output_data/bitbucket_pr_data.json'

# StackOverFlow
cols["stackoverflow"] = [db.StackOverflow]
keys["stackoverflow"] = ['title', 
                         'post_content', 
                         'answer', 
                         'quote', 
                         'question_code', 
                         'answer_code']
fname["stackoverflow"] = 'output_data/new_stackoverflow_data.json'
# ROSDiscurse
cols["rosdiscurse"] = [db.ROSDiscourse]
keys["rosdiscurse"] = ['title', 
                      'thread_contents', 
                      'thread_details'
                     ]
fname["rosdiscurse"] = 'output_data/ros-discourse_data.json'

# ROSAnswers
cols["rosanswers"] = [db.ROSAnswers]
keys["rosanswers"] = ['title', 
                      'post_content', 
                      'answer',
                      'question_details',
                      'answer_details' 
                     ]
fname["rosanswers"] = 'output_data/ros-answers_data.json'

# Wiki
cols["wiki"] = [db.Wiki]
keys["wiki"] = ['package', 
                      'pakcage_summary', 
                      'package_code',
                      'package_tt',
                      'package_details'
                     ]
fname["wiki"] = 'output_data/wiki_energy_data.json'
# PRS Git
cols["prsgit"] = [db.GitHubOpenPRs, db.GitHubClosedPRs]
keys["prsgit"] = ['pr_title', 
                      'pr_contents', 
                      'pr_comments', 
                      'pr_code', 
                      'pr_quotes', 
                      'pr_details', 
                      'pr_details_more'
                     ]
fname["prsgit"] = 'output_data/github-prs_data.json'
# Open Issues
cols["issues"] = [db.GitHubOpenIssues,db.GitHubClosedIssues]
keys["issues"] = ['issue_title', 
                      'issue_contents', 
                      'issue_code', 
                      'issue_quotes', 
                      'contents_details', 
                      'contents_details_more'
                     ]
fname["issues"] = 'output_data/new_github-issues_data.json'

# Commits
cols["commit"] = [db.Commits]
keys["commit"] = [ 'Commit Info'
                  ]
fname["commit"] = 'output_data/commit_data_new.json'

# Repo
cols["repo"] = [db.GitHubRepos]
keys["repo"] = [
                    'code_comments_python',
                    'code_comments_c++', 
                    'md_contents',
                    'md_file_names'
                     ]
fname["repo"] = 'output_data/repositories_data.json'

##############################
### EXECUTION
#####
#repos = cols.values()
klist = cols.keys()
for k in klist:
    c = cols.get(k)
    collection_key = keys.get(k)
#c = [db.BitBucketPR]
    print('\n')
    no_duplicate_energy_pr = []
    for collection in c:
        print('\n')
        print (collection)
        print('\n')
        print('-------------------------------------')
        print('\n')
        print('By keyword:')
        total_duplicate_energy_pr = 0
        total_no_duplicate_energy_pr = 0
        #for rk in regex_keyword:      
        duplicate_energy_pr_stat, no_duplicate_energy_pr_stat, pr_document_term_counter_stat = get_energy_pr(collection, k)
        if len(no_duplicate_energy_pr_stat) > 0:
            for ndk in no_duplicate_energy_pr_stat:
                no_duplicate_energy_pr.append(ndk)
        total_duplicate_energy_pr += len(duplicate_energy_pr_stat)
        print("duplicate energy pr stats: ", len(duplicate_energy_pr_stat))
        print("energy pr stats: ", len(no_duplicate_energy_pr_stat))    
        print('\n')
        print('-------------------------------------')
        print('\n')
        print('Total:')
        print("duplicate energy pr: ", total_duplicate_energy_pr)
        print("energy pr: ", len(no_duplicate_energy_pr))
        print('\n')
        print('-------------------------------------')
        print('\n')
    #for i in no_duplicate_energy_pr:
    #    print(i)
    
    print("Adding to file...")
    
    with open(fname.get(k), 'a') as outfile:
        outfile.write('[')
        for item in no_duplicate_energy_pr:
    #        print(item)
            del item['_id']
            outfile.write(json.dumps(item)+'\n,')
        outfile.write(']')
        