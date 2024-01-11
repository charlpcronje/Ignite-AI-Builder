# test_logger.py
# Handles logging of test results

import json

log_file = "api_test_log.md"

def log_json_response(name, url, response, overview):
    with open(log_file, "w") as file:
        file.write(f"# {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write(f"### Status Code: {response.status_code}\n")
        file.write("```json\n")
        file.write(json.dumps(response.json(), indent=4) if response else "No response")
        file.write("\n```\n\n")

def log_response(name, url, response, overview):
    with open(log_file, "w") as file:
        file.write(f"# {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write("```json\n")
        file.write(json.dumps(response.json(), indent=2) if response else "No response")
        file.write("\n```\n\n")

def log_error(name, url, response, expected_status, overview):
    with open(log_file, "w") as file:
        file.write(f"# Error: {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write(f"### Expected Status: {expected_status}\n")
        file.write(f"### Actual Status: {response.status_code if response else 'No Response'}\n")
        file.write("```json\n")
        file.write(json.dumps(response.json(), indent=2) if response else "No response")
        file.write("\n```\n\n")

def log_exception(name, url, exception, overview):
    with open(log_file, "w") as file:
        file.write(f"# Exception: {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write(f"### Exception: {str(exception)}\n\n")

def log_markdown_response(name, url, response, overview):
    # Log Markdown or plain text response
    with open(log_file, "w") as file:
        file.write(f"# {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write(response.text)  # Assuming response.text contains the Markdown content

