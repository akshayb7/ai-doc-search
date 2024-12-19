#!/usr/bin/env python
import sys
import warnings
import argparse

from ai_search_doc.crew import AiSearchDoc

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    parser = argparse.ArgumentParser(description="Run the AiSearchDoc crew.")
    parser.add_argument("--customer", type=str, required=True, help="Customer name")
    parser.add_argument("--person", type=str, required=True, help="Person name")
    parser.add_argument("--inquiry", type=str, required=True, help="Inquiry text")
    args = parser.parse_args()

    inputs = {
        "customer": args.customer,
        "person": args.person,
        "inquiry": args.inquiry,
    }
    AiSearchDoc().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
