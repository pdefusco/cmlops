"""
Class to manage git CI/CD in a CML Project
"""

# Find git python package here
# import pygithub
import os

class CmlGitManager:

    def __init__(self):
        self.projectId = os.environ["CDSW_PROJECT_ID"]

    def gitAdd(self, files):
        """
        Method to add files to git commit
        """
        raise NotImplementedError

    def gitPush(self, message):
        """
        Method to commit files added
        """
        raise NotImplementedError

    def gitPull(self):
        """
        Method to pull latest files from git repository
        """
        raise NotImplementedError


        
