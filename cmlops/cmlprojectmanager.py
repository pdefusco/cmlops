"""
Class to manage CML Projects via APIv2
"""

import os

class CmlProjectManager:

    def __init__(self, workspaceId):
        self.WORKSPACE_ID = workspaceId

    def createProject(self):
        raise NotImplementedError

    def deleteProject(self, projectName):
        raise NotImplementedError

    def listProjects(self):
        raise NotImplementedError

    def listProjectFiles(self, projectName):
        raise NotImplementedError
