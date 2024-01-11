import argparse
from test_config import endpoints
from test_runner import run_tests

# Setup argument parser
parser = argparse.ArgumentParser(description='API Tester for Ignite')
parser.add_argument('--test', type=int, help='The number of the test to run', default=None)

# Parse arguments
args = parser.parse_args()

# Run tests
run_tests(test_number=args.test)
