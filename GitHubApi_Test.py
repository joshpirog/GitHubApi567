import unittest

from GitHubApi import githubInfo

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestgithubInfo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    def testGithubInfo(self):
        self.assertEqual(githubInfo("richkempinski"),'Repo hellogitworld has 30 commits.\nRepo helloworld has 6 commits.\nRepo Mocks has 10 commits.\nRepo Project1 has 2 commits.\nRepo threads-of-life has 1 commits.\n')
    
    
        
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
