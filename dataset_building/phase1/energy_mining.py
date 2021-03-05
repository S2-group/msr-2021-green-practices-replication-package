import ssl
import json
import sys

sys.path.insert(1, '../include/')

from mongodb import mongo_con

ssl._create_default_https_context = ssl._create_unverified_context

def get_energy_pr(collection, rk, collection_key):
    original_energy_list = []
    counter_list = []
    counter = 0
                
    #### File Names
    if 'code_comments_python' in collection_key: 
        with open('./input_data/git_repos_data.json') as f: # From JSON (Code from previous work)
            d = json.load(f)
        for ck in collection_key:
            md_file_names = []
            code_comments_md = [item.get(ck) for item in d]
            for dictionary in code_comments_md:
                for file_name in dictionary:
                    md_file_names.append(file_name)
                    
            for name in md_file_names:
                if rk == '.*power.*':
                    #query = "{ '$and': [ { "+ck+": {'$regex': '"+rk+"'}}, "+blist_regex+']}'
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*powering.*'}},
                                { ck+"."+name: {'$regex': '.*powered.*'}},
                                { ck+"."+name: {'$regex': '.*have\spower.*'}},
                                { ck+"."+name: {'$regex': '.*power\scon.*'}},
                                { ck+"."+name: {'$regex': '.*powered.*'}},
                                { ck+"."+name: {'$regex': '.*power\sbutton.*'}},
                                { ck+"."+name: {'$regex': '.*powerful.*'}},
                                { ck+"."+name: {'$regex': '.*power\soff.*'}}
                            ] } ] }
                )                
                elif rk == '.*consum.*':
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*time\sconsum.*'}},
                                { ck+"."+name: {'$regex': '.*consumer.*'}},
                                { ck+"."+name: {'$regex': '.*time-consum.*'}}
                            ] } ] }
                    )
                elif rk == '.*charg.*':
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*free\sof\scharge.*'}}
                            ] } ] }
                    )
                elif rk == '.*wak.*':
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*.benewake*'}},
                                { ck+"."+name: {'$regex': '.*nowak.*'}}
                            ] } ] }
                    )
                elif rk == '.*efficien.*':
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*coefficient.*'}}
                            ] } ] }
                    )     
                elif rk == '.*amper.*':
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*ampersand.*'}},
                                { ck+"."+name: {'$regex': '.*hamper.*'}}
                            ] } ] }
                    ) 
                elif rk == '.*sleep.*':
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*sleep().*'}},
                                { ck+"."+name: {'$regex': '.*sleep([0-9]).*'}}
                            ] } ] }
                    )
                elif rk == '.*sustainab.*':
                    energy_query = collection.find(
                        { '$and': [ { ck+"."+name: {'$regex': rk} }, { '$nor': [
                                { ck+"."+name: {'$regex': '.*unsustainable.*'}}
                            ] } ] }
                    )
                elif rk == '.*green.*':
                    energy_query = collection.find(
                        { '$and': [ { '$or': [ { ck+"."+name: {'$regex': '.*green\scomp.*'} },
                                              { ck+"."+name: {'$regex': '.*green\ssoft.*'} },
                                              { ck+"."+name: {'$regex': '.*green\stec.*'} },
                                              { ck+"."+name: {'$regex': '.*green\srobot.*'} },
                                              { ck+"."+name: {'$regex': '.*green\sit.*'} } ] }
                                   , { '$nor': [
                                { ck+"."+name: {'$regex': '.*green\slight.*'}},
                                { ck+"."+name: {'$regex': '.*green\scolor.*'}},
                                { ck+"."+name: {'$regex': '.*green\sline.*'}},
                                { ck+"."+name: {'$regex': '.*green\sdot.*'}},
                                { ck+"."+name: {'$regex': '.*green\sarrow.*'}},
                                { ck+"."+name: {'$regex': '.*not\sgreen.*'}},
                                { ck+"."+name: {'$regex': '.*green\sbox.*'}},
                                { ck+"."+name: {'$regex': '.*green\slaser.*'}},
                                { ck+"."+name: {'$regex': '.*green\spower\slight.*'}},
                                { ck+"."+name: {'$regex': '.*green\sled.*'}},
                                { ck+"."+name: {'$regex': '.*green\sLED.*'}},
                                { ck+"."+name: {'$regex': '.*are\sgreen.*'}},
                                { ck+"."+name: {'$regex': '.*green\scircle.*'}},
                                { ck+"."+name: {'$regex': '.*green\spix.*'}},
                                { ck+"."+name: {'$regex': '.*green\smarker.*'}},
                                { ck+"."+name: {'$regex': '.*green\snose.*'}},
                                { ck+"."+name: {'$regex': '.*lights\sgreen.*'}},
                                { ck+"."+name: {'$regex': '.*green\spolyg.*'}},
                                { ck+"."+name: {'$regex': '.*blinking\sgreen.*'}},
                                { ck+"."+name: {'$regex': '.*green\saxe.*'}},
                                { ck+"."+name: {'$regex': '.*green\sobject.*'}},
                                { ck+"."+name: {'$regex': '.*green\saxis.*'}},
                                { ck+"."+name: {'$regex': '.*green\sobstacle.*'}},
                                { ck+"."+name: {'$regex': '.*green\sshade.*'}},
                                { ck+"."+name: {'$regex': '.*green\ssquare.*'}},
                                { ck+"."+name: {'$regex': '.*green\simage.*'}},
                                { ck+"."+name: {'$regex': '.*green\scurve.*'}},
                                { ck+"."+name: {'$regex': '.*green\sbord.*'}},
                                { ck+"."+name: {'$regex': '.*green\sparticle.*'}},
                                { ck+"."+name: {'$regex': '.*green\ssquiggle.*'}},
                                { ck+"."+name: {'$regex': '.*green\scheck.*'}},
                                { ck+"."+name: {'$regex': '.*green\spoint.*'}},
                                { ck+"."+name: {'$regex': '.*green\sstatus.*'}}
                            ] } ] }
                    )
                else:
                    energy_query = collection.find(
                        { ck+"."+name: {'$regex': rk} }
                        )
                for document in energy_query:
                    original_energy_list.append(document)
                    counter = counter + 1
                counter_list.append(counter)                   
    else:
        for ck in collection_key:
            if rk == '.*power.*':
                #query = "{ '$and': [ { "+ck+": {'$regex': '"+rk+"'}}, "+blist_regex+']}'
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*powering.*'}},
                            { ck: {'$regex': '.*powered.*'}},
                            { ck: {'$regex': '.*have\spower.*'}},
                            { ck: {'$regex': '.*power\scon.*'}},
                            { ck: {'$regex': '.*powered.*'}},
                            { ck: {'$regex': '.*power\sbutton.*'}},
                            { ck: {'$regex': '.*powerful.*'}},
                            { ck: {'$regex': '.*power\soff.*'}}
                        ] } ] }
                )                
            elif rk == '.*consum.*':
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*time\sconsum.*'}},
                            { ck: {'$regex': '.*consumer.*'}},
                            { ck: {'$regex': '.*time-consum.*'}}
                        ] } ] }
                )
            elif rk == '.*charg.*':
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*.free\sof\scharge*'}}
                        ] } ] }
                )
            elif rk == '.*wak.*':
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*.benewake*'}},
                            { ck: {'$regex': '.*nowak.*'}}
                        ] } ] }
                )
            elif rk == '.*efficien.*':
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*coefficient.*'}}
                        ] } ] }
                )     
            elif rk == '.*amper.*':
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*ampersand.*'}},
                            { ck: {'$regex': '.*hamper.*'}}
                        ] } ] }
                ) 
            elif rk == '.*sleep.*':
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*sleep().*'}},
                            { ck: {'$regex': '.*sleep([0-9]).*'}}
                        ] } ] }
                )
            elif rk == '.*sustainab.*':
                energy_query = collection.find(
                    { '$and': [ { ck: {'$regex': rk} }, { '$nor': [
                            { ck: {'$regex': '.*unsustainable.*'}}
                        ] } ] }
                )
            elif rk == '.*green.*':
                energy_query = collection.find(
                    { '$and': [ { '$or': [ { ck: {'$regex': '.*green\scomp.*'} },
                                          { ck: {'$regex': '.*green\ssoft.*'} },
                                          { ck: {'$regex': '.*green\stec.*'} },
                                          { ck: {'$regex': '.*green\srobot.*'} },
                                          { ck: {'$regex': '.*green\sit.*'} } ] }
                               , { '$nor': [
                            { ck: {'$regex': '.*green\slight.*'}},
                            { ck: {'$regex': '.*green\scolor.*'}},
                            { ck: {'$regex': '.*green\sline.*'}},
                            { ck: {'$regex': '.*green\sdot.*'}},
                            { ck: {'$regex': '.*green\sarrow.*'}},
                            { ck: {'$regex': '.*not\sgreen.*'}},
                            { ck: {'$regex': '.*green\sbox.*'}},
                            { ck: {'$regex': '.*green\slaser.*'}},
                            { ck: {'$regex': '.*green\spower\slight.*'}},
                            { ck: {'$regex': '.*green\sled.*'}},
                            { ck: {'$regex': '.*green\sLED.*'}},
                            { ck: {'$regex': '.*are\sgreen.*'}},
                            { ck: {'$regex': '.*green\scircle.*'}},
                            { ck: {'$regex': '.*green\spix.*'}},
                            { ck: {'$regex': '.*green\smarker.*'}},
                            { ck: {'$regex': '.*green\snose.*'}},
                            { ck: {'$regex': '.*lights\sgreen.*'}},
                            { ck: {'$regex': '.*green\spolyg.*'}},
                            { ck: {'$regex': '.*blinking\sgreen.*'}},
                            { ck: {'$regex': '.*green\saxe.*'}},
                            { ck: {'$regex': '.*green\sobject.*'}},
                            { ck: {'$regex': '.*green\saxis.*'}},
                            { ck: {'$regex': '.*green\sobstacle.*'}},
                            { ck: {'$regex': '.*green\sshade.*'}},
                            { ck: {'$regex': '.*green\ssquare.*'}},
                            { ck: {'$regex': '.*green\simage.*'}},
                            { ck: {'$regex': '.*green\scurve.*'}},
                            { ck: {'$regex': '.*green\sbord.*'}},
                            { ck: {'$regex': '.*green\sparticle.*'}},
                            { ck: {'$regex': '.*green\ssquiggle.*'}},
                            { ck: {'$regex': '.*green\scheck.*'}},
                            { ck: {'$regex': '.*green\spoint.*'}},
                            { ck: {'$regex': '.*green\sstatus.*'}}
                        ] } ] }
                )
            else:
                energy_query = collection.find(
                    { ck: {'$regex': rk} }
                    )
                
            for document in energy_query:
                original_energy_list.append(document)
                counter = counter + 1
                counter_list.append(counter)

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
        outfile.write('[')
        for item in no_duplicate_energy_pr:
    #        print(item)
            del item['_id']
            outfile.write(json.dumps(item)+'\n,')
        outfile.write(']')
        
