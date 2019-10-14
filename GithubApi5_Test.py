import unittest
import json
from unittest import mock
import GithubApi5


class TestGithubApi(unittest.TestCase):

    @mock.patch('GithubApi5.requests.get')
    def testGetRepos(self, mockedRequest):
        mockedRequest.return_value.json.return_value = [{'name': 'joshPirog'},{'name': 'mock'}]
        self.assertIn({'name': 'joshPirog'}, GithubApi5.getRepos('mock'))

    @mock.patch('GithubApi5.requests.get')
    def testGetCommits(self, mockedRequest):
        mockedRequest.return_value.json.return_value = [{'commit': 'commitOne'},{'commit': 'commitTwo'}]
        commits = GithubApi5.getCommits('mock', 'repoMock')
        self.assertEqual(commits, 2)
                

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)