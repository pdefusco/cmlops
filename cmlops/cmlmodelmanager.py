"""
Class to manage CML model deployments
"""

import os

class CmlModelManager:

    def __init__(self):
        self.PROJECT_ID = os.environ["CDSW_PROJECT_ID"]

    def createModel(self):
        """
        Method to create a CML Model
        """
        raise NotImplementedError

    def createModelBuild(self):
        """
        Method to create a CML Model Build
        """
        raise NotImplementedError

    def createModelDeployment(self):
        """
        Method to create a CML Model Deployment
        """
        raise NotImplementedError

    def updateModelDeployment(self, modelId):
        """
        Method to change Resource Profile for previously deployed model
        """
        raise NotImplementedError

    
