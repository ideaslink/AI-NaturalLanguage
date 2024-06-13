"""
    test - document intelligence

    dependency:     python, azure ai services
    reference:      
    notes:          
"""

import unittest
import os
import sys

'''
    add path to package

    Note: the action is not needed when running in PyCharm
'''
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from document_intelligence.doc_intel_azure import DocIntelAnalysis
import document_intelligence.secretvars as commvar


class TestDocIntelAnalysisAzure(unittest.TestCase):
    """
        test functions of document intelligence analysis
        note: 
    """

    def __init__(self, *args, **kwargs):
        """
        init: create an instance of azure doc_intel_azure
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)      
        self.docintel_analysis = DocIntelAnalysis(commvar.AZURE_DOCINTEL_KEY, commvar.AZURE_DOCINTEL_ENDPOINT)
        self.text_content = ['''Enjoyed the vibrant energy and iconic attractions in Las Vegas,  but found the overall service quality lacking. Nonetheless, the unique charm of the city made for an unforgettable experience.''',
                            #  """I recently visited Las Vegas and was captivated by the vibrant energy of the city and its iconic tourist attractions. The lively atmosphere, dazzling lights, and world-renowned entertainment truly
                            #    made it a memorable experience. However, I couldn't help but notice that the overall service quality fell short of the city's grandeur. While the attractions were fantastic, there were instances where 
                            #    the service didn't quite match up to the city's reputation. Nonetheless, the charm of Las Vegas and its unique offerings outweighed these concerns, leaving me with fond memories of an unforgettable trip."""
                            '''Founded in 1975 by Bill Gates and Paul Allen, Microsoft quickly became a tech giant, achieving early success with MS-DOS and Windows. Dominating the '90s with Microsoft Office, the company faced antitrust challenges but adapted to the internet era. Under CEO Satya Nadella's leadership since 2014, Microsoft embraced cloud computing with Azure and ventured into mobile. Recent innovations in AI, cloud solutions, and collaboration reflect Microsoft's commitment to shaping the future of technology, cementing its legacy as a global tech powerhouse.'''
                            ]
        self.doc_url = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_forms/forms/Invoice_1.pdf"

    def test_analyze_doc(self):
        """
        call function to analyze document by azure document intelligence
        """
        self.docintel_analysis.analyze_document(self.doc_url)
        self.assertTrue(1)


if __name__ == "__main__":
    """ 
    unittest
    """
    unittest.main()
