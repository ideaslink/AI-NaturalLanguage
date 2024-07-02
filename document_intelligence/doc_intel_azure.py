# ------------------------------------------------------------------------------------------------
#   Copyright (c) Ideaslink. All rights reserved
#   Licensed under the MIT License. 
#
#   ref: ms azure ai services
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

# import os
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
        poller = self.docintelclient.begin_analyze_document("prebuilt-layout", AnalyzeDocumentRequest(url_source=docurl))
        # poller = self.docintelclient.begin_analyze_document("prebuilt-layout", AnalyzeDocumentRequest(docurl), output_content_format=ContentFormat.MARKDOWN)
        result: AnalyzeResult = poller.result()

        if result.styles and any([style.is_handwritten for style in result.styles]):
            print("Document contains handwritten content")
        else:
            print("Document does not contain handwritten content")

        for page in result.pages:
            print(f"----Analyzing layout from page #{page.page_number}----")
            print(
                f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}"
            )

            if page.lines:
                for line_idx, line in enumerate(page.lines):
                    words = self.get_words(page, line)
                    print(
                        f"...Line # {line_idx} has word count {len(words)} and text '{line.content}' "
                        f"within bounding polygon '{line.polygon}'"
                    )

                    for word in words:
                        print(
                            f"......Word '{word.content}' has a confidence of {word.confidence}"
                        )

            if page.selection_marks:
                for selection_mark in page.selection_marks:
                    print(
                        f"Selection mark is '{selection_mark.state}' within bounding polygon "
                        f"'{selection_mark.polygon}' and has a confidence of {selection_mark.confidence}"
                    )

        if result.tables:
            for table_idx, table in enumerate(result.tables):
                print(
                    f"Table # {table_idx} has {table.row_count} rows and "
                    f"{table.column_count} columns"
                )
                if table.bounding_regions:
                    for region in table.bounding_regions:
                        print(
                            f"Table # {table_idx} location on page: {region.page_number} is {region.polygon}"
                        )
                for cell in table.cells:
                    print(
                        f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'"
                    )
                    if cell.bounding_regions:
                        for region in cell.bounding_regions:
                            print(
                                f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'"
                            )

        print("----------------------------------------")
        # print(f"result(total pages {result.pages.__len__} \n")
        print(result)

    @staticmethod
    def get_words(page, line):
        result = []
        for word in page.words:
            if DocIntelAnalysis._in_span(word, line.spans):
                result.append(word)
        return result
    

    @staticmethod
    def _in_span(word, spans):
        for span in spans:
            if word.span.offset >= span.offset and (word.span.offset + word.span.length) <= (span.offset + span.length):
                return True
        return False