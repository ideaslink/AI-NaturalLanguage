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

    def abstract_summary(self, text_content):
        """
        abstract summary
        """
        results = self.taclient.begin_abstract_summary(text_content).result()

        for result in results:
            if result.kind == "AbstractiveSummarization":
                print("result of abstract summaries:\n")
                [print(f"{summary.text}\n") for summary in result.summaries]                    
            elif result.is_error is True:
                print(f"Error: {result.error.message} (code: {result.error.code})")
        

    def recognize_key_phrases(self, text_content):
        """
        extract key phrases from text content
        """
        result = self.taclient.extract_key_phrases(text_content)
        print(f"\nRecognizing key phrases: \n")
        for idx, doc in enumerate(result):
            if doc.is_error:
                print(f"{doc.error.message}")
                continue
            print(f"Key phrases in doc {idx+1}: {', '.join(doc.key_phrases)}")


    def recognize_entities(self, text_content):
        """
        recognize entities from text content
        """
        result = self.taclient.recognize_entities(text_content)
        result = [content for content in result if not content.is_error]

        print(f"\nRecognizing entities: \n")
        for idx, content in enumerate(result):
            for entity in content.entities:
                print(f"Entity '{entity.text}' has category '{entity.category}'")


    def recognize_linked_entities(self, text_content):
        """
        recognize linked entities from external knowledge base (e.g. wikipedia...)
        """
        result = self.taclient.recognize_linked_entities(text_content)
        result = [content for content in result if not content.is_error]
        
        print("\nRecognizing linked entities:\n")
        for doc in result:
            for entity in doc.entities:
                url = "None" if entity.data_source is None else entity.url
                print(f"Entity '{entity.name}': link: {url}, mentioned: {len(entity.matches)} time{'s' if len(entity.matches) > 1 else ''}")


