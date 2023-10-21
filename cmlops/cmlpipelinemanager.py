"""
Class to manage CML Job Pipelines
"""

import os

class CmlPipelineManager:

    def __init__(self):
        self.PROJECT_ID = os.environ["CDSW_PROJECT_ID"]

    def createJob(self):
        """
        Method to create CML Job
        """
        raise NotImplementedError

    def runJob(self, jobId):
        """
        Method to run CML Job
        """
        raise NotImplementedError

    def deleteJob(self, jobId):
        """
        Method to delete CML Job
        """
        raise NotImplementedError

    
