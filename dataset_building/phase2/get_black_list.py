import ssl
import json
import re
from mongodb.crud import MongoCon

ssl._create_default_https_context = ssl._create_unverified_context

def get_energy_pr(collection, rk, collection_key):
    original_energy_list = []
    counter_list = []
    counter = 0
    #### File Names
    if 'code_comments_python' in collection_key:
        with open('../../phase1_data_collection/git_scraper/data/git_repos_data.json') as f:
            d = json.load(f)
                
        for ck in collection_key:
            md_file_names = []
            code_comments_md = [item.get(ck) for item in d]
            for dictionary in code_comments_md:
                for file_name in dictionary:
                    md_file_names.append(file_name)
                    
            for name in md_file_names:
                energy_query = collection.find(
                    { ck+"."+name: {'$regex': rk} }
                )
                for document in energy_query:
                    original_energy_list.append(document)
                    counter = counter + 1
                counter_list.append(counter)                   
    else:
        for ck in collection_key:
            energy_query = collection.find(
                { ck: {'$regex': rk} }
            )
            for document in energy_query:
                txt = str(document)
                #print(len(txt))
                words = rk.split('.')
                word = words[1].split('*')
                w = word[1]
                #print(w)
                #print('\n')
                pos = txt.find(w)
                if pos > -1:
                #    print(pos)
                    print(txt[pos-20:pos+20])
                #    print('\n')
                original_energy_list.append(document)
                counter = counter + 1
            counter_list.append(counter)

    new_energy_list = [i for n, i in enumerate(original_energy_list) if i not in original_energy_list[n + 1:]]
    return original_energy_list, new_energy_list, counter_list

############################
####### MAIN PROGRAM #######
############################

# MONGODB DRIVER
client = MongoCon.con.mongoClient
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
"""
# BitBucket
cols["bitbucket"] = [db.BitBucketPR]
keys["bitbucket"] = ['pr_title', 
                     'pr_contents', 
                     'pr_comments']
fname["bitbucket"] = 'data/consum_bitbucket_pr_data.json'
# StackOverFlow
cols["stackoverflow"] = [db.StackOverflow]
keys["stackoverflow"] = ['title', 
                         'post_content', 
                         'answer', 
                         'quote', 
                         'question_code', 
                         'answer_code']
fname["stackoverflow"] = 'data/consum_new_stackoverflow_data.json'

# ROSDiscurse
cols["rosdiscurse"] = [db.ROSDiscourse]
keys["rosdiscurse"] = ['title', 
                      'thread_contents', 
                      'thread_details'
                     ]
fname["rosdiscurse"] = 'data/consum_ros-discourse_data.json'
"""

# ROSAnswers
cols["rosanswers"] = [db.ROSAnswers]
keys["rosanswers"] = ['title', 
                      'post_content', 
                      'answer',
                      'question_details',
                      'answer_details' 
                     ]
fname["rosanswers"] = 'data/consum_ros-answers_data.json'

"""
# Wiki
cols["wiki"] = [db.Wiki]
keys["wiki"] = ['package', 
                      'pakcage_summary', 
                      'package_code',
                      'package_tt',
                      'package_details'
                     ]
fname["wiki"] = 'data/wiki_energy_data.json'
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
fname["prsgit"] = 'data/consum_github-prs_data.json'
# Open Issues
cols["issues"] = [db.GitHubOpenIssues,db.GitHubClosedIssues]
keys["issues"] = ['issue_title', 
                      'issue_contents', 
                      'issue_code', 
                      'issue_quotes', 
                      'contents_details', 
                      'contents_details_more'
                     ]
fname["issues"] = 'data/consum_new_github-issues_data.json'

# Commits
cols["commit"] = [db.Commits]
keys["commit"] = [ 'Commit Info'
                  ]
fname["commit"] = 'data/consum_commit_data_new.json'

# Repo
cols["repo"] = [db.GitHubRepos]
keys["repo"] = [
                    'code_comments_python',
                    'code_comments_c++', 
                    'md_contents',
                    'md_file_names'
                     ]
fname["repo"] = 'data/consum_repositories_data.json'
"""

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
        for rk in regex_keyword:
            duplicate_energy_pr_stat, no_duplicate_energy_pr_stat, pr_document_term_counter_stat = get_energy_pr(collection, rk, collection_key)
            if len(no_duplicate_energy_pr_stat) > 0:
                for ndk in no_duplicate_energy_pr_stat:
                    no_duplicate_energy_pr.append(ndk)
            total_duplicate_energy_pr += len(duplicate_energy_pr_stat)
            print(rk)
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
        for item in no_duplicate_energy_pr:
    #        print(item)
            del item['_id']
            outfile.write(json.dumps(item))
        