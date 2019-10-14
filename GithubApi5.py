import requests
import json

 
def getRepos(userId):
    repos = requests.get("https://api.github.com/users/" + userId + "/repos")
    repos = repos.json()
    return repos

def getCommits(userId, repoName):
    commitUrl = requests.get("https://api.github.com/repos/" + userId + "/" + repoName+ "/commits")
    commitUrl = commitUrl.json()
    return len(commitUrl)

