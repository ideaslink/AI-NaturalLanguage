"""
    test - sentiment

    dependency:     python, azure cognitive
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

from sentiment_analysis.sentiment_analysis_azure import SentimentAnalysis
import sentiment_analysis.secretvars as commvar


class TestSentimentAnalysisAzure(unittest.TestCase):
    """
        test functions of sentiment analysis
        note: 
    """

    def __init__(self, *args, **kwargs):
        """
        init: create an instance of azure sentiment_analysis_azure
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)      
        self.sentiment_analysis = SentimentAnalysis(commvar.AZURE_COG_KEY, commvar.AZURE_COG_ENDPOINT)
        self.text_content = ['''Enjoyed the vibrant energy and iconic attractions in Las Vegas,  but found the overall service quality lacking. Nonetheless, the unique charm of the city made for an unforgettable experience.''', 
                    #    """I recently visited Las Vegas and was captivated by the vibrant energy of the city and its iconic tourist attractions. The lively atmosphere, dazzling lights, and world-renowned entertainment truly 
                    #    made it a memorable experience. However, I couldn't help but notice that the overall service quality fell short of the city's grandeur. While the attractions were fantastic, there were instances where 
                    #    the service didn't quite match up to the city's reputation. Nonetheless, the charm of Las Vegas and its unique offerings outweighed these concerns, leaving me with fond memories of an unforgettable trip.""",
                       '''Founded in 1975 by Bill Gates and Paul Allen, Microsoft quickly became a tech giant, achieving early success with MS-DOS and Windows. Dominating the '90s with Microsoft Office, the company faced antitrust challenges but adapted to the internet era. Under CEO Satya Nadella's leadership since 2014, Microsoft embraced cloud computing with Azure and ventured into mobile. Recent innovations in AI, cloud solutions, and collaboration reflect Microsoft's commitment to shaping the future of technology, cementing its legacy as a global tech powerhouse.'''
                       ]

    def test_analyze_sentiment(self):
        """
        call function to analyze sentiment in text content
        :return:
        """
        self.sentiment_analysis.analyze_sentiment(self.text_content)
        self.assertTrue(1)

    def test_abstract_summary(self):
        """
        call function to begin abstract summary
        :return:
        """
        self.sentiment_analysis.abstract_summary(self.text_content)
        self.assertTrue(1)
        
    def test_key_phrases(self):
        """
        call function to extract key phrases in doc
        """
        self.sentiment_analysis.recognize_key_phrases(self.text_content)
        self.assertTrue(True)
        
    def test_recognize_entities(self):
        """
        call function to recognize entities
        """
        self.sentiment_analysis.recognize_entities(self.text_content)
        self.assertTrue(True)
        
    def test_linked_entities(self):
        """
        call function to recognize linked entities
        """
        self.sentiment_analysis.recognize_linked_entities(self.text_content)
        self.assertTrue(True)


if __name__ == "__main__":
    """ 
    """
    unittest.main()