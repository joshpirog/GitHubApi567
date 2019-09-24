'''
Created on Sep 21, 2019

@author: Josh
'''


import requests
import json

userId = "joshpirog"



def githubInfo(userId):
    repo = requests.get('https://api.github.com/users/' + userId + '/repos')
    repoJson = repo.json() 
    listOfRepos = []
    toString = ''
    
    for repo in repoJson:
        
        commits = requests.get('https://api.github.com/repos/' + userId + '/' + repo["name"] + '/commits')
        commitsJson = commits.json()
        commitsLen = len(commitsJson)
        
        #print("Repo " + repo["name"] + " has " + str(commitsLen) + " commits.")
        #listOfRepos.append("Repo " + repo["name"] + " has " + str(commitsLen) + " commits.")
        toString += "Repo " + repo["name"] + " has " + str(commitsLen) + " commits." + '\n'

    #print(toString)
    return toString



print(githubInfo(userId))
# listOfRepos = githubInfo(userId)
# 
# for repo in listOfRepos:
#     print(repo)








# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
# }
# url = 'http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=0021500281&RangeType=2&Season=2016-17&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'
# response = requests.get(url, timeout=5, headers=HEADERS)
# print(response.text)


# #https://api.github.com/users/richkempinski/repos
# 
# #https://api.github.com/repos/richkempinski/hellogitworld/commits
# 
# #https://api.github.com/repos/richkempinski/hellogitworld/commits
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# 
# # print(r.text)
