import unittest

from GitHubApi import githubInfo

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestgithubInfo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    def testGithubInfo(self):
        self.assertEqual(githubInfo("joshpirog"),'Repo ClassifyTriangle has 2 commits.\nRepo CS-385-Algorithms has 2 commits.\nRepo dribbble2react has 30 commits.\nRepo GitHubApi567 has 2 commits.\nRepo helloworld has 2 commits.\nRepo TriangleTest has 9 commits.\n')
    
    
        
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
