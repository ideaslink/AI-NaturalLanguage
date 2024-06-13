# ------------------------------------------------------------------------------------------------
#   Copyright (c) Ideaslink. All rights reserved
#   Licensed under the MIT License. 
# ------------------------------------------------------------------------------------------------

"""
About:
    Azure AI Document Intelligence

Description:
    this program demonstrates Azure AI Document Intelligence features

Reference:
    Microsoft Azure AI Documents

Usage:
    Run the file in python environment. See samples_and_tests for details 

    Set the keys/secrets before running:

"""

import os
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult, AnalyzeDocumentRequest, ContentFormat
from azure.core.credentials import AzureKeyCredential


class DocIntelAnalysis:
    """
    azure ai - document intelligence
    """

    def __init__(self, cog_key, cog_endpoint) -> None:
        """
        create azure ai document intelligence services client
        :param cog_key:
        :param cog_endpoint:
        """
        self.credential = AzureKeyCredential(cog_key)
        self.docintelclient = DocumentIntelligenceClient(endpoint=cog_endpoint, credential=self.credential)
        
    def analyze_document(self, docurl):
        """
        analyse document from url
        """
        poller = self.docintelclient.begin_analyze_document("prebuilt-layout",
                                                            AnalyzeDocumentRequest(docurl),
                                                            output_content_format=ContentFormat.MARKDOWN)
        result: AnalyzeResult = poller.result()

        print(f"doc intel result: \n")
        print(result)



