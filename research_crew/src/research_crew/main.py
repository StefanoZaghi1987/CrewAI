#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from research_crew.crew import ResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the research  crew.
    """
    inputs = {
        'topic': 'Artificial Intelligence in Healthcare',
        'current_year': str(datetime.now().year)
    }

    try:
        # Create and run the crew
        result = ResearchCrew().crew().kickoff(inputs=inputs)

        # Print the result
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
        print("\n\nReport has been saved to output/report.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Artificial Intelligence in Healthcare",
        'current_year': str(datetime.now().year)
    }
    try:
        ResearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResearchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the research crew execution and returns the results.
    """
    inputs = {
        "topic": "Artificial Intelligence in Healthcare",
        "current_year": str(datetime.now().year)
    }

    try:
        ResearchCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()