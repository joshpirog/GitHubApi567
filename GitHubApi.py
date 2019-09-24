'''
Created on Sep 21, 2019

@author: Josh
'''


import requests
import json

userId = "richkempinski"
# To get user input
# userId = input("Enter GitHub user ID: ")



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
