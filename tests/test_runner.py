# test_runner.py
# Executes the API tests
import requests
from test_cases import tests
from test_logger import log_response, log_error, log_exception, log_markdown_response, log_json_response
from test_config import api_key

def test_endpoint(name, url, method, data=None, params=None, overview="", expected_status=200):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    response = None

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, json=data, headers=headers)

        # Check if response is successful and as expected
        if response and response.status_code == expected_status:
            # Check for Markdown or non-JSON response
            if response.headers.get('Content-Type') in ['text/markdown', 'text/plain']:
                log_markdown_response(name, url, response, overview)
            else:
                log_json_response(name, url, response, overview)
        else:
            log_error(name, url, response, expected_status, overview)
            log_response(name, url, response, overview)
    
    except Exception as e:
        log_exception(name, url, e, overview)

def run_tests(test_number=None):
    # Convert test_number to int if it's provided as a string
    if test_number is not None:
        try:
            test_number = int(test_number)
        except ValueError:
            print(f"Invalid test number: {test_number}")
            return

    if test_number is not None and 0 <= test_number < len(tests):
        test = tests[test_number]
        test_endpoint(test["name"], test["endpoint"], test["method"], 
                      data=test.get("data"), params=test.get("params"), 
                      overview=test["overview"], expected_status=test.get("expected_status", 200))
    else:
        for test in tests:
            test_endpoint(test["name"], test["endpoint"], test["method"], 
                          data=test.get("data"), params=test.get("params"), 
                          overview=test["overview"], expected_status=test.get("expected_status", 200))

if __name__ == "__main__":
    # Check for command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test_number = sys.argv[2] if len(sys.argv) > 2 else None
        run_tests(test_number)
    else:
        run_tests()