#!/usr/bin/env python
import sys
import warnings

from ai_search_doc.crew import AiSearchDoc

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": r"""I need help with setting up a MySQL database.
        Can you provide guidance?""",
    }
    AiSearchDoc().crew().kickoff(inputs=inputs)
