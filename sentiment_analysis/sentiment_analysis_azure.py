# ------------------------------------------------------------------------------------------------
#   Copyright (c) Ideaslink. All rights reserved
#   Licensed under the MIT License. 
# ------------------------------------------------------------------------------------------------

"""
About:
    Azure sentiment analysis

Description:
    this program demonstrates Azure AI sentiment analysis features

Reference:
    Microsoft Azure AI Documents

Usage:
    Run the file in python environment. See samples_and_tests for details 

    Set the keys/secrets before running:

"""

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class SentimentAnalysis:
    """
    azure ai - sentiment analysis
    """

    def __init__(self, cog_key, cog_endpoint) -> None:
        """
        create azure ai language service instance for sentiment analysis
        :param cog_key:
        :param cog_endpoint:
        """
        self.credential = AzureKeyCredential(cog_key)
        self.taclient = TextAnalyticsClient(endpoint=cog_endpoint, credential=self.credential)
        self.taclient._default_language = None

    def analyze_sentiment(self, text_content):
        """
        analyze sentiment in text content
        :param text_content:
        :return:
        """

        result = self.taclient.analyze_sentiment(text_content, show_opinion_mining=True)
        result = [x for x in result if not x.is_error]

        pos_content = [x for x in result if x.sentiment == 'positive']
        neg_content = [x for x in result if x.sentiment == 'negative']

        # general sentiment for doc
        print("\nGeneral sentiment for each sentence:\n")
        for idx, doc in enumerate(result):
            print(f"Content: {text_content[idx]}")
            print(f"sentiment: {doc.sentiment}\n")

        for ct in result:
            print(f"content sentiment: {ct.sentiment}")
            print(f"overall scores: positive: {ct.confidence_scores.positive:.2f}, netural: {ct.confidence_scores.neutral:.2f}, negative: {ct.confidence_scores.negative:.2f}\n")

            # get sentiment for each sentence
            for sentence in ct.sentences:
                print(f"Sentence: {sentence.text}\n  (sentiment: {sentence.sentiment}, score: positive {sentence.confidence_scores.positive:.2f}, neutral: {sentence.confidence_scores.neutral:.2f}, negative: {sentence.confidence_scores.negative})")
                for opinion in sentence.mined_opinions:
                    target = opinion.target
                    print(f"\t'{target.sentiment}' target '{target.text}'")
                    print(f"\t\ttarget score: positive={target.confidence_scores.positive:.2f}, negative={target.confidence_scores.negative:.2f}")
                    for assessment in opinion.assessments:
                        print(f"\t'{assessment.sentiment}' assessment '{assessment.text}'")
                        print(f"\t\tassessment scores: positive={assessment.confidence_scores.positive:.2f}, negative={assessment.confidence_scores.negative:.2f}")
            print("\n")
        print("\n")                        


